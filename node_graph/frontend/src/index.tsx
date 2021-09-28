
import React from 'react';
import ReactDOM from 'react-dom';
import BodyWidget from './components/BodyWidget';
import "./index.css";
// Tells React to render the App component on the DOM element whose id is "root"
// You never did that, and thats why there's no child on the "root" div on the DevTools
ReactDOM.render(<BodyWidget />, document.getElementById('root'));