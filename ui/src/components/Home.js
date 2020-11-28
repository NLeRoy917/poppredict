import React from 'react';
import { useHistory } from "react-router-dom";
import styles from '../styles/Home.module.css';

import Button from './Button';

const Home = () => {
    let history = useHistory();
    const goPredict = () => {
        history.push('/predict')
    }
    const goView = () => {
      history.push('/view-data')
  }
    return(
        <>
         <div className={styles.landing}>
         <h1>Pop-Predict Playground</h1>
          <div className={styles.buttonWrapper}>
              <Button onClick={() => goPredict()}>
                Predict popularity
              </Button>
            <Button
              style={{background: 'white', color: '#ff4154', border: 'white 1px solid'}}
              onClick={() => goView()}
            >
                View Data
            </Button>
          </div>
         </div>
        </>
    )
}

export default Home;