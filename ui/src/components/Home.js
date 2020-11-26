import React from 'react';
import styles from '../styles/Home.module.css';

import Button from './Button';

const Home = () => {
    return(
        <>
         <div className={styles.landing}>
         <h1>Pop-Predict Playground</h1>
          <div className={styles.buttonWrapper}>
            <Button>
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