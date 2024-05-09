import React, { useState, useEffect } from 'react';
import io from 'socket.io-client';
import { Line } from 'react-chartjs-2';

// Initialize WebSocket connection
const socket = io('http://localhost:5066');

// Utility function to convert bytes to human-readable units
const formatBytes = (bytes) => {
    const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
    if (bytes === 0) return '0 Bytes';
    const i = parseInt(Math.floor(Math.log(bytes) / Math.log(1024)));
    return `${(bytes / Math.pow(1024, i)).toFixed(2)} ${sizes[i]}`;
};

// Style for chart containers
const chartContainerStyle = {
    width: '80%',
    height: '300px',
    margin: 'auto',
    marginBottom: '40px',
};

const DataVisualizationLive = () => {
    const [metrics, setMetrics] = useState([]);

    useEffect(() => {
        // Listen to live updates from WebSocket
        socket.on('live_update', (data) => {
            console.log('Received WebSocket Data:', data); // Log WebSocket data
            setMetrics((prevMetrics) => {
                const updatedMetrics = [...prevMetrics, ...data]; // Append new data
                // Limit to the last 15 data points
                return updatedMetrics.length > 15 ? updatedMetrics.slice(-15) : updatedMetrics;
            });
        });
    }, []);

    // Extract metrics for the live visualization
    const timestamps = Array.from({ length: metrics.length }, (_, i) => `T${i + 1}`);
    const cpuUsages = metrics.map((m) => m.cpu_usage);
    const memoryUsed = metrics.map((m) => m.memory?.used || 0);
    const networkSent = metrics.map((m) => m.network?.bytes_sent || 0);
    const networkReceived = metrics.map((m) => m.network?.bytes_recv || 0);

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

    const memoryLineChartData = {
        labels: timestamps,
        datasets: [
            {
                label: 'Memory Used (Bytes)',
                data: memoryUsed,
                borderColor: 'rgba(255, 99, 132, 1)',
                fill: false,
            },
        ],
    };

    const networkLineChartData = {
        labels: timestamps,
        datasets: [
            {
                label: 'Network Bytes Sent',
                data: networkSent,
                borderColor: 'rgba(54, 162, 235, 1)',
                fill: false,
            },
            {
                label: 'Network Bytes Received',
                data: networkReceived,
                borderColor: 'rgba(255, 205, 86, 1)',
                fill: false,
            },
        ],
    };

    return (
        <div>
            <h2>Live System Monitoring Data</h2>

            <div style={chartContainerStyle}>
                <h3>CPU Usage Over Time</h3>
                <Line data={cpuLineChartData} />
            </div>

            <div style={chartContainerStyle}>
                <h3>Memory Usage Over Time</h3>
                <Line data={memoryLineChartData} />
            </div>

            <div style={chartContainerStyle}>
                <h3>Network Usage Over Time</h3>
                <Line data={networkLineChartData} />
            </div>
        </div>
    );
};

export default DataVisualizationLive;
