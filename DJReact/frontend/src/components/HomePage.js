import React from 'react';
import '../App.css';
import {Link} from 'react-router-dom';
import NavBar from './NavBar';

const HomePage = () => (
    <div>
    
<div className="App">
<h1 className="myheader">Home Page</h1>
<NavBar></NavBar>
        
</div>
<div>
        <img src="https://d4kkpd69xt9l7.cloudfront.net/sys-master/root/h39/h95/9126618693662/razer-blade-15-gallery08.jpg"  ></img>
        <p>

        </p>
        <a
          className="App-link"
          href="https://www.deptagency.com/nl-nl/"
          target="_blank"
          rel="noopener noreferrer"
        >
         <h1>Welcome to Dept Agency's Lending Page</h1>
        </a>
    </div>
    </div>
        
);

export default HomePage;