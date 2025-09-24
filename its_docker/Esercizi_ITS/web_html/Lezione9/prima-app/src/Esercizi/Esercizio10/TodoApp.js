import React, { useState, useEffect } from 'react'
import TodoList from './TodoList'
import TodoForm from './TodoForm'

const API_URL = "http://localhost:4000/tasks"

const TodoApp = () => {
    
  const [tasks, setTasks] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  const getTasks = async () => {

    setLoading(true)

    try {

      const response = await fetch(API_URL)
      if (!response.ok) throw new Error("Errore nella fetch")
      const data = await response.json()

      setTasks(data)
      setError(null)

    } catch (err) {

      setError(err)

    } finally {

      setLoading(false)
    }
  }

  const deleteTask = async (id) => {

    try {

      const res = await fetch(API_URL + "/" + id, { method: "DELETE" })
      if (!res.ok) throw new Error("Errore eliminazione task")
      await getTasks()

    } catch (err) {

      setError(err)
    }
  }

  const toggleTask = async (id, completed) => {

    try {

      const res = await fetch(API_URL + "/" + id, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ completed: !completed })
      })

      if (!res.ok) throw new Error("Errore aggiornamento task")
      await getTasks()

    } catch (err) {

      setError(err)
    }
  }

  useEffect(() => {

    getTasks()

  }, [])

  if (loading) return <div>Caricamento…</div>
  if (error) return <div>Errore: {error.message}</div>

  return (
    <div>
      <h1>TodoApp</h1>
      <TodoForm />
      <TodoList
        tasks={tasks}
        onDeleteTask={deleteTask}
        onToggleTask={toggleTask}
      />
    </div>
  )
}

export default TodoApp
