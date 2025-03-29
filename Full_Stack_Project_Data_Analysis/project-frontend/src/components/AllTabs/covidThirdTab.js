import React from "react";
import {
    LineChart, 
    Line,
    Label,
    LabelList,
    PieChart,
    Pie,
    Tooltip,
    BarChart,
    XAxis,
    YAxis,
    Legend,
    CartesianGrid,
    Sector,
    Cell,
    Bar
  } from "recharts";
  
  
 const CustomTooltip = ({ active, payload, label }) => {
    if (active) {
       return (
       <div
          className="custom-tooltip"
          style={{
             backgroundColor: "#1111",
             padding: "5px",
             border: "1px solid #cccc"
          }}
       >
          <label>{`${payload[0].name} : ${payload[0].value}`}</label>
       </div>
    );
 }
 return null;
};
const FirstTab = () => {
    const COLORS = [ '#00949F', '#0FBA08', '#FF8042','#E1A811', '#6C11E1', '#2D9603','#0088FE', '#F168A6','#108E77', '#A8D1AB', '#900C3F', '#F67286'];

    const cases2022 = [
        { name: "Jan", value: 55722 },
        { name: "Feb", value: 4831 }, 
        { name: "Mar", value: 2140 },
        { name: "Apr", value: 4643 },
        { name: "May", value: 14092 },
        { name: "Jun", value: 8867 }, 
        { name: "Jul", value: 9632 },
        { name: "Aug", value: 8775 },
        { name: "Sept", value: 5858 },
        { name: "Oct", value: 4334 },
        { name: "Nov", value: 1821 },
       
      ];
      const deaths2022= [
        { name: "Jan", value: 489 },
        { name: "Feb", value: 233 }, 
        { name: "Mar", value: 76 },
        { name: "Apr", value: 25 },
        { name: "May", value: 45 },
        { name: "Jun", value: 56 }, 
        { name: "Jul", value: 58 },
        { name: "Aug", value: 49 },
        { name: "Sept", value: 41 },
        { name: "Oct", value: 40 },
        { name: "Nov", value: 12 },
       
      ];
      
    
  return (
    <div className="FirstTab">
        <div className="container">
            <h3 style={{color: "White"}}>Baltimore Covid Cases Per Month</h3>
        </div>
    <div class='parent'>
        <div class='child'>
            <PieChart width={400} height={410}>
                <Pie data={cases2022} color="#000000" dataKey="value" nameKey="name" cx="50%" cy="50%" outerRadius={140} fill="#8884d8">
                {deaths2022.map((entry, index) => (
                    <Cell
                    key={`cell-${index}`}
                    fill={COLORS[index % COLORS.length]}
                    />
                ))}
                </Pie>
                <Tooltip content={<CustomTooltip />} />
                <Legend />
            </PieChart>
           
        </div>
        <div class='child'>
        <BarChart width={800}  height={400} data={cases2022} margin={{top: 5,right: 5,left: 40, bottom: 5,}}barSize={40}>
          <XAxis dataKey="name" scale="point" padding={{ left: 25, right: 10 }}/>
          <YAxis />
          <Tooltip />
          <Legend />
          <CartesianGrid strokeDasharray="3 3" />
          <Bar dataKey="value" fill="turquoise"  />
        </BarChart>
        </div>    
    </div> 
    <div className="container">
        <h3 style={{color: "White"}}>Baltimore Covid Deaths Per Month</h3>
    </div>
    <div class='parent'>
        <div class='child'>
            <PieChart width={400} height={410}>
                <Pie data={deaths2022} color="#000000" dataKey="value" nameKey="name" cx="50%" cy="50%" outerRadius={140} fill="#8884d8">
                {deaths2022.map((entry, index) => (
                    <Cell
                    key={`cell-${index}`}
                    fill={COLORS[index % COLORS.length]}
                    />
                ))}
                </Pie>
                <Tooltip content={<CustomTooltip />} />
                <Legend />
            </PieChart>
        </div>
        <div class='child'>
        <BarChart width={800}  height={400} data={deaths2022} margin={{top: 5,right: 5,left: 40, bottom: 5,}}barSize={40}>
          <XAxis dataKey="name" scale="point" padding={{ left: 25, right: 10 }}/>
          <YAxis />
          <Tooltip />
          <Legend />
          <CartesianGrid strokeDasharray="3 3" />
          <Bar dataKey="value" fill="turquoise"  />
        </BarChart>
        </div>
    </div>
    </div>
  );
};
export default FirstTab;