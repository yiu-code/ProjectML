import React, { Component } from 'react';
import { Link, NavLink } from 'react-router-dom';

class Header extends Component {
  render() {
    const { simple } = this.props;
    const cartAmount = window.localStorage.getItem('cart')
      ? JSON.parse(window.localStorage.getItem('cart')).length
      : 0;
    return (
      <header className={`header${simple ? ' header--simple' : ''}`}>
        <div className="wrapper">
          <h1 className="header__logo">
            <Link to="/">
              <img
                src="https://www.keytoe.nl/wp-content/themes/keytoe-new/assets/images/keytoe_logo_wit.svg"
                alt="Keytoe"
                title="Keytoe"
              />
            </Link>
          </h1>
          <div className="header__navigation">
            <NavLink exact activeClassName="is-active" to="/">
              Home
            </NavLink>
            <NavLink activeClassName="is-active" to="/overzicht">
              Producten
            </NavLink>
            <NavLink exact activeClassName="is-active" to="/inloggen">
              Mijn account
            </NavLink>
            <NavLink exact activeClassName="is-active" to="/winkelmand">
              Winkelmand ({cartAmount})
            </NavLink>
          </div>
        </div>
      </header>
    );
  }
}

export default Header;
