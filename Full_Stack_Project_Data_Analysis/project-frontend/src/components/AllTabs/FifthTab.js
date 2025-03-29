import React from "react";
import {
    LineChart, 
    Line,
    Label,
    PieChart,
    Pie,
    Tooltip,
    BarChart,
    XAxis,
    YAxis,
    Legend,
    CartesianGrid,
    Bar
  } from "recharts";
const FifthTab = () => {
    const data2022 = [
        { name: "Jan", value: 2975 },
        { name: "Feb", value: 2604 },
        { name: "Mar", value: 3043 },
        { name: "Apr", value: 3089 },
        { name: "May", value: 3389 },
        { name: "Jun", value: 3630 }, 
        { name: "Jul", value: 3798 },
        { name: "Aug", value: 3677 },
        { name: "Sept", value: 3701 },
        { name: "Oct", value: 3251 }
        
       
      ];

      const crime2022 =[
        { name: "Larceny", value: 7516 },
        { name: "Larc From Auto", value: 3110 },
        { name: "Rape", value: 212 },
        { name: "Robb. - Commercial", value: 407 },
        { name: "Robbery", value: 2376 },
        { name: "Robb.-Carjacking", value: 533 }, 
        { name: "Homicide", value: 278 },
        { name: "Shooting", value: 603 },
        { name: "Comm. Assault", value: 7435 },
        { name: "Arson", value: 110 },
        { name: "Agg. Assault", value: 4623 },
        { name: "Auto Theft", value: 2837 },
        { name: "Buglary", value: 3115 }

    ];
  return (
    <div className="FirstTab">
        <div className="container">
  <h3>Baltimore Crime Data Per Month</h3>
  </div>
      <LineChart
          width={1500}
          height={400}
          data={data2022}
          
          margin={{
            top: 1,
            right: 2,
            left: 1,
            bottom:1,
          }}
        >
        

          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name"  />
          <Label value="Amount of crime committed in 2018" offset={10} position="insideBottom" />
          <YAxis  type="number" domain={[0, 4800]} orientation="right" width="10" label={{value: 'Number of crime reported', angle: -90, position: 'insideRight' , offset:-110}} />
          
          <Tooltip />
          <Legend />
          <Line isAnimationActive={false} type="monotone" dataKey="value" stroke="#8884d8" activeDot={{ r: 8 }} />

        </LineChart>
        <div className="container">
            <div>Baltimore Crime Data This Year</div>
        </div>
        <BarChart
          width={1500}
          height={500}
          data={crime2022}
          margin={{
            top: 5,
            right: 50,
            left: 80,
            bottom: 5,
          }}
          barSize={40}
        >
          <XAxis
            dataKey="name"
            scale="point"
            padding={{ left: 25, right: 10 }}
          />
          <YAxis />
          <Tooltip />
          <Legend />
          <CartesianGrid strokeDasharray="3 3" />
          <Bar dataKey="value" fill="turquoise"  />
        </BarChart>    </div>
  );
};
export default FifthTab;