
import React from 'react';
import ReactDOM from 'react-dom';
import BodyWidget from './components/BodyWidget';
import "./index.css";
import {
	Streamlit,
	StreamlitComponentBase,
	withStreamlitConnection,
  } from "streamlit-component-lib"

ReactDOM.render(
    <React.StrictMode>
        {/* <div style={{ width: "1000px", height: "1000px", color: "red"}}>Hi</div> */}
        <BodyWidget />
    </React.StrictMode>
, document.getElementById('root'));

