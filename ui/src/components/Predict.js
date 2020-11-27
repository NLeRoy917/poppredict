import React from 'react';
import styles from '../styles/Predict.module.css'
import Button from './Button';

import Query from './Query';

const Predict = (props) => {
    return(
        <>
          <div className={styles.layout}>
            <button className={styles.generateButton}>
              Random
            </button>
            
          </div>
        </>
    )
}

export default Predict;