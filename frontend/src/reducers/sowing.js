import * as actionTypes from '../utils/actionTypes';

const initialAppState = {
    phValue1: 3,
    phValue2: 3,
    phValue3: 3,
};

const numStone = (state = initialAppState, action) => {
  if (action.type === actionTypes.INPUT_NUMBER) {
    console.log("performed Onclick function")
    return {
      ...state,
      phValue1: state.phValue1 + 1,
    };
  } 
  else {
    return state;
  }
};

export default numStone;

