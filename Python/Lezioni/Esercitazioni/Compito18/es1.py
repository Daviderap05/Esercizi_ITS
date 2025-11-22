# class Member:
#     def __init__(self, member_id, name, borrowed_books=None):
#         if borrowed_books is None:
#             borrowed_books = []
#         self.member_id = member_id
#         self.name = name
#         self.borrowed_books = borrowed_books

#     def borrow_book(self, book_id):
#         if book_id not in self.borrowed_books:
#             self.borrowed_books.append(book_id)
#         else:
#             raise ValueError("Errore, libro già presente nella lista")

#     def return_book(self, book_id):
#         if book_id in self.borrowed_books:
#             self.borrowed_books.remove(book_id)
#         else:
#             raise ValueError("Book not borrowed by this member")


# class Book:
#     def __init__(self, book_id, title, author, is_borrowed=False):
#         self.book_id = book_id
#         self.title = title
#         self.author = author
#         self.is_borrowed = is_borrowed

#     def borrow(self):
#         if self.is_borrowed:
#             raise ValueError("Book is already borrowed")
#         self.is_borrowed = True

#     def return_book(self):
#         if not self.is_borrowed:
#             raise ValueError("Libro non è in prestito")
#         self.is_borrowed = False


# class Library:
#     def __init__(self):
#         self.books = {}
#         self.members = {}

#     def add_book(self, book_id, title, author):
#         self.books[book_id] = Book(book_id, title, author)

#     def register_member(self, member_id, name):
#         self.members[member_id] = Member(member_id, name)

#     def borrow_book(self, member_id, book_id):
#         member = self.members.get(member_id)
#         if not member:
#             raise ValueError("Member not found")

#         book = self.books.get(book_id)
#         if not book:
#             raise ValueError("Book not found")

#         member.borrow_book(book_id)
#         book.borrow()


#     def return_book(self, member_id, book_id):
#         member = self.members.get(member_id)
#         if not member:
#             raise ValueError("Member not found")

#         book = self.books.get(book_id)
#         if not book:
#             raise ValueError("Book not found")

#         member.return_book(book_id)
#         book.return_book()

#     def get_borrowed_books(self, member_id):
#         member = self.members.get(member_id)
#         if not member:
#             raise ValueError("Membro non trovato")
#         return [self.books[b].title for b in member.borrowed_books]



# class RecipeManager():
#     def __init__(self):
#         self.ricette: dict[str, list[str]] = {}
        
#     def create_recipe(self, name: str, ingredients: list[str]):
#         if name not in self.ricette:
#             self.ricette[name] = ingredients
#         else:
#             return "Errore ricetta già esistente"
        
#         return {name : self.ricette[name]}
    
#     def add_ingredient(self, recipe_name: str, ingredient: str):
#         if recipe_name in self.ricette:
#             if ingredient not in self.ricette[recipe_name]:
#                 self.ricette[recipe_name].append(ingredient)
#             else:
#                 return "Ingrediente già presente"
#         else:
#             return "Errore ricetta non esistente"
        
#         return {recipe_name : self.ricette[recipe_name]}
    
#     def remove_ingredient(self, recipe_name: str, ingredient: str):
#         if recipe_name in self.ricette:
#             if ingredient in self.ricette[recipe_name]:
#                 self.ricette[recipe_name].remove(ingredient)
#             else:
#                 return "Errore"
#         else:
#             return "Errore"
        
#         return {recipe_name : self.ricette[recipe_name]}
    
#     def update_ingredient(self, recipe_name: str, old_ingredient: str, new_ingredient: str):
#         if recipe_name in self.ricette:
#             if old_ingredient in self.ricette[recipe_name]:
#                 index: int = self.ricette[recipe_name].index(old_ingredient)
#                 self.ricette[recipe_name][index] = new_ingredient
#             else:
#                 return "Ingrediente non presente"
#         else:
#             return "Errore ricetta non esistente"
        
#         return {recipe_name : self.ricette[recipe_name]}
    
#     def list_recipes(self):
#         lista_r = []
#         for k in self.ricette.keys():
#             lista_r.append(k)
        
#         return lista_r
    
#     def list_ingredients(self, recipe_name: str):
#         if recipe_name in self.ricette:
#             return self.ricette[recipe_name]
#         else:
#             return "Errore ricetta non esistente"
        
#     def search_recipe_by_ingredient(self, ingredient: str):
#         diz = {}
#         for k, v in self.ricette.items():
#             if ingredient in v:
#                 diz[k] = v
                
#         if diz:
#             return diz
        
#         return "Nessuna ricetta contiene l'ingrediente"
    

# class Account:
#     def __init__(self, account_id: str, balance: float):
#         self.account_id: str = account_id
#         self.balance: float = balance
        
#     def deposit(self, amount: float):
#         self.balance += amount
        
#     def get_balance(self):
#         return self.balance
    
# class Bank:
#     def __init__(self, accounts: dict[str, Account] = {}):
#         self.accounts: dict[str, Account] = accounts
        
#     def create_account(self, account_id):
#         if account_id not in self.accounts:
#             self.accounts[account_id] = 0
#         else:
#             raise KeyError ("Account with this ID already exists")
        
#     def deposit(self, account_id, amount):
#         if account_id in self.accounts:
#             self.accounts[account_id] = amount
#         else:
#             raise KeyError ("Account with this ID not exists")
        
