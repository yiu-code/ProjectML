import React, { Component } from "react";
import { Link } from "react-router-dom";

class Header extends Component {
  render() {
    const { children } = this.props;
    return (
      <button onClick={this.addToCart} className="button">
        {children}
      </button>
    );
  }
}

export default Header;
