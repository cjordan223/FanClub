import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Line, Bar } from 'react-chartjs-2';

const DataVisualization = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        // Ensure the server address matches your server's IP and port.
        axios.get('http://192.168.0.19:5065/api/data')
            .then((response) => setData(response.data))
            .catch((error) => console.error('Error fetching data:', error));
    }, []);

    // Check for undefined fields and provide fallback values
    const timestamps = data.map(item => item.timestamp || 'Unknown');
    const cpuUsages = data.map(item => (item.raw_data?.cpu_usage) ?? 0);
    const memoryUsed = data.map(item => (item.raw_data?.memory?.used) ?? 0);
    const memoryTotal = data.map(item => (item.raw_data?.memory?.total) ?? 0);
    const diskUsed = data.map(item => (item.raw_data?.disk?.used) ?? 0);
    const diskTotal = data.map(item => (item.raw_data?.disk?.total) ?? 0);

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

    const diskBarChartData = {
        labels: ['Used', 'Total'],
        datasets: [
            {
                label: 'Disk (Bytes)',
                data: [diskUsed[0] || 0, diskTotal[0] || 0],
                backgroundColor: ['rgba(153, 102, 255, 0.6)', 'rgba(255, 159, 64, 0.6)'],
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
                <h3>Disk Usage</h3>
                <Bar data={diskBarChartData} />
            </div>
        </div>
    );
};

export default DataVisualization;
