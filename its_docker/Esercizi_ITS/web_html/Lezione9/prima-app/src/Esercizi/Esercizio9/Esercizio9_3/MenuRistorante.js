import React from "react";
import { piatti } from "../../../dati/piatti";

const MenuRistorante = () => {

    return(
    
        <div>

            {
            
                piatti.map((piatto) => {

                    return <ul key={piatto.id}><li>{piatto.nome}, {piatto.prezzo} euro.</li></ul>;

                })
            
            }

        </div>
    
    );
};

export default MenuRistorante