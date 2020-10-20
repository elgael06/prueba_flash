import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom';
import { IP_API } from '../constants/ip_services';

const Usuarios = ()=>{
    const [lista,setLista] = useState([]);

    useEffect(()=>{
        getData();
    },[]);

    const getData = async () =>{
        const res = await fetch(`${IP_API}/api/getUsuarios/`);
        console.log('res=> ',res);
        const data = await res.json();
        console.log(data);
        setLista(data); 
    }

    return <div>
        <h3>Usuarios</h3>
        <Link to='/usuario/crear'>nuevo</Link>
        <hr/>
        <ol>
            {
            lista.map(e=><li key={e.id}>
                <img src={`${IP_API+'/' + e.img}`} height='80' alt='avatar' />
                <b> {`${e.nombre} ${e.apeido} `} </b>
                <u>{e.fecha_alta}</u>
            </li>)
            }
        </ol>
    </div>
}
export default Usuarios;