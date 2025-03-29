import React from 'react';
import './coviddata.css';
import Covid1 from '../AllTabs/covidFirstTab';
import Covid2 from '../AllTabs/covidSecondTab';
import Covid3 from '../AllTabs/covidThirdTab';
import Crime1 from '../AllTabs/FirstTab';
import Crime2 from '../AllTabs/SecondTab';
import Crime3 from '../AllTabs/ThirdTab';
import Tabs from "../TabComponent/Tabs";
import CovidTabs from "../TabComponent/covidTabs";
const CovidData = () => {
  return (
    <div>
      <div>
        <Tabs/>
        <CovidTabs/>
      </div>
    </div>
  );
};
  
export default CovidData;