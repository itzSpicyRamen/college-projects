import React from 'react';
import MapView from './MapView';

var perf = require('./heatmap.html');

class CrimeData extends React.Component {
  render(){
    return(
      <iframe src={perf}></iframe>
    );
  }
}

export default CrimeData;