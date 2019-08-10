import React, { Component } from 'react';
import Button from '@material-ui/core/Button';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import * as actions from '../actions';

class PlayerHole extends Component {
  render(){
    const { numStone, actions } = this.props;
    return (
      <div>
        <Button variant="contained" onClick={() => actions.onHoleClick()}>
            {numStone.phValue1}
        </Button>
        <Button variant="contained" onClick={() => actions.onHoleClick()}>
            {numStone.phValue2}
        </Button>
        <Button variant="contained" onClick={() => actions.onHoleClick()}>
            {numStone.phValue3}
        </Button>
      </div>
    );
  }
}

const mapStateToProps = (state) => ({
  numStone: state.numStone,
});

function mapDispatchToProps(dispatch) {
  return {
    actions: bindActionCreators(actions, dispatch),
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(PlayerHole);
