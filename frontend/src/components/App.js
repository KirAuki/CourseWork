import React, {Component, Fragment} from "react";
import ReactDOM from "react-dom";
import Header from "./layout/header";


class App extends Component{
    render(){
        return (
            <Fragment>
                <Header />
            </Fragment>
        )
        
    }
}

ReactDOM.render(<App />, document.getElementById('app'));