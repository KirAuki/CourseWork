import React, {Component, Fragment} from "react";
import {createRoot} from "react-dom/client";


import Header from "./layout/header";
import DashBoard from "./viewsc/dashboard";

import {Provider} from 'react-redux';
import store from "../store";

class App extends Component{
    render(){
        return (
            <Provider store={store}>
                <div className="react__container">
                    <Header />
                    <DashBoard />
                </div>
            </Provider>
        )
        
    }
}

const cont = document.getElementById('app')
const root = createRoot(cont);
root.render(<App />);