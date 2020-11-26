import React from 'react';
import { useHistory } from "react-router-dom";
import styles from '../styles/Home.module.css';

import Button from './Button';

const Home = () => {
    let history = useHistory();
    const goQueryData = () => {
        history.push('/query-data')
    }
    return(
        <>
         <div className={styles.landing}>
         <h1>Pop-Predict Playground</h1>
          <div className={styles.buttonWrapper}>
              <Button onClick={() => goQueryData()}>
                Query Data
              </Button>
            <Button
              style={{background: 'white', color: '#ff4154', border: 'white 1px solid'}}
            >
                Run Script
            </Button>
          </div>
         </div>
        </>
    )
}

export default Home;