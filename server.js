// Serves the MAKOM panels (static pages in docs/) on Railway's $PORT.
const http = require('http');
const fs = require('fs');
const path = require('path');

const DOCS = path.join(__dirname, 'docs');
const pages = {};
for (const f of fs.readdirSync(DOCS)) if (f.endsWith('.html')) pages['/' + f] = fs.readFileSync(path.join(DOCS, f));
pages['/'] = pages['/index.html'];
// share cards (Open Graph images)
const images = {};
for (const f of fs.readdirSync(path.join(DOCS, 'og'))) if (f.endsWith('.png')) images['/og/' + f] = fs.readFileSync(path.join(DOCS, 'og', f));
const port = process.env.PORT || 3000;

http.createServer((req, res) => {
  if (req.method !== 'GET' && req.method !== 'HEAD') { res.writeHead(405); return res.end(); }
  const url = req.url.split('?')[0];
  if (images[url]){
    res.writeHead(200, { 'Content-Type': 'image/png', 'Cache-Control': 'public, max-age=86400', 'X-Content-Type-Options': 'nosniff' });
    return res.end(req.method === 'HEAD' ? undefined : images[url]);
  }
  const page = pages[url] || pages[url.replace(/\/$/, '') + '.html'];
  if (!page) { res.writeHead(302, { Location: '/' }); return res.end(); }
  res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8', 'Cache-Control': 'no-cache', 'X-Content-Type-Options': 'nosniff' });
  res.end(req.method === 'HEAD' ? undefined : page);
}).listen(port, '0.0.0.0', () => console.log(`MAKOM panels on :${port}`));
