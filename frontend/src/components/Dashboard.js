import React, { useEffect, useState } from "react";
import { fetchMetrics } from "../services/api";
import { LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid } from "recharts";

export default function Dashboard() {
  const [metrics, setMetrics] = useState([]);
  useEffect(() => {
    const interval = setInterval(async () => {
      const data = await fetchMetrics();
      setMetrics(data);
    }, 5000);
    return () => clearInterval(interval);
  }, []);
  return (
    <div>
      <h2>Analytics Dashboard</h2>
      <LineChart width={600} height={300} data={metrics}>
        <XAxis dataKey="timestamp" />
        <YAxis />
        <CartesianGrid stroke="#eee" strokeDasharray="5 5"/>
        <Tooltip/>
        <Line type="monotone" dataKey="value" stroke="#8884d8"/>
      </LineChart>
    </div>
  );
}
