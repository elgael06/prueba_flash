import React, { useState } from 'react'
import { useHistory } from 'react-router';
import Loading from '../components/Loading';
import { IP_API } from '../constants/ip_services';



const CrearUsuario = () => {
    const history = useHistory();
    const [values ,setValues] = useState({
        nombre:'',
        ap:'',
    });
    const [cargando,setCargando] = useState(false);

    const saveUsuarios = async e =>{
        setCargando(true);
        const formData = new FormData();
        const fileField = document.querySelector("input[type='file']");

        console.log(fileField.files[0]);
        formData.append('avatar',fileField.files[0]);
        formData.append('nombre',values.nombre);
        formData.append('apeido',values.ap);

        e.preventDefault();
        const res = await fetch(`${IP_API}/api/addUsuarios/`,{
            method:'POST',
            body:formData
        });
        const data = await res.json();
        console.log(data);
        alert(data.message);
        setTimeout(()=>{
            setCargando(false);
            history.push('/usuarios');
        },1000)
    }

    return(<div>
        <h4>Nuevo Usuario</h4>
       {cargando ? <Loading/> : <form onSubmit={saveUsuarios}>
            <label>Nombre</label>
            <input 
                value={values.nombre} 
                onChange={e=>setValues({...values,nombre:e.target.value})} 
                required
            />
            <label>Apeido</label>
            <input 
                value={values.ap}
                onChange={e=>setValues({...values,ap:e.target.value})}
                required
            />
            <input 
                type='file' 
                accept="image/png, image/jpeg" 
                max='1000'
                required
            />
            <button type='submit' > Enviar</button>
        </form>}
    </div>);
}

export default CrearUsuario;