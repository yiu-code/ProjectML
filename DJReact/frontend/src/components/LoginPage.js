import React, {Component} from 'react';
import LoginForm from './forms/LoginForm';
import HomePage from './HomePage';
import NavBar from './NavBar';

class LoginPage extends React.Component {

    submit = data => {
        console.log(data);
    };
    render() {
        return (
            <div>
            <h1>Login page</h1>
            <NavBar></NavBar>
            <LoginForm submit={this.submit}/>
            </div>
        )
    }
};

export default LoginPage;


