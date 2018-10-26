
const numbers = [11,7,3,5,1,9,2];
var outer;

for( outer = 0; outer < numbers.length -1 ; outer++) {
  var minNumberIndex = outer;
  var inner;
  for(inner = outer + 1; inner < numbers.length; inner++) {
    if(numbers[inner] < numbers[minNumberIndex]) {
      minNumberIndex = inner;
    }
  }
  console.log(numbers);
  var temp = numbers[minNumberIndex];
  numbers[minNumberIndex] = numbers[outer];
  numbers[outer] = temp;  
}

//output [1, 2, 3, 5, 7, 9, 11]
