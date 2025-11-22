import React from "react";

const CardUtente = (props) => {

    return (

        <div>
            
            <h2>{props.nome}</h2> 
            <p>{props.email}</p>
            <img src={props.imgUrl} alt="Avatar utente" />
            
        </div>
    )
}

export default CardUtente