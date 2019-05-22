import React, {Component} from 'react';
import NavBar from '../components/NavBar';
import Footer from './Footer';

class ProductPage extends React.Component {

    render() {
        return (
            <div>
            <h1>Product Page</h1>
            <NavBar></NavBar>

            <p>Welcome to the Product page. You can find all the Products here!</p>
            <button type="button" class="btn btn-light">View recommended</button>
            <section class="products">

  <div class="product-card">
    <div class="product-image">
      <img src="data:image/jpeg;base64,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"/>
    </div>
    <div class="product-info">
      <h5>product naam</h5>
      <h6>$99.99</h6>
    </div>
  </div>
    </section>

    <Footer></Footer>
    </div>

        )
    }
};

export default ProductPage;