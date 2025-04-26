import * as React from "react";
import * as ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router";
import { createRoot } from "react-dom/client";
import { StrictMode } from "react";
import App from './pages/App/App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </StrictMode>,
)