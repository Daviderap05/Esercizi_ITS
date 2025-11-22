import React, { useState } from 'react'

const Login = () => {

    const mostraCredenziali = (e) => {

        e.preventDefault();

        setMessage(`Credenziali Utente:

        Email: ${email}
        Password: ${psw}`);

    };

    const [email, setEmail] = useState("");
    const [psw, setPsw] = useState("");
    const [message, setMessage] = useState("");

  return (
    <div className='container'>

        <h3>{message}</h3>

        <form className='row g-3'>

            <div className='col-md-6'>

                <label htmlFor='inputNome' className='form-label'>Email</label>
                <input type='text' value={email} onChange={(e)=>setEmail(e.target.value)} className='form-control' id='inputEmail'></input>

            </div>

            <div className='col-md-6'>

                <label htmlFor='inputPsw' className='form-label'>Password</label>
                <input type='password' value={psw} onChange={(p)=>setPsw(p.target.value)} className='form-control' id='inputPsw'></input>

            </div>

            <div className='col-12'>

                <button type="submit" className='btn btn-primary' onClick={mostraCredenziali} >Crea Account</button>

            </div>

        </form>

    </div>
  )
}

export default Login