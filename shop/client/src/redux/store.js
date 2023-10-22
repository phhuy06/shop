import { configureStore } from '@reduxjs/toolkit';
import exampleSlice from './exampleSlice';
export default configureStore({
    reducer: {
        example: exampleSlice
    },
});


//useSelector-> get value
//useDispatch-> set value