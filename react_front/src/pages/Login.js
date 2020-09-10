import React from "react";
import GoogleFontLoader from 'react-google-font-loader';

import 'adminbsb-materialdesign/plugins/bootstrap/css/bootstrap.min.css';
import 'adminbsb-materialdesign/plugins/node-waves/waves.css';
import 'adminbsb-materialdesign/plugins/animate-css/animate.css';
import 'adminbsb-materialdesign/css/style.css';
import AuthHandler from "../utils/AuthHandler";



class Login extends React.Component {

    state = {
        username  : "",
        password  : "",
        btnDesable : true,
        loginStatus:0
    }

    saveInputs = (event) =>{
        var key = event.target.name;
        this.setState({[key]:event.target.value});
        if (this.state.username !=="" && this.state.password !=="") {
            this.setState({btnDesable: false});
        } else {
            this.setState({btnDesable: true});
        }
    }

    formSubmit = (event) =>{
        event.preventDefault();
        console.log(this.state);
        this.setState({loginStatus:1});
        AuthHandler.login(this.state.username, this.state.password,this.handleAjaxResponse
        );
    }

    handleAjaxResponse = (data) => {
        console.log(data);
        if(data.error){
            this.setState({loginStatus:4});
        } else {
            this.setState({loginStatus:3});
        }
    }

    getMessages =() => {
        if (this.state.loginStatus===0){
            return""
        } else if (this.state.loginStatus === 1){
            return (
                <div className="alert alert-waarning" style={{ textAlign: "center" }}>
                    <strong>Connexion en cours</strong>  un instant SVP...
                </div>
            );
        } else if (this.state.loginStatus === 3){
            return (
                <div className="alert alert-success" style={{ textAlign: "center" }}>
                    <strong>Connexion Réussie!</strong>  Bienvenue
                </div>
            );
        } else if (this.state.loginStatus === 4){
            return (
                <div className="alert alert-danger" style={{ textAlign: "center" }}>
                    <strong>Connexion invalide!</strong>  Réessayer SVP ...
                </div>
            );
        }
    };

    render() {
        document.body.className='login-page';
        return(
            <React.Fragment>
            <GoogleFontLoader
              fonts={[
                {
                  font: 'Roboto',
                  weights: [400, 700],
                }
              ]}
              subsets={['latin' ,'cyrillic-ext']}
            />

            <GoogleFontLoader
              fonts={[
                {
                  font: 'Material+Icons',
                }
              ]}
            />

            <div className="login-box">
                <div className="logo">
                    <a href="javascript:void(0);">Easy<b>PHARMA</b></a>
                    <small>Veuillez Saisir vos Paramètres de Connexions</small>
                </div>
                <div className="card">
                    <div className="body">
                        <form id="sign_in" method="POST" onSubmit={this.formSubmit}>
                            <div className="msg"><strong>Connexion</strong></div>
                            {this.getMessages()}
                            <div className="input-group">
                        <span className="input-group-addon">
                            <i className="material-icons">person</i>
                        </span>
                                <div className="form-line">
                                    <input type="text" className="form-control" name="username"
                                       placeholder="nom utilisateur"
                                       required autoFocus
                                       onChange={this.saveInputs}
                                    />
                                </div>
                            </div>
                            <div className="input-group">
                        <span className="input-group-addon">
                            <i className="material-icons">lock</i>
                        </span>
                                <div className="form-line">
                                    <input type="password" className="form-control" name="password"
                                       placeholder="mot de passe" required
                                       onChange={this.saveInputs}
                                    />
                                </div>
                            </div>
                            <div className="row">
                                {/*<div className="col-xs-6 p-t-5">*/}
                                {/*    <input type="checkbox" name="rememberme" id="rememberme"*/}
                                {/*           className="filled-in chk-col-pink" />*/}
                                {/*        <label htmlFor="rememberme">Rester Connecter</label>*/}
                                {/*</div>*/}
                                <div className="col-xs-6 col-xs-offset-3">
                                    <button className="btn btn-block bg-pink waves-effect"
                                            type="submit" desabled={this.state.btnDisabled}>
                                        CONNEXION
                                    </button>
                                </div>
                            </div>
                            <div className="row m-t-15 m-b--20">
                                <div className="col-xs-6">
                                    <a href="sign-up.html">Inscription!</a>
                                </div>
                                <div className="col-xs-6 align-right">
                                    <a href="forgot-password.html">Mot de passe Oublié?</a>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
            </React.Fragment>
        )
    }
}

export default Login;