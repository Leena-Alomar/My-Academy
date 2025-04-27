// IMPORTS
import "./styles.css";
import { useState } from 'react';
import Elements from "../../components/Elements/Elements";
import { Routes } from "react-router";
// import SchdeduleDetailPage from "../SchdeduleDetailPage";

// IMAGES


// COMPONENTS

export default function MainPage() {

    const mainEl = [
        {
          img: '',
          imgAlt: '',
          title: 'Schedule',
        },
        {
            img: '',
            imgAlt: '',
            title: 'Dashboard',
          },
      ];

    //   function getMainEl(day) {
    //     return mainEl.find((el) => el.img === img);
    //   }
      
    return (
    
    <div className="main-con">  
      <section className="main-section">
        {mainEl.map((el, index) => (
          <Elements key={index} el={el} />
        ))}
      </section>
      {/* <Routes>    
          <Route 
        path="/schdeule/:id" 
        element={<SchdeduleDetailPage getMain={getMainEl} />} 
      />
      </Routes> */}

     </div>

) 
  }
  