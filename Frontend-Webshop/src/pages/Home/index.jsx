import React, { Component } from 'react';
import request from 'superagent';

// layout
import LayoutDefault from '../../layout/Default';

// components
import PageHero from '../../components/PageHero';
import Loading from '../../components/Loading';
import ProductGrid from '../../components/ProductGrid';
import SimpleHeading from '../../components/SimpleHeading';

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      loading: true,
      response: null
    };
  }

  componentDidMount() {
    this.getFeaturedProducts();
  }

  getFeaturedProducts = () => {
    request.get(`https://reqres.in/api/product?per_page=3`).then(response => {
      this.setState({
        response: response.body,
        loading: false
      });
    });
  };

  render() {
    const { loading, response } = this.state;
    return (
      <React.Fragment>
        <LayoutDefault className="home">
          <PageHero
            intro
            title="Welcome!"
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eget lorem lacus."
            image="https://images.unsplash.com/photo-1504392308976-1668b20126a4?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=98cef3ebd4d78106480ef3229c7071d1&auto=format&fit=crop&w=2500&q=100"
          />
          <div className="wrapper">
            {loading ? (
              <Loading text="Producten ophalen..." />
            ) : response && response && response.data.length > 0 ? (
              [
                <SimpleHeading
                  title="Uitgelichte producten"
                  description="Lorem ipsum dolor sit amet, consectetur adipiscing"
                  key="heading"
                />,
                <ProductGrid items={response.data} key="grid" />
              ]
            ) : (
              <p>Geen producten gevonden...</p>
            )}
          </div>
        </LayoutDefault>
      </React.Fragment>
    );
  }
}

export default Home;
