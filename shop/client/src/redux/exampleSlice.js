import { createSlice } from '@reduxjs/toolkit'

export const exampleSlice = createSlice({
  name: 'example',
  initialState: {
    value: 0
  },
  reducers: {
    handleExample: (state) => {
        state.value = state.value;
    },
  }
})

// Action creators are generated for each case reducer function
export const { handleExample } = exampleSlice.actions

export default exampleSlice.reducer