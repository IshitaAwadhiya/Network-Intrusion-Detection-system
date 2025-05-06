// import React, { useState, useEffect } from 'react';

// function App() {
//     const [logs, setLogs] = useState([]);

//     useEffect(() => {
//         fetch('/logs')
//             .then(res => res.json())
//             .then(data => setLogs(data.logs));
//     }, []);

//     return (
//         <div>
//             <h2>Intrusion Alerts</h2>
//             <ul>
//                 {logs.map((log, index) => (
//                     <li key={index}>{log.timestamp}: {log.alert}</li>
//                 ))}
//             </ul>
//         </div>
//     );
// }

// export default App;


import React, { useState, useEffect } from 'react';

function App() {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/logs')
      .then(res => res.json())
      .then(data => setLogs(data))
      .catch(err => console.error('API Error:', err));
  }, []);

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h2> 🚨 Intrusion Alerts</h2>

      <span
              style={{
                color: alert.prediction === "Intrusion Detected!" ? "red" : "green",
                fontWeight: "bold",
              }}
            >
              {alert.prediction}
            </span>{" "}

      <ul>
        {logs.length === 0 ? (
          <p>No alerts yet.</p>
        ) : (
          logs.map((log, index) => (
            <li key={index}>
              <strong>{log.timestamp}</strong>:  {log.prediction}  — <em>{log.features}</em>
            </li>
                
          ))
        )}
      </ul>
    </div>
  );
}

export default App;
  
