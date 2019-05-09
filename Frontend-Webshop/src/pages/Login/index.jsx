import React, { Component } from "react";
import { Link } from "react-router-dom";

// layout
import LayoutAccount from "../../layout/Account";

// components
import SimpleHeading from "../../components/SimpleHeading";
import LoginForm from "../../components/LoginForm";

class Login extends Component {
  constructor(props) {
    super(props);
    this.state = {
      width: null
    };
  }

  render() {
    return (
      <React.Fragment>
        <LayoutAccount className="login" simple>
          <div className="wrapper">
            <SimpleHeading
              title="Inloggen"
              description="Lorem ipsum dolor sit amet, consectetur adipiscing"
            />
            <LoginForm />
          </div>
        </LayoutAccount>
      </React.Fragment>
    );
  }
}

export default Login;
