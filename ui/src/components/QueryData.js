import React from 'react';
import styles from '../styles/QueryData.module.css'

import Query from './Query';

const QueryData = (props) => {
    return(
        <>
          <div className={styles.layout}>
            <Query />
          </div>
        </>
    )
}

export default QueryData;