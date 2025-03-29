import React, { useState } from "react";
import FirstTab from "../AllTabs/covidFirstTab.js";
import SecondTab from "../AllTabs/covidSecondTab.js";
import ThirdTab from "../AllTabs/covidThirdTab.js";

import TabNavItem from "../V2/TabNavItem";
import TabContent from "../V2/TabContent";

const CovidTabs = () => {
    const [activeTab, setActiveTab] = useState("tab1");
   
    return (
      <div className="Tabs">
        <ul className="nav">
          <TabNavItem title="2020" id="tab1" activeTab={activeTab} setActiveTab={setActiveTab}/>
          <TabNavItem title="2021" id="tab2" activeTab={activeTab} setActiveTab={setActiveTab}/>
          <TabNavItem title="2022" id="tab3" activeTab={activeTab} setActiveTab={setActiveTab}/>
        </ul>
   
        <div className="outlet">
         
          <TabContent id="tab1" activeTab={activeTab}>
            <FirstTab/>
          </TabContent>
          <TabContent id="tab2" activeTab={activeTab}>
            <SecondTab/>
          </TabContent>
          <TabContent id="tab3" activeTab={activeTab}>
            <ThirdTab/>
          </TabContent>
        </div>
      </div>
    );
  };
   
  export default CovidTabs;