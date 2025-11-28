import React from 'react'

const PostList = ({ posts }) => {

  return (
    
    <div>

      {posts.map((p, i) => (

        <div key={i} style={{

          border: '1px solid #ccc',
          borderRadius: '6px',
          padding: '12px',
          marginBottom: '10px',
          background: '#f9f9f9'

        }}>

          <h4>{p.titolo}</h4>
          <p style={{margin: 0}}>{p.contenuto}</p>

        </div>

      ))}

    </div>

  )
  
}

export default PostList