import React from 'react'

const Tabellina = (props) => {

        const tab = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

  return (
    <div>

        {

            tab.map((n)=>{

                return <p>{n*props.moltiplicatore}</p>

        })

    }</div>
  )
}

export default Tabellina