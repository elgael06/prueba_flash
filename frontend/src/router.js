import React from 'react';
import {
    BrowserRouter,
    Route,
    Switch
} from 'react-router-dom';
import CrearUsuario from './pages/CrearUsuario';
import Home from './pages/Home';
import PageError from './pages/PageError';
import Usuarios from './pages/Usuarios';

export default ()=>{

    return (
        <BrowserRouter>
            <Switch>
                <Route path='/' component={Home} exact />
                <Route path='/usuarios' component={Usuarios} exact />
                <Route path='/usuario/crear' component={CrearUsuario} exact />
                <Route path='' component={PageError} />
            </Switch>
        </BrowserRouter>
    );
}