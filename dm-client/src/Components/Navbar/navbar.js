import { Link, useMatch, useResolvedPath } from "react-router-dom"
import styles from './navbar.module.css';
import {FaGithubSquare,FaRegNewspaper} from 'react-icons/fa';
export default function Navbar() {
  return (
    <nav className={styles.nav}>
        <Link to="/" style={{fontSize:"1.5rem"}}>
          <FaRegNewspaper style={{marginRight:"3px"}} /> <b>Stance Detection</b>
        </Link>
        <span className={styles.vertical}></span>
        <ul>
          {/* <CustomLink to="/pricing">Pricing</CustomLink> */}
          <CustomLink to="/about-api">API</CustomLink>
        </ul>
        <div >
          <a href="https://github.com/avinash-rdy2903/dm-client" target="_blank" ><FaGithubSquare className={styles.socials}></FaGithubSquare></a>
        </div>      
    </nav>
  )
}

function CustomLink({ to, children, ...props }) {
  const resolvedPath = useResolvedPath(to)
  const isActive = useMatch({ path: resolvedPath.pathname, end: true })

  return (
    <li className={isActive ? styles.active : ""}>
      <Link to={to} {...props}>
        {children}
      </Link>
    </li>
  )
}