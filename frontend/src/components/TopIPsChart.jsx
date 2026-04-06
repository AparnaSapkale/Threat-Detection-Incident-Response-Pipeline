import React, { useEffect, useState } from "react";
import { PieChart, Pie, Tooltip } from "recharts";

const TopIPsChart = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/top-ips")
      .then(res => res.json())
      .then(data => setData(data));
  }, []);

  return (
    <PieChart width={400} height={300}>
      <Pie data={data} dataKey="count" nameKey="ip" outerRadius={100} />
      <Tooltip />
    </PieChart>
  );
};

export default TopIPsChart;