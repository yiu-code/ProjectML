import React, { Component } from "react";
import { Link } from "react-router-dom";

class Pagination extends Component {
  constructor(props) {
    super(props);
    this.state = {
      pages: 1,
      showPages: []
    };
  }
  render() {
    const { perPage, totalPages, currentPage } = this.props;
    const { pages, showPages } = this.state;
    return (
      <div className="pagination">
        {Array.apply(0, Array(totalPages)).map((item, i) => {
          let page = i + 1;
          let link = `/overzicht/pagina/${page}`;
          if (i === 0) {
            link = "/overzicht";
          }
          return (
            <Link
              to={link}
              className={`pagination-item${
                currentPage === page ? " pagination-item--is-active" : ""
              }`}
              key={i}
            >
              {page}
            </Link>
          );
        })}
      </div>
    );
  }
}

export default Pagination;
