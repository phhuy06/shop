import styles from './App.module.scss';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Main from './pages/Main';
function App() {
    return (
        <BrowserRouter>
            <div className={styles.container}>
                <Routes>
                    <Route path="/" element={<Main />}></Route>
                </Routes>
            </div>
        </BrowserRouter>
    );
}

export default App;
