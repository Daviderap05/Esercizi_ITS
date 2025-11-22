from __future__ import annotations
from dataclasses import dataclass
from secrets import randbelow, randbits
import hashlib, hmac
from typing import Optional, Tuple

# --------------------------------------------------------------------
#  Utilities: HKDF (SHA-256)
# --------------------------------------------------------------------
def hkdf_sha256(ikm: bytes, salt: bytes = b"", info: bytes = b"", length: int = 32) -> bytes:
    """HKDF (RFC 5869) con SHA-256: derive key material da 'ikm'."""
    if not salt:
        salt = bytes([0] * hashlib.sha256().digest_size)
    prk = hmac.new(salt, ikm, hashlib.sha256).digest()  # Extract
    okm = b""
    t = b""
    counter = 1
    while len(okm) < length:
        t = hmac.new(prk, t + info + bytes([counter]), hashlib.sha256).digest()
        okm += t
        counter += 1
    return okm[:length]

def int_to_bytes(x: int) -> bytes:
    return x.to_bytes(max(1, (x.bit_length() + 7) // 8), "big")

# --------------------------------------------------------------------
#  Fallback primality: Miller–Rabin (probabilistico)
# --------------------------------------------------------------------
def _is_probable_prime(n: int, k: int = 16) -> bool:
    if n < 2:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small_primes:
        if n % p == 0:
            return n == p
    # n-1 = 2^r * d (d dispari)
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for _ in range(k):
        a = randbelow(n - 3) + 2  # in [2, n-2]
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for __ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def _gen_prime(bits: int) -> int:
    """Genera primo di ~bits bit (fallback standard-library)."""
    while True:
        cand = randbits(bits) | 1
        cand |= (1 << (bits - 1))  # forza MSB per avere esattamente 'bits' bit
        if _is_probable_prime(cand):
            return cand

def _gen_safe_prime_fallback(bits: int) -> Tuple[int, int]:
    """Genera p=2q+1 con q primo (fallback)."""
    if bits < 64:
        raise ValueError("Usa almeno 64 bit (meglio 512/1024/2048).")
    while True:
        q = _gen_prime(bits - 1)
        p = 2 * q + 1
        if _is_probable_prime(p):
            return p, q

# --------------------------------------------------------------------
#  Preferisci SymPy se disponibile (più veloce/robusto)
# --------------------------------------------------------------------
def generate_safe_prime(bits: int) -> Tuple[int, int]:
    """
    Ritorna (p, q) con p=2q+1 (safe prime). Usa SymPy se presente,
    altrimenti fallback Miller–Rabin.
    """
    try:
        import sympy as sp  # type: ignore
        while True:
            q = sp.randprime(2 ** (bits - 2), 2 ** (bits - 1))
            p = 2 * q + 1
            if sp.isprime(p):
                return int(p), int(q)
    except Exception:
        # Nessuna sympy o errore: fallback
        return _gen_safe_prime_fallback(bits)

# --------------------------------------------------------------------
#  Diffie–Hellman core
# --------------------------------------------------------------------
def gen_private(q: int) -> int:
    """Chiave privata in [2, q-1]."""
    if q <= 3:
        raise ValueError("q troppo piccolo")
    return randbelow(q - 2) + 2

def select_generator(p: int, q: int) -> int:
    """
    Sceglie g nel sottogruppo di ordine q (p=2q+1).
    Strategia: prendi h casuale, g = h^2 mod p. Verifica g!=1 e g^q≡1.
    """
    if p != 2 * q + 1:
        raise ValueError("p non è un safe prime rispetto a q (p != 2q+1).")
    while True:
        h = randbelow(p - 3) + 2  # [2, p-2]
        g = pow(h, 2, p)          # forza nel sottogruppo di residui quadratici
        if g != 1 and pow(g, q, p) == 1:
            return g

def gen_public(g: int, priv: int, p: int) -> int:
    return pow(g, priv, p)

def compute_shared(peer_pub: int, priv: int, p: int) -> int:
    return pow(peer_pub, priv, p)

# --------------------------------------------------------------------
#  API comoda per due partecipanti A e B
# --------------------------------------------------------------------
@dataclass
class Party:
    name: str
    priv: int
    pub: int

    @classmethod
    def create(cls, name: str, q: int, g: int, p: int) -> "Party":
        priv = gen_private(q)
        pub = gen_public(g, priv, p)
        return cls(name, priv, pub)

def derive_symmetric_key(shared: int, salt: bytes = b"DH-demo", info: bytes = b"key") -> bytes:
    """Deriva 32B da 'shared' con HKDF-SHA256 (usable in AES/ChaCha20)."""
    return hkdf_sha256(int_to_bytes(shared), salt=salt, info=info, length=32)

# --------------------------------------------------------------------
#  Demo runnable
# --------------------------------------------------------------------
def demo(bits: int = 512) -> None:
    print(f"[+] Genero safe-prime da ~{bits} bit… (usa SymPy se disponibile)")
    p, q = generate_safe_prime(bits)
    print(f"    p bit={p.bit_length()}, q bit={q.bit_length()}")

    g = select_generator(p, q)
    print(f"[+] Generatore g scelto (ordine q): g={g}")

    A = Party.create("A", q, g, p)
    B = Party.create("B", q, g, p)
    print(f"[+] A_pub={A.pub}\n[+] B_pub={B.pub}")

    sA = compute_shared(B.pub, A.priv, p)
    sB = compute_shared(A.pub, B.priv, p)
    assert sA == sB, "Segreti non coincidenti!"
    shared = sA

    key = derive_symmetric_key(shared)
    print(f"[✓] DH OK — segreto condiviso (int) ha {shared.bit_length()} bit")
    print(f"[✓] Chiave simmetrica (HKDF-SHA256, 32B): {key.hex()}")

if __name__ == "__main__":
    # Puoi alzare a 1024/2048 per più sicurezza (ci mette di più a generare p,q)
    demo(bits=512)