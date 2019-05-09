import React, { Component } from "react";

// components
import ProductGridItem from "../../components/ProductGridItem";

class ProductGrid extends Component {
  render() {
    const { items } = this.props;
    return (
      <section className="product-grid">
        {items.map((item, i) => {
          return <ProductGridItem item={item} key={i} />;
        })}
      </section>
    );
  }
}

export default ProductGrid;
