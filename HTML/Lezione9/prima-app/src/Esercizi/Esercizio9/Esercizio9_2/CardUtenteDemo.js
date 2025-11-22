import React from 'react'
import CardUtente from './CardUtente'

const CardUtenteDemo = () => (
  <div>

    <CardUtente
      nome="Davide"
      email="aaa.aaa@gmail.com"
      imgUrl="https://placehold.co/600x400"
    />

    <CardUtente
      nome="Marco"
      email="marco@example.com"
      imgUrl="https://placehold.co/400x300"
    />
    
  </div>
);

export default CardUtenteDemo