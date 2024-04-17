const http = require('http');
const fs = require('fs');
const url = require('url');

http.createServer(function (req, res) {
    const q = url.parse(req.url, true);

    const regex = /\/(c\d+)/;

    if (q.pathname === "/" || q.pathname === "/index.html") { 
        fs.readFile('results/index.html', function (err, data) {
            res.writeHead(200, {'Content-Type': 'text/html'});
            res.write(data);
            res.end();
        });
    } else if (regex.test(q.pathname)) {
        console.log(q.pathname)
        const file = q.pathname.substring(1);
        console.log(file)
        fs.readFile('results/' + file, function (err, data) {
            res.writeHead(200, {'Content-Type': 'text/html'});
            res.write(data);
            res.end();
        });
    } else {
        console.log(q.pathname)
        res.writeHead(404, {'Content-Type': 'text/html'});
        res.write("<h1>404 Not Found</h1>");
        res.end();
    }
}).listen(7777);
