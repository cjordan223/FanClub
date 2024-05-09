// DataVisualization.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import {
    Chart as ChartJS,
    LineElement,
    BarElement,
    CategoryScale,
    LinearScale,
    PointElement,
    Title,
    Tooltip,
    Legend,
} from 'chart.js';
import { Line, Bar } from 'react-chartjs-2';


ChartJS.register(
    LineElement,
    BarElement,
    CategoryScale,
    LinearScale,
    PointElement,
    Title,
    Tooltip,
    Legend
);

const DataVisualization = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        axios.get('http://192.168.0.19:5065/api/data')
            .then((response) => setData(response.data))
            .catch((error) => console.error('Error fetching data:', error));
    }, []);

    // Extract specific metrics for visualization
    const timestamps = data.map(item => item.timestamp);
    const cpuUsages = data.map(item => item.raw_data.cpu_usage);
    const memoryUsed = data.map(item => item.raw_data.memory?.used || 0);
    const memoryTotal = data.map(item => item.raw_data.memory?.total || 0);

    // Access network data directly
    const bytesSent = data.map(item => item.raw_data.network?.bytes_sent || 0);
    const bytesReceived = data.map(item => item.raw_data.network?.bytes_recv || 0);

    // Chart data
    const cpuLineChartData = {
        labels: timestamps,
        datasets: [
            {
                label: 'CPU Usage (%)',
                data: cpuUsages,
                borderColor: 'rgba(75,192,192,1)',
                fill: false,
            },
        ],
    };

    const memoryBarChartData = {
        labels: ['Used', 'Total'],
        datasets: [
            {
                label: 'Memory (Bytes)',
                data: [memoryUsed[0] || 0, memoryTotal[0] || 0],
                backgroundColor: ['rgba(255, 99, 132, 0.6)', 'rgba(54, 162, 235, 0.6)'],
            },
        ],
    };

    const networkBarChartData = {
        labels: ['Bytes Sent', 'Bytes Received'],
        datasets: [
            {
                label: 'Network (Bytes)',
                data: [bytesSent[0] || 0, bytesReceived[0] || 0],
                backgroundColor: ['rgba(255, 205, 86, 0.6)', 'rgba(75, 192, 192, 0.6)'],
            },
        ],
    };

    const chartContainerStyle = {
        maxHeight: '400px',
        maxWidth: '100%',
        marginBottom: '40px',
    };

    return (
        <div>
            <h2>System Monitoring Data</h2>

            <div style={chartContainerStyle}>
                <h3>CPU Usage Over Time</h3>
                <Line data={cpuLineChartData} />
            </div>

            <div style={chartContainerStyle}>
                <h3>Memory Usage</h3>
                <Bar data={memoryBarChartData} />
            </div>

            <div style={chartContainerStyle}>
                <h3>Network Usage</h3>
                <Bar data={networkBarChartData} />
            </div>
        </div>
    );
};

export default DataVisualization;
