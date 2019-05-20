import React, {Component} from 'react';
import NavBar from '../components/NavBar';

class ProductPage extends React.Component {

    render() {
        return (
            <div>
            <h1>Product Page</h1>
            <NavBar></NavBar>

            <p>Welcome to the Product page. You can find all the Products here!</p>
            </div>
        )
    }
};

export default ProductPage;
