import styles from './Main.module.scss';
import clsx from 'clsx';
import Header from '../../components/Header';
import Body from '../../components/Body';
import Footer from '../../components/Footer';
function Main() {
    return (
        <div className={styles.container}>
            <div className={styles.header}>
                <Header />
            </div>
            <div className={clsx(styles.body, 'grid', 'wide')}>
                <Body />
            </div>
            <div className={styles.footer}>
                <Footer />
            </div>
        </div>
    );
}

export default Main;
