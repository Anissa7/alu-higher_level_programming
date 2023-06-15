#!/usr/bin/node
<<<<<<< HEAD
const numberOfArgs = process.argv.length;

if (numberOfArgs == 0) {
  console.log('No arguments');
} else if (numberOfArgs == 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found')
=======
switch (process.argv.length) {
  case 2:
    console.log('No argument');
    break;
  case 3:
    console.log('Argument found');
    break;
  default:
    console.log('Arguments found');
    break;
>>>>>>> daa2712bae33371bf4f6ee8ee249d7322b095679
}
