import React from 'react';
import {
    BrowserRouter as Router,
    Route,
    Switch
  } from "react-router-dom";
import Home from './components/Home';
import QueryData from './components/QueryData';
import './styles/App.css';

const App = () => {
    return (
        <div>
          <Router>
            <Switch>
              <Route path="/query-data/" component={QueryData}></Route>
              <Route path="/" component={Home}></Route>
            </Switch>
          </Router>
        </div>
    );
}
export default App;