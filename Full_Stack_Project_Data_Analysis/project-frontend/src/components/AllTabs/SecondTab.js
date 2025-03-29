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
const SecondTab = () => {
    const data2019 = [
        { name: "Jan", value: 3731 },
        { name: "Feb", value: 3142 },
        { name: "Mar", value: 3478 },
        { name: "Apr", value: 3684 },
        { name: "May", value: 4154 },
        { name: "Jun", value: 4198 }, 
        { name: "Jul", value: 4546 },
        { name: "Aug", value: 4485 },
        { name: "Sept", value: 4241 },
        { name: "Oct", value: 3924 },
        { name: "Nov", value: 3558 },
        { name: "Dec", value: 3462 }
       
      ];
      const crime2019 =[
        { name: "Larceny", value: 10770 },
        { name: "Larc. From Auto", value: 5778 },
        { name: "Rape", value: 316 },
        { name: "Robb. - Commercial", value: 585 },
        { name: "Robbery", value: 3991 },
        { name: "Robb.-Carjacking", value: 583 }, 
        { name: "Homicide", value: 348 },
        { name: "Shooting", value: 766 },
        { name: "Comm. Assault", value: 8415 },
        { name: "Arson", value: 115 },
        { name: "Agg. Assault", value: 5735 },
        { name: "Auto Theft", value: 3770 },
        { name: "Buglary", value: 5427 }

    ];
  return (
    <div className="FirstTab">
        <div className="container">
  <h3 style={{color: "White"}}>Baltimore Crime Data Per Month</h3>
  </div>
      <LineChart
          width={1500}
          height={400}
          data={data2019}
          
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
          data={crime2019}
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
export default SecondTab;