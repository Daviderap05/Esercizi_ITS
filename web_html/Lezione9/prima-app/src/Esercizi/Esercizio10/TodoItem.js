import React, { useState } from "react";

const TodoItem = ({ task, onDeleteTask, onToggleTask, onUpdateTask }) => {

  const [isEditing, setIsEditing] = useState(false);
  const [editTest, setEditTest] = useState(task.text);

  const handleSave = () => {

    if (editTest.trim()) {

      onUpdateTask(task.id, editTest)
      setIsEditing(false)

    } else {

      setIsEditing(false)

    }

  }

  return (

    <li className="list-group-item d-flex justify-content-between">

      <div>

        {isEditing ? (

          <div>

            <input

              type="text"
              value={editTest}
              className="form-control d-inline-block"
              onChange={(e) => setEditTest(e.target.value)}
              onBlur={handleSave}
              onKeyDown={(e) => { if (e.key === "Enter") { handleSave() } }}
              autoFocus

            ></input>

          </div>

        ) : (

          <>

            <div>

              <input

                type="checkbox"
                checked={task.completed}
                className="form-check-input me-2"
                onChange={() => {

                  onToggleTask(task.id, task.completed);

                }}

              ></input>

              <span

                style={{

                  textDecoration: task.completed ? "line-through" : "none",

                }}

                onDoubleClick={() => setIsEditing(true)}

              >
                {task.text}

              </span>

            </div>

          </>

        )}

      </div>

      <button

        className="btn btn-danger"
        onClick={() => {

          onDeleteTask(task.id);

        }}

      >
        Delete

      </button>

    </li>

  );

};

export default TodoItem;