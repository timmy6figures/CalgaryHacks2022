import { ReactComponent as Mango } from "../../icons/mango_icon.svg";
import { ReactComponent as Hamburger } from "../../icons/hamburger-menu.svg";
import { ReactComponent as Close } from "../../icons/close.svg";
import MenuList from "./MenuList";
import { useState } from "react";

const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  return (
    <header className="header">
      <nav className="header-navbar">
        {/* Title wrapper */}
        <div className="header-title-wrapper">
          <section className="header-title">
            <div className="mango-icon">
              <Mango />
            </div>

            <h1>Mango Health</h1>
          </section>

          <section className="header-hamburger">
            {isMenuOpen ? (
              <Close
                className="close-button"
                onClick={() => {
                  setIsMenuOpen(!isMenuOpen);
                }}
              />
            ) : (
              <Hamburger
                className="hamburger-button"
                onClick={() => {
                  setIsMenuOpen(!isMenuOpen);
                }}
              />
            )}
          </section>
        </div>

        {/* Expanded menu items */}
        <MenuList isOpen={isMenuOpen} />
      </nav>
    </header>
  );
};

export default Header;
