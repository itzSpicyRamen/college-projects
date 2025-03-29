import React, { useState } from "react";
import FirstTab from "../AllTabs/FirstTab.js";
import SecondTab from "../AllTabs/SecondTab.js";
import ThirdTab from "../AllTabs/ThirdTab.js";
import FourthTab from "../AllTabs/FourthTab.js";
import FifthTab from "../AllTabs/FifthTab.js";

import TabNavItem from "../V2/TabNavItem";
import TabContent from "../V2/TabContent";
 
const Tabs = () => {
  const [activeTab, setActiveTab] = useState("tab1");
 
  return (
    <div className="Tabs">
      <ul className="nav">
        <TabNavItem title="2018" id="tab1" activeTab={activeTab} setActiveTab={setActiveTab}/>
        <TabNavItem title="2019" id="tab2" activeTab={activeTab} setActiveTab={setActiveTab}/>
        <TabNavItem title="2020" id="tab3" activeTab={activeTab} setActiveTab={setActiveTab}/>
        <TabNavItem title="2021" id="tab4" activeTab={activeTab} setActiveTab={setActiveTab}/>
        <TabNavItem title="2022" id="tab5" activeTab={activeTab} setActiveTab={setActiveTab}/>
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
        <TabContent id="tab4" activeTab={activeTab}>
          <FourthTab/>
        </TabContent>
        <TabContent id="tab5" activeTab={activeTab}>
          <FifthTab/>
        </TabContent>
      </div>
    </div>
  );
};
 
export default Tabs;