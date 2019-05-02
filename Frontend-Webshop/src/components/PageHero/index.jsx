import React, { Component } from 'react';

// https://images.unsplash.com/photo-1504392308976-1668b20126a4?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=98cef3ebd4d78106480ef3229c7071d1&auto=format&fit=crop&w=2500&q=100
// https://images.unsplash.com/photo-1537771555080-dd75c6af3dce?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=d85fde3f569f12cd1046da2beb039d1e&auto=format&fit=crop&w=1920&q=100
//https://images.unsplash.com/photo-1537182534312-f945134cce34?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=3e15098b0f1917ea25a41c7908a227a5&auto=format&fit=crop&w=1920&q=100

class PageHero extends Component {
  render() {
    const { image, type, intro, title, description } = this.props;
    return (
      <section
        className={`page-hero${type ? ` page-hero--${type}` : ''}`}
        style={{
          backgroundImage: `url(${image})`
        }}>
        {intro && (
          <div className="wrapper">
            <h1 className="page-hero__title">{title}</h1>
            {description && (
              <p className="page-hero__description">{description}</p>
            )}
          </div>
        )}
      </section>
    );
  }
}

export default PageHero;
