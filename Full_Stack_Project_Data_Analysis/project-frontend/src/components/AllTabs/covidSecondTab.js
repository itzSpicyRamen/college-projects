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

    const cases2021 = [
        { name: "Jan", value: 15098 },
        { name: "Feb", value: 6000 },
        { name: "Mar", value: 9193 },
        { name: "Apr", value: 13891 },
        { name: "May", value: 4103 },
        { name: "Jun", value: 610 }, 
        { name: "Jul", value: 1296 },
        { name: "Aug", value: 5541 },
        { name: "Sept", value: 6651 },
        { name: "Oct", value: 6045 },
        { name: "Nov", value: 5968 },
        { name: "Dec", value: 35890 }
       
      ];
      const deaths2021= [

        { name: "Jan", value: 327},
        { name: "Feb", value: 200 },
        { name: "Mar", value:  139 },
        { name: "Apr", value: 184 },
        { name: "May", value: 378 },
        { name: "Jun", value: 50 }, 
        { name: "Jul", value: 26 },
        { name: "Aug", value: 32 },
        { name: "Sept", value: 93 },
        { name: "Oct", value: 105 },
        { name: "Nov", value: 87 },
        { name: "Dec", value: 133 }
       
      ];
      
    
  return (
    <div className="FirstTab">
        <div className="container">
            <h3 style={{color: "White"}}>Baltimore Covid Cases Per Month</h3>
        </div>
    <div class='parent'>
        <div class='child'>
            <PieChart width={400} height={410}>
                <Pie data={cases2021} color="#000000" dataKey="value" nameKey="name" cx="50%" cy="50%" outerRadius={140} fill="#8884d8">
                {deaths2021.map((entry, index) => (
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
        <BarChart width={800}  height={400} data={cases2021} margin={{top: 5,right: 5,left: 40, bottom: 5,}}barSize={40}>
          <XAxis dataKey="name" scale="point" padding={{ left: 25, right: 10 }}/>
          <YAxis />
          <Tooltip />
          <Legend />
          <CartesianGrid strokeDasharray="3 3" />
          <Bar dataKey="value" fill="turquoise" />
        </BarChart>
        </div>    
    </div> 
    <div className="container">
        <h3 style={{color: "White"}}>Baltimore Covid Deaths Per Month</h3>
    </div>
    <div class='parent'>
        <div class='child'>
            <PieChart width={400} height={410}>
                <Pie data={deaths2021} color="#000000" dataKey="value" nameKey="name" cx="50%" cy="50%" outerRadius={140} fill="#8884d8">
                {deaths2021.map((entry, index) => (
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
        <BarChart width={800}  height={400} data={deaths2021} margin={{top: 5,right: 5,left: 40, bottom: 5,}}barSize={40}>
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