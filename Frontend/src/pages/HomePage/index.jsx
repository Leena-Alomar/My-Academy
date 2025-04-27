// IMPORTS
import "./styles.css";
import { useState } from "react";
import { useNavigate } from "react-router";
// IMAGES
import study from "../../assets/images/icon.png";
import studyTwo from "../../assets/images/icon3.png";
// APIs
import * as usersAPI from "../../utilities/users-api";


export default function HomePage({ user, setUser }) {
  const initialState = { username: "", password: "" }
  const [formData, setFormData] = useState(initialState)
  const navigate = useNavigate()

  function handleChange(evt) {
    setFormData({ ...formData, [evt.target.name]: evt.target.value})
  }

  async function handleLogin(evt) {
    try {
      evt.preventDefault();
      const loggedInUser = await usersAPI.login(formData);
      setUser(loggedInUser);
      navigate("/Main");
    } catch (err) {
      setUser(null);
    }
}

  return (<>
    <section className="logo-container">
      <div className="home-container">
        
      </div>
      {/* <img src={logoType} alt="Text reads: Cat Collector" /> */}
    </section>
    {!user &&
      <section>
       <img className="study2" src={studyTwo} alt="study2 icon" />
        <form onSubmit={handleLogin} className="form-container-login">
          <h1 className="login">User Login</h1>
          <p>
            <label htmlFor="id_username"></label>
            <input placeholder="User Name" className="in" value={formData.username} type="text" name="username" maxLength="150" required id="id_username" onChange={handleChange}/>
          </p>
          <p>
            <label htmlFor="id_password"></label>
            <input placeholder="Password" className="in" value={formData.password} type="password" name="password" required id="id_password" onChange={handleChange} />
          </p>
          <button type="submit" className="btn1">Login</button>
        </form>
        <img className="study" src={study} alt="study icon" />
       
      </section>
    }
  </>)
}