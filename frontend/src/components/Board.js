import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import PlayerHole from '../components/PlayerHole';
import SideHole from '../components/SideHole';

const useStyles = makeStyles(theme => ({
  board: {
    display: "flex",
  },
}));

export default function Board() {
  const classes = useStyles();

  return (
    <div className={classes.board}>
      <SideHole />
      <div >
        <PlayerHole />
        <PlayerHole />  
      </div>
      <SideHole />
    </div>
  );
}