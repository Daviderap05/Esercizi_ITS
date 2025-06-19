import React from 'react'

const Stampanumeri = () => {

    const num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

  return (
    
    <div>

        {
            num.map((n)=>{
                return <p>{n}</p>
            })
        }

    </div>
  )
}

export default Stampanumeri