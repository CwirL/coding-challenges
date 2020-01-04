
// Exit event
process.on('exit', function() {
  process.nextTick(function () {
    console.log('Esto no se ejecutará')
  })
  console.log('Apunto de salir.')
  process.stdout.write('Not from console');
})

// Output stream
console.log = function (d) {
  process.stdout.write(d + '\n');
};

// Read data
process.stdin.resume();
process.stdin.setEncoding('utf8');
process.stdin.on('data', function (chunk) {
  process.stdout.write('data: ' + chunk);
});

// SIGINT = CTRL+C
process.on('SIGINT', function () {
  console.log('Recibido SIGINT.  Haz Control-D para salir.');
});