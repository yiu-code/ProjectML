import React from 'react';

class NavBar extends React.Component {

    render() {
        return (
            <div>            
            <div>
            {/* <img src="https://d4kkpd69xt9l7.cloudfront.net/sys-master/root/h39/h95/9126618693662/razer-blade-15-gallery08.jpg"></img> */}
        </div>
      <header className="App-header">
        <div>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
      
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div class="navbar-nav">
          <a class="nav-item nav-link active" href="/">Home <span class="sr-only">(current)</span></a>
          <a class="nav-item nav-link active" href="./login">Login</a>
          <a class="nav-item nav-link active" href="./productpage">Products</a>
          <a class="nav-item nav-link active" href="/">Cart</a>
          {/* <a class="nav-item nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a> */}
    </div>
  </div>
</nav>

        </div>
        </header>
        </div>
        )
    }
};

export default NavBar;



