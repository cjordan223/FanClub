// App.js
import React from 'react';
import DataVisualization from './Components/DataVisualization';
import DataVisualizationLive from "./Components/DataVisualizationLive";  // Adjust path as needed

function App() {
    return (
        <div>
            <h1>Cybersecurity Monitoring Dashboard</h1>
            <DataVisualizationLive />
        </div>
    );
}

export default App;
