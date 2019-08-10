import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';

const useStyles = makeStyles(theme => ({
  button: {
    margin: theme.spacing(1),
  },
  input: {
    display: 'none',
  },
}));

export default function SideHole() {
  const classes = useStyles();

  return (
    <div>
      <Button variant="contained" className={classes.button}>
          SH
      </Button>
    </div>
  );
}