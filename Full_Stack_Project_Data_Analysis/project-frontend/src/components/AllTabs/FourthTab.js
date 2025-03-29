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
const FourthTab = () => {
    const data2021 = [
        { name: "Jan", value: 2551 },
        { name: "Feb", value: 2174 },
        { name: "Mar", value: 2669 },
        { name: "Apr", value: 2646 },
        { name: "May", value: 3271 },
        { name: "Jun", value: 3392 }, 
        { name: "Jul", value: 3358 },
        { name: "Aug", value: 3391 },
        { name: "Sept", value: 3553 },
        { name: "Oct", value: 3549 },
        { name: "Nov", value: 3318 },
        { name: "Dec", value: 3533 }
       
      ];

      const crime2021 =[
        { name: "Larceny", value: 7225 },
        { name: "Larc. From Auto", value: 4581 },
        { name: "Rape", value: 282 },
        { name: "Robb. - Commercial", value: 324 },
        { name: "Robbery", value: 2777 },
        { name: "Robb.-Carjacking", value: 582 }, 
        { name: "Homicide", value: 335 },
        { name: "Shooting", value: 728 },
        { name: "Comm. Assault", value: 8239 },
        { name: "Arson", value: 139 },
        { name: "Agg. Assault", value: 5537 },
        { name: "Auto Theft", value: 3186 },
        { name: "Buglary", value: 3458 }

    ];
  return (
    <div className="FirstTab">
        <div className="container">
  <h3>Baltimore Crime Data Per Month</h3>
  </div>
      <LineChart
          width={1500}
          height={400}
          data={data2021}
          
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
            <div>Baltimore Crime Data This Year</div>
        </div>
        <BarChart
          width={1500}
          height={500}
          data={crime2021}
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
export default FourthTab;