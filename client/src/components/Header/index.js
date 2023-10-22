import styles from './Header.module.scss';
import Topnav from './Topnav';
import Midnav from './Midnav';
import Bottomnav from './Bottomnav';
function Header() {
    return (
        <header className={styles.container}>
            <div className={styles.topnav}>
                <Topnav />
            </div>
            <div className={styles.midnav}>
                <Midnav />
            </div>
            <div className={styles.bottomnav}>
                <Bottomnav />
            </div>
        </header>
    );
}

export default Header;
