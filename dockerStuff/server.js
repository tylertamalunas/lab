// import HTTP module
const http = require('http');

// create server object
const server = http.createServer((req, res) => {
	// set response HTTP header with HTTP status and Content type
	res.writeHead(200, { 'Content-Type': 'text/plain' });

	// send response
	res.end('Hello There! You just started an http server!!!!\n');
});

// define port to listen on
const PORT = 8080;

// start server and listen on port
server.listen(PORT, () => {
	console.log(`Server running at http://localhost:${PORT}/`);
});
