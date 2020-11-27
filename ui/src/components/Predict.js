import React from 'react';
import styles from '../styles/Predict.module.css'
import Button from './Button';

import Query from './Query';

const Predict = (props) => {
    return(
        <>
          <div className={styles.layout}>
          <h1>Predict Popularity Scores</h1>
           <div className={styles.buttonWrapper}>
            <button className={styles.generateButton}>
              Random
            </button>
            <button className={styles.generateButton}>
              Test on Song
            </button>
           </div>
          </div>
        </>
    )
}

export default Predict;