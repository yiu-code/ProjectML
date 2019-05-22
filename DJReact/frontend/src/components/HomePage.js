import React from 'react';
import '../App.css';
import {Link} from 'react-router-dom';
import NavBar from './NavBar';
import Footer from './Footer';
import Background from './Background';

const HomePage = () => (
    <div>
    
<div className="App">
<h1 className="myheader">Home Page</h1>
<NavBar></NavBar>
</div>
<div> 
    <Background/>
    <br/>
        <Footer/>
    </div>
    </div>
        
);

export default HomePage;