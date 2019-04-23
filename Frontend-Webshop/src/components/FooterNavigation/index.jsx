import React, { Component } from "react";
import { NavLink } from "react-router-dom";

class FooterNavigation extends Component {
  constructor(props) {
    super(props);
    this.state = {
      width: null
    };
  }

  render() {
    return (
      <footer className="footer-navigation">
        <div className="wrapper">
          <div className="footer-navigation__columns">
            <div className="footer-navigation__list">
              <h4 className="footer-navigation__title">Categorie 1</h4>
              <NavLink activeClassName="is-active" to="/overzicht">
                Subcategorie 1
              </NavLink>
              <NavLink
                activeClassName="is-active"
                to="/overzicht/categorie-1/subcategorie-2"
              >
                Subcategorie 2
              </NavLink>
              <NavLink
                activeClassName="is-active"
                to="/overzicht/categorie-1/subcategorie-3"
              >
                Subcategorie 3
              </NavLink>
              <NavLink
                activeClassName="is-active"
                to="/overzicht/categorie-1/subcategorie-4"
              >
                Subcategorie 4
              </NavLink>
            </div>
            <div className="footer-navigation__list">
              <h4 className="footer-navigation__title">Categorie 2</h4>
              <NavLink
                activeClassName="is-active"
                to="/overzicht/categorie-2/subcategorie-1"
              >
                Subcategorie 1
              </NavLink>
              <NavLink
                activeClassName="is-active"
                to="/overzicht/categorie-2/subcategorie-2"
              >
                Subcategorie 2
              </NavLink>
              <NavLink
                activeClassName="is-active"
                to="/overzicht/categorie-2/subcategorie-3"
              >
                Subcategorie 3
              </NavLink>
              <NavLink
                activeClassName="is-active"
                to="/overzicht/categorie-2/subcategorie-4"
              >
                Subcategorie 4
              </NavLink>
            </div>
            <div className="footer-navigation__list">
              <h4 className="footer-navigation__title">Categorie 1</h4>
              <NavLink
                activeClassName="is-active"
                to="/overzicht/categorie-3/subcategorie-1"
              >
                Subcategorie 1
              </NavLink>
              <NavLink
                activeClassName="is-active"
                to="/overzicht/categorie-3/subcategorie-2"
              >
                Subcategorie 2
              </NavLink>
              <NavLink
                activeClassName="is-active"
                to="/overzicht/categorie-3/subcategorie-3"
              >
                Subcategorie 3
              </NavLink>
              <NavLink
                activeClassName="is-active"
                to="/overzicht/categorie-3/subcategorie-4"
              >
                Subcategorie 4
              </NavLink>
            </div>
          </div>
        </div>
      </footer>
    );
  }
}

export default FooterNavigation;