#     def get_balance(self, account_id):
#         if account_id not in self.accounts:
#             raise KeyError ("Account not found")
#         else:
#             return self.accounts[account_id]


# class Veicolo:
    
#     def __init__(self, marca: str, modello: str, anno: int):
#         self.marca: str = marca
#         self.modello: str = modello
#         self.anno: str = anno
        
#     def descrivi_veicolo(self):
#         print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}")


# class Auto(Veicolo):
#     def __init__(self, marca: str, modello: str, anno: int, numero_porte: int):
#         super().__init__(marca, modello, anno)
#         self.numero_porte: int = numero_porte
        
#     def descrivi_veicolo(self):
#         print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.numero_porte}")
        

# class Moto(Veicolo):
#     def __init__(self, marca: str, modello: str, anno: int, tipo: str):
#         super().__init__(marca, modello, anno)
#         self.tipo: str = tipo
        
#     def descrivi_veicolo(self):
#         print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}")



# def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:
#     dizionario: dict[str, list[int]] = {}
#     for k, v in tuples:
#         if k in dizionario:
#             dizionario[k].append(v)
#         else:
#             dizionario[k] = [v]
            
#     return dizionario
            
# print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)]))


# def trova_chiave_per_valore(dizionario: dict[str: int], valore: int) -> str:
#     for k, v in dizionario.items():
#         if v == valore:
#             return k
        
#     return None


# def sum_above_threshold(numbers: list[int], threshold: int = 20) -> int:
#     somma = 0
#     for n in numbers:
#         if n > threshold:
#             somma += n
#     retur


# def frequency_dict(elements: list) -> dict:
#     dizionario: dict[str, int] = {}
#     for e in elements:
#         if e in dizionario:
#             dizionario[e] += 1
#         else:
#             dizionario[e] = 1
#     return dizionario


# def check_access(username: str, password: str, is_active: bool) -> str:
#     if username == "admin" and password == "12345" and is_active:
#         return "Accesso consentito"
#     else:
#         return "Accesso negato"



# def print_seq(): 
    
#     print("Sequenza a):")
#     for n in range(1, 8):
#         print(n)

#     print("\nSequenza b):")
#     for n in range(3, 24, 5):
#         print(n)

#     print("\nSequenza c):")
#     for n in range(20, -11, -6):
#         print(n)

#     print("\nSequenza d):")
#     for n in range(19, 52, 8):
#         print(n)


# def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
#     if conditionA or (conditionB and conditionC):
#         return "Operazione permessa"
#     return "Operazione negata"


# def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
#     for key, value in dict2.items():
#         if key not in dict1:
#             dict1[key] = value
#         else:
#             dict1[key] += value
            
#     return dict1

# print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))



# def classifica_numeri(lista: int) -> dict[str, list[int]]:
#     diz: dict[str, list[int]] = {'pari':[], 'dispari':[]}
    
#     for n in lista:
#         if n % 2 == 0:
#             diz['pari'].append(n)
#         else:
#             diz['dispari'].append(n)
#     return diz



# def transform(x: int) -> int:
#     if x % 2 == 0:
#         return x / 2
#     return x*3-1


# def filtra_e_mappa(prodotti: dict[str, float]) -> dict[str, float]:
#     diz: dict[str, float] = {}
    
#     for key, value in prodotti.items():
#         if value > 20:
#             diz[key] = value * 0.9
            
#     return diz


# rimane l'ultimo


# def num_ord(lista_n: list[float] = []) -> tuple[float, float]:
    
#     if not lista_n:
#         raise ValueError ("Errore... inserire una lista di numeri.")
    
#     n_min: float = lista_n[0]
#     n_max: float = lista_n[0]
    
#     for n in lista_n:
#         if n > n_max:
#             n_max = n
#         elif n < n_min:
#             n_min = n
            
#     return (n_min, n_max)
            
# print(num_ord([2, -4, 3, 7]))
# print(num_ord())



# import string
# def fun(l: list[str]) -> dict[str, int]:
#     diz: dict[str, int] = {}
    
#     for s in l:
#         s = s.lower().strip().split()
        
#         for j in s:
#             j = j.strip(string.punctuation)
#             if j not in diz:
#                 diz[j] = 1
#             else:
#                 diz[j] += 1
                
#     return diz



# def fun(l: list[str]) -> dict[str, int]:
    
    # diz: dict[str, int] = {}
    
    # for s in l:
    #     s = s.lower().strip().split()

    #     for i in s:
    #         parola: str = ""
            
    #         for j in i:
                
    #             if j.isalpha():
    #                 parola += j
                    
    #         if parola not in diz:
    #             diz[parola] = 1
    #         else:
    #             diz[parola] += 1
                 
    # return diz
                    

# s = "Ciao , come stai,"
# s = s.lower().strip().split()
# print(s)

# print(fun(["Ciao! come", "ci,ao,"]))



# def fun(l: list[int]):

#     lista = [l[0]]
    
#     for i in l[1:]:
#         placed = False
        
#         for j in lista:
#             if i <= j:
                
#                 lista.insert(lista.index(j), i)
#                 placed = True
#                 break
            
#         if not placed:
#             lista.append(i)
            
#     return lista
    

# print(fun([1, 0, 5, 2, 3]))