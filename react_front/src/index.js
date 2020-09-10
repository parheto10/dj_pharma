import React from 'react'
import ReactDOM from 'react-dom'
import {Switch, Route, BrowserRouter as Router} from "react-router-dom";
import Login from "./pages/Login";
import HomeComponent from "./components/HomeComponent";

ReactDOM.render(
    <Router>
        <Switch>
            <Route exact path="/" component={Login}></Route>
            <Route exact path="/home" component={HomeComponent}></Route>
        </Switch>
    </Router>, document.getElementById('root')
)
