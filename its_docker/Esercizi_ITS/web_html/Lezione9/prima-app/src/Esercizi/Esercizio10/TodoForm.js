import React from 'react'
import { useState } from 'react';

const TodoForm = ({onAddTask}) => {

  const [text, setText] = useState("");

  const handleSubmit = (e) => {

    e.preventDefault();
    if (!text.trim()) return
    onAddTask(text)

  }

  return (

    <form className='d-flex mb-3' onSubmit={handleSubmit}>

      <input type='text' className='form-control me-2' value={text} onChange={(e) => setText(e.target.value)}></input>
      <button className='btn btn-primary'>Aggiungi task</button>
      
    </form>

  )

}

export default TodoForm 