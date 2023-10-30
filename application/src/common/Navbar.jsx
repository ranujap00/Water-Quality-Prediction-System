import { useNavigate } from "react-router-dom";
import "./navbar.css";

function Navbar() {
  const navigate = useNavigate();

  return (
    <>
      <nav className="navbar navbar-expand-lg">
        <div className="container-fluid">
          <div className="collapse navbar-collapse" id="navbarSupportedContent">
            <ul className="navbar-nav me-auto mb-2 mb-lg-0">
              <li className="nav-item">
                <button
                  className="btn btn-link"
                  onClick={() => {
                    navigate("/");
                  }}
                >
                  Home
                </button>
              </li>
              <li className="nav-item">
                <button
                  className="btn btn-link"
                  onClick={() => {
                    navigate("/waterPotability");
                  }}
                >
                  Test Water Potability
                </button>
              </li>

              <li className="nav-item heading">
                <h2>Water Quality Testing Application</h2>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </>
  );
}

export default Navbar;
