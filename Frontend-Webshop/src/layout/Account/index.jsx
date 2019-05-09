import React, { Component } from "react";
import Header from "../../components/Header";
import Footer from "../../components/Footer";

class LayoutAccount extends Component {
  render() {
    const { children, simple, className } = this.props;
    return (
      <div {...this.props} className={className}>
        <Header simple />
        <main className={`${simple ? "main--simple" : ""}`}>{children}</main>
        <Footer />
      </div>
    );
  }
}

export default LayoutAccount;
