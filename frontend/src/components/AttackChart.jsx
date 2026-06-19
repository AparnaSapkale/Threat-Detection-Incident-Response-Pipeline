import React, { useEffect, useState } from "react";

import {
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
} from "recharts";

import "../styles/components/chart.css";

const AttackChart = () => {

  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8001/attack-stats")
      .then((res) => res.json())
      .then((data) => setData(Array.isArray(data) ? data : []));
  }, []);

  return (
    <div className="chart-container">

      <h3 className="chart-title">
        Attack Frequency
      </h3>

      <div className="chart-wrapper">

        <ResponsiveContainer width="100%" height={320}>

          <BarChart
            data={data}
            margin={{
              top: 10,
              right: 20,
              left: 0,
              bottom: 5,
            }}
          >

            <CartesianGrid
              strokeDasharray="3 3"
              stroke="rgba(255,255,255,0.06)"
            />

            <XAxis
              dataKey="attack_type"
              stroke="#94a3b8"
              tick={{ fontSize: 12 }}
            />

            <YAxis
              stroke="#94a3b8"
              tick={{ fontSize: 12 }}
            />

            <Tooltip
              contentStyle={{
                backgroundColor: "#0f172a",
                border: "1px solid rgba(255,255,255,0.08)",
                borderRadius: "10px",
                color: "white",
              }}
            />

            <Bar
              dataKey="count"
              fill="#ef4444"
              radius={[6, 6, 0, 0]}
            />

          </BarChart>

        </ResponsiveContainer>

      </div>

    </div>
  );
};

export default AttackChart;