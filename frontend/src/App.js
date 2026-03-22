import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [properties, setProperties] = useState([]);
  const [health, setHealth] = useState(null);

  useEffect(() => {
    axios.get('/health')
      .then(res => setHealth(res.data.status))
      .catch(() => setHealth('offline'));

    axios.get('/api/v1/properties')
      .then(res => setProperties(res.data.properties))
      .catch(err => console.log(err));
  }, []);

  return (
    <div style={{ fontFamily: 'Arial', padding: '20px' }}>
      <h1>🏠 Real Estate Investment Analyzer</h1>
      <p>API Status: <strong>{health || 'checking...'}</strong></p>
      <h2>Properties ({properties.length})</h2>
      {properties.length === 0 && <p>No properties yet. Start scraping!</p>}
    </div>
  );
}

export default App;
