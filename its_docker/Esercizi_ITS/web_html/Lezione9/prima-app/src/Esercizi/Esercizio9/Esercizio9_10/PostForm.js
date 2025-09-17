import React from 'react'
import BlogApp from './BlogApp'
import { useState } from 'react';

const PostForm = ({aggiungiPosts}) => {

    const [titolo, setTitolo] = useState('');
    const [contenuto, setContenuto] = useState('');

    return (
        <div>
            
            Titolo<input type='text' className='form-control' id='inputTitolo' name='titolo' value={titolo} onChange={(e) => setTitolo(e.target.value)}/>
            Contenuto<input type='text' className='form-control' id='inputContenuto' name='contenuto' value={contenuto} onChange={(e) => setContenuto(e.target.value)}/>

            <button type="button" className="btn btn-primary" onClick={() => aggiungiPosts({titolo, contenuto})}>Invia</button>


        </div>
    )
}

export default PostForm