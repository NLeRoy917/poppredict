import React from 'react';
import styles from '../styles/Button.module.css';

const Button = (props) => {
    return(
        <>
           <button
             {...props}
             className={styles.buttonLarge}
           >
               {props.children}
           </button>
        </>
    )
}

export default Button;