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
const FirstTab = () => {
    const data2018 = [
        { name: "Jan", value: 3761 },
        { name: "Feb", value: 3122 },
        { name: "Mar", value: 3488 },
        { name: "Apr", value: 3788 },
        { name: "May", value: 4211 },
        { name: "Jun", value: 4074 }, 
        { name: "Jul", value: 4315 },
        { name: "Aug", value: 4545 },
        { name: "Sept", value: 4214 },
        { name: "Oct", value: 4577 },
        { name: "Nov", value: 4182 },
        { name: "Dec", value: 4322 }
       
      ];
    const crime2018 =[
        { name: "Larceny", value: 10711 },
        { name: "Larc. From Auto", value: 6376 },
        { name: "Rape", value: 365 },
        { name: "Robb. - Commercial", value: 722 },
        { name: "Robbery", value: 4313 },
        { name: "Robb.-Carjacking", value: 483 }, 
        { name: "Homicide", value: 309 },
        { name: "Shooting", value: 677 },
        { name: "Comm. Assault", value: 8446 },
        { name: "Arson", value: 127 },
        { name: "Agg. Assault", value: 5632 },
        { name: "Auto Theft", value: 4217 },
        { name: "Buglary", value: 6218 }

    ];
  return (
    <div className="FirstTab">
        <div className="container">
  <h3 style={{color: "White"}}>Baltimore Crime Data Per Month</h3>
  </div>
      <LineChart
          width={1500}
          height={400}
          data={data2018}
          
          margin={{
            top: 1,
            right: 2,
            left: 1,
            bottom:1,
          }}
        >
        

          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" />
          <Label value="Amount of crime committed in 2018" offset={10} position="insideBottom" />
          <YAxis type="number" domain={[0, 4800]} orientation="right" width="10" label={{value: 'Number of crime reported', angle: -90, position: 'insideRight' , offset:-110}} />
          
          <Tooltip />
          <Legend />
          <Line isAnimationActive={false} type="monotone" dataKey="value" stroke="#8884d8" activeDot={{ r: 8 }} />

        </LineChart>
        <div className="container">
            <h3 style={{color: "White"}}>Baltimore Crime Data This Year</h3>
        </div>
        <BarChart
          width={1500}
          height={500}
          data={crime2018}
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
          <Bar dataKey="value" fill="turquoise" />
        </BarChart>
    </div>
  );
};
export default FirstTab;