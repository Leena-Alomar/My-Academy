// IMPORTS
import "./App.css";
import { useState } from "react";
import { Route, Routes, Link, useLocation, Navigate } from 'react-router';


// COMPONENTS
import HomePage from "../HomePage";
import AboutPage from "/src/pages/AboutPage/index.jsx";
import SchdeuleDetailPage from "../SchdeduleDetailPage";
import SignupPage from "../SignupPage/SignupPage";
import Navbar from "../../components/Navbar/Navbar";
import MainPage from "../MainPage";



import { getUser } from '../../utilities/users-api';
function App () {
    const [user, setUser] = useState(getUser());


  return (
    <>
   
    <header>
      <div className={`header-logo-container`}>
        <Link to="/">
          {/* <img src={headerLogo} alt="The Cat Collector Logo" /> */}
        </Link>
      </div>
      <nav>
        <ul className=" nav1">
          <Navbar user={user} setUser={setUser} />
        </ul>
      </nav>
      </header>

        
        {user ?
            <Routes>
                <Route path="/*" element={<Navigate to="/home" />} />
                <Route path="/about" element={<AboutPage />} />
                <Route path="/schedule" element={<SchdeuleDetailPage />} />
                <Route path="/Main" element={<MainPage />} />
            </Routes>
          :
          <Routes>
            <Route path="/signup" element={<SignupPage user={user} setUser={setUser}  />}/>
            <Route path="/home" element={<HomePage  user={user} setUser={setUser}/>} />
            <Route path="/*" element={<Navigate to="/home" />} />
          </Routes>
        }
                
    </>
  )
}

export default App

