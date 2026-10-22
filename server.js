// Serves the MAKOM tunnel dashboard (a single static page) on Railway's $PORT.
const http = require('http');
const fs = require('fs');
const path = require('path');

const page = fs.readFileSync(path.join(__dirname, 'docs', 'index.html'));
const port = process.env.PORT || 3000;

http.createServer((req, res) => {
  if (req.method !== 'GET' && req.method !== 'HEAD') { res.writeHead(405); return res.end(); }
  res.writeHead(200, {
    'Content-Type': 'text/html; charset=utf-8',
    'Cache-Control': 'no-cache',
    'X-Content-Type-Options': 'nosniff',
  });
  res.end(req.method === 'HEAD' ? undefined : page);
}).listen(port, '0.0.0.0', () => console.log(`MAKOM dashboard on :${port}`));
