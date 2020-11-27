import React from 'react';
import styles from '../styles/Button.module.css';

const Button = (props) => {
    return(
        <>
           <button
             {...props}
             className={styles.buttonMedium}
           >
               {props.children}
           </button>
        </>
    )
}

export default Button;