import React from 'react'
import TodoItem from './TodoItem'

const TodoList = (props) => {
  return (
    
    <ul className='list-group'>

        {
            props.tasks.map((t) => {
                return (<TodoItem key={t.id} tasks={t} onDeleteTask={props.onDeleteTask} onToggleTask={props.onToggleTask}></TodoItem>)
            })
        }

    </ul>
  )
}

export default TodoList