import React from 'react';
import {Route} from 'react-router-dom';
import './App.css';
import Background from './components/Background';
import HomePage from './components/HomePage';
import LoginPage from './components/LoginPage';
import ProductPage from './components/ProductPage';



const App = () =>(
 
  <div className="ui container">
    <Route path="/" exact component={HomePage}/>
    <Route path="/login" exact component={LoginPage}/>
    <Route path="/productpage" exact component={ProductPage}/>
  </div>
);

export default App;
