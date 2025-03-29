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
const ThirdTab = () => {
    const data2020 = [
        { name: "Jan", value: 3368 },
        { name: "Feb", value: 3098 },
        { name: "Mar", value: 3093 },
        { name: "Apr", value: 2543 },
        { name: "May", value: 2918 },
        { name: "Jun", value: 3141 }, 
        { name: "Jul", value: 3179 },
        { name: "Aug", value: 3065 },
        { name: "Sept", value: 3125 },
        { name: "Oct", value: 3189 },
        { name: "Nov", value: 2856 },
        { name: "Dec", value: 2713 }
       
      ];

      const crime2020 =[
        { name: "Larceny", value: 7668 },
        { name: "Larc. From Auto", value: 3661 },
        { name: "Rape", value: 295 },
        { name: "Robb. - Commercial", value: 418 },
        { name: "Robbery", value: 2651 },
        { name: "Robb.-Carjacking", value: 518 }, 
        { name: "Homicide", value: 335 },
        { name: "Shooting", value: 721 },
        { name: "Comm. Assault", value: 7497 },
        { name: "Arson", value: 106 },
        { name: "Agg. Assault", value: 5350 },
        { name: "Auto Theft", value: 3006 },
        { name: "Buglary", value: 4055 }

    ];
  return (
    <div className="FirstTab">
        <div className="container">
  <h3 style={{color: "White"}}>Baltimore Crime Data Per Month</h3>
  </div>
      <LineChart
          width={1500}
          height={400}
          data={data2020}
          
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
          <Line isAnimationActive={false}  type="monotone" dataKey="value" stroke="#8884d8" activeDot={{ r: 8 }} />

        </LineChart>
        <div className="container">
            <h3 style={{color: "White"}}>Baltimore Crime Data This Year</h3>
        </div>
        <BarChart
          width={1500}
          height={500}
          data={crime2020}
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
        </BarChart>
    </div>
  );
};
export default ThirdTab;