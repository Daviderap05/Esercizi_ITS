import React from 'react'
import { useState, useEffect} from 'react';

const urlUser = "https://jsonplaceholder.typicode.com/users";
const urlAlbums = "https://jsonplaceholder.typicode.com/albums";
const urlPhotos = "https://jsonplaceholder.typicode.com/photos";

const UserAlbum = () => {

    const [user, setUser] = useState([]);
    const [userSelected, setUserSelected] = useState(0);

    const [albums, setAlbums] = useState([]);
    const [filteredAlbums, setFilteredAlbums] = useState([]);

    const [photos, setPhotos] = useState([]);
    const [filteredPhotos, setFilteredPhotos] = useState([]);


    const getUser = async () => {

        try {

            const response = await fetch(urlUser);
            const result = await response.json();
            setUser(result);

        } catch ( error ) {

            console.error( "Errore nel caricamento utenti:", error );

        }
    };

    const getAlbums = async () => {

        try {

            const response = await fetch(urlAlbums);
            const result = await response.json();
            setAlbums(result);

        } catch (error) {

            console.error("Errore nel caricamento album:", error);

        }
    };

    const getPhotos = async () => {

        try {

            const response = await fetch(urlPhotos);
            const result = await response.json();
            setPhotos(result);

        } catch (error) {

            console.error("Errore nel caricamento album:", error);

        }
    };

    useEffect(() => {

        getUser();
        getAlbums();
        getPhotos();

    }, []);

    useEffect(() => {

        if (userSelected) {

            const filtered = albums.filter((album) => album.userId === parseInt(userSelected));
            setFilteredAlbums(filtered);

        } else {

            setFilteredAlbums([]);

        }

    }, [userSelected, albums]);

    return (

        <div className="container">

            <h1>Gestione albums photos</h1>

            <div className="row">

                <div className="col-6">

                    <select className="form-select" value={userSelected} onChange={(e) => setUserSelected(e.target.value)}>
                        
                        <option value="">Seleziona utente</option>

                        {user.map((u) => {

                            return (

                                <option key={u.id} value={u.id}>{u.name}</option>
                            
                            );

                        })}
                        
                    </select>

                </div>

                <div className="col-6">

                    <select className="form-select">

                        <option value="0">Seleziona l'album</option>

                        {filteredAlbums.map((a) => (

                            <option key={a.id} value={a.id}>{a.title}</option>

                        ))}

                    </select>

                </div>
            
            </div>

            <div className="row">

                <div className="col-12"></div>

            </div>

        </div>
    );
}

export default UserAlbum;