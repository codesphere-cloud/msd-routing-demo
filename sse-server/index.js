// index.js
const express = require('express');
const app = express();
const PORT = 3000;

app.get('/events', (req, res) => {
    res.setHeader('Content-Type', 'text/event-stream');
    res.setHeader('Cache-Control', 'no-cache');
    res.setHeader('Connection', 'keep-alive');

    const sendData = () => {
        const message = `event: data\ndata: ${new Date().toISOString()}\n\n`;
        res.write(message);
    };

    // Send an initial event
    sendData();

    // Send updates every 5 seconds
    const interval = setInterval(sendData, 100);

    // Clean up if client disconnects
    req.on('close', () => {
        clearInterval(interval);
        res.end();
    });
});

app.listen(PORT, () => {
    console.log(`✅ SSE server running at http://localhost:${PORT}`);
});
