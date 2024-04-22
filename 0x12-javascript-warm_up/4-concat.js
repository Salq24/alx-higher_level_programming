#!/usr/bin/node

const conc = process.argv[2];
const conc2 = process.argv[3];
if (!conc) {
  console.log('undefined is ' + conc2);
} else if (!conc2) {
  console.log(conc + ' is ' + 'undefined');
} else {
  console.log(conc + ' is ' + conc2);
}
