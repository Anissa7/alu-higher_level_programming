#!/usr/bin/node
const numberOfArgs = process.argv.length;

if (numberOfArgs == 0) {
  console.log('No arguments');
} else if (numberOfArgs == 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found')
}
