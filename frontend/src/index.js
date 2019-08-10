import React from 'react';
import { render } from 'react-dom';
import { createStore } from 'redux';
import { Provider } from 'react-redux';
import './index.css';
import reducer from './reducers';
import MancalaContainer from './containers/MancalaContainer';

const store = createStore(reducer);

render(
  <Provider store={store}>
    <MancalaContainer />
  </Provider>,
  document.getElementById('root')
);
