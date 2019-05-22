import React, {Component} from 'react';

class Footer extends React.Component {

    
    render() {
        return (
        <div>
        <footer className="footer">
        <div className="wrapper">
          <span className="footer__copyright">
            &copy; {new Date().getFullYear()} Dept inc
          </span>
          <ul className="footer__navigation">
            <li>
                Algemene voorwaarden
            </li>
            <li>
                Privacy policy
            </li>
          </ul>
        </div>
      </footer>
            </div>
            
        )
    }
};

export default Footer;





