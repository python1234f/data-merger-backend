import React from 'react';
import { createRoot } from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

// Create a root container
const root = createRoot(document.getElementById('root'));

// Render the App into the root container
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

reportWebVitals();