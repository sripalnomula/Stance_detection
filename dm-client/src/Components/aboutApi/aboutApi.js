import styles from './aboutApi.module.css';
import { useEffect } from 'react';
export default function AboutApi(){
    const SERVER_URL = process.env.REACT_APP_SERVER_URL;
    useEffect(()=>{
        document.title="About API"
    },[])
    const requestBodyFormat = `{
        "title":"article title",
        "body":"article body"
    }`
    return (
        <div className="container">
            <h1 style={{ margin:0}}>API Endpoints</h1>
            <h3>API is hosted at: {SERVER_URL}</h3>
            <h3>Find the JSON format of request body for both endpoints in code snippet show below</h3>
            <pre><code>
            {requestBodyFormat}    
            </code></pre>
            <div className={styles.endpointContainer}>
                <h3>Endpoints</h3>
                <ul>
                    <li>
                        <div className={styles.endpoint}>
                            <h2>/stance-detection</h2>
                            <p>Using this endpoint, an user can determine the stance between title and body of an article. This endpoint follows a HTTP Post method.</p>
                            <hr/>
                        </div>
                    </li>
                    <li>
                        <div className={styles.endpoint}>
                            <h2>/fake-news-detection</h2>
                            <p>Using this endpoint, an user can determine the truthness of an article, provided the title and body. This endpoint follows a HTTP Post method.</p>
                            <hr/>
                        </div>
                    </li>
                </ul>
                
                
            </div>
        </div>
        
    )
}