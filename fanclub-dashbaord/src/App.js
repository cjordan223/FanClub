// App.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

function DataDisplay() {
    const [data, setData] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const result = await axios('http://localhost:5065/data');
                setData(result.data);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };
        fetchData();
    }, []);

    return (
        <div>
            <h1>Data from Flask</h1>
            <ul>
                {data.map((item, index) => (
                    <li key={index}>
                        Hostname: {item.host_name}, IP Address: {item.ip_address},
                        RAM Size: {item.ram_size}, Storage: {item.storage_amount}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default DataDisplay;
