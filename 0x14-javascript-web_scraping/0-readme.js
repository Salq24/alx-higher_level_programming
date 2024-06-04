#!/usr/bin/node
//reads and prints file contene


const fsys = require('fs');
const filenm = process.argv[2];

fsys.readFile(filenm, 'utf-8', (error, data) => {
	if (error) {
		console.log(error);
	} else {
		console.log(data);
	}
});

