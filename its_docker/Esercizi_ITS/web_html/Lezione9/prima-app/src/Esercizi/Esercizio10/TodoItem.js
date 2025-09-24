import React from 'react'

const TodoItem = ({tasks, onDeleteTask, onToggleTask}) => {
  return (
    <li className='list-group-item d-flex justify-content-between' >

        <div>

            <input 
                type='checkbox' 
                checked={tasks.completed} 
                className='form-form-check-input me-2' 
                onChange={() => {onToggleTask(tasks.id, tasks.completed)}}
            >
            </input>
            
            <span style={{textDecoration: tasks.completed ? 'line-through' : 'none'}}>{" "} {tasks.text}</span>

        </div>
        
       <button className='btn btn-danger' onClick={() => {onDeleteTask(tasks.id)}}>Delete</button>

    </li>
  )
}

export default TodoItem 