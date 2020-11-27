import React from 'react';
import styles from '../styles/Query.module.css';

const Query = (props) => {
    return(
        <>
          <textarea rows="10" cols="50" className={styles.queryInput}>

          </textarea>
        </>
    )
}

export default Query;