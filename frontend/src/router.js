import React from 'react';
import {
    BrowserRouter,
    Route,
    Switch
} from 'react-router-dom';
import Home from './pages/home';

export default ()=>{

    return (
        <BrowserRouter>
            <Switch>
                <Route path='/' component={Home} />
            </Switch>
        </BrowserRouter>
    );
}