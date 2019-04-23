import React, { Component } from 'react';
import request from 'superagent';

// layout
import LayoutDefault from '../../layout/Default';

// components
import Loading from '../../components/Loading';
import ProductAmount from '../../components/ProductAmount';

class ProductSingle extends Component {
  constructor(props) {
    super(props);
    this.state = {
      loading: true,
      response: null,
      price: Math.round(Math.random() * Math.floor(20)) // don't do this
    };
  }

  componentDidMount() {
    this.getProduct(this.props.match.params.id);
  }

  getProduct(id) {
    request.get(`https://reqres.in/api/product/${id}`).then(response => {
      this.setState({
        response: response.body.data,
        loading: false
      });
    });
  }

  render() {
    const { loading, response, price } = this.state;
    return (
      <React.Fragment>
        <LayoutDefault simple="true">
          <div className="wrapper">
            {loading ? (
              <Loading text="Product ophalen..." />
            ) : response ? (
              <div className="product-detail">
                <figure className="product-image">
                  <img
                    src="https://source.unsplash.com/random"
                    alt={response.name}
                  />
                </figure>
                <div className="product-information">
                  <h1 className="product-information__title">
                    {response.name}
                  </h1>
                  <span className="product-information__price">
                    &euro;{price}
                  </span>
                  <p className="product-information__description">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. In
                    eget leo sed eros varius ultrices sed nec risus. Nulla
                    mattis tellus tellus, vel ornare nulla porttitor nec. Donec
                    et libero erat. Morbi justo ante, pretium ut eros a!
                  </p>
                  <ul className="specifications">
                    <li>
                      <span>Jaar</span>
                      {response.year}
                    </li>
                    <li>
                      <span>Kleur</span>
                      {response.color}
                    </li>
                    <li>
                      <span>Idk?</span>
                      {response.pantone_value}
                    </li>
                  </ul>
                  <div className="add-to-cart">
                    <ProductAmount id={response.id} />
                  </div>
                </div>
              </div>
            ) : (
              <p>Er ging iets fout!</p>
            )}
          </div>
        </LayoutDefault>
      </React.Fragment>
    );
  }
}

export default ProductSingle;
