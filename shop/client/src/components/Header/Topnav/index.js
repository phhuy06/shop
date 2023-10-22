import styles from './Topnav.module.scss';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSearch } from '@fortawesome/free-solid-svg-icons';
function Topnav() {
    return (
        <div className={styles.container}>
            <div className={styles.wraper}>
                <div className={styles.user}>
                    <p>Đăng nhập</p>
                </div>
                <div className={styles.contact}>
                    <p>Gọi ngay: 0989165022 - Hỗ trợ 7 ngày trong tuần</p>
                </div>
                <div className={styles.search}>
                    <input type="text" placeholder="Search..."></input>
                    <div className={styles.icon}>
                        <FontAwesomeIcon icon={faSearch} />
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Topnav;
