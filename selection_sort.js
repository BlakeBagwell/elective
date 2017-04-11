var arr = [2, 3, 6, 2, 5, 6, 7, 9, 3, 0];
var min = 0;

// for (var i = 0; i <= arr.length - 1; i++) {
//   min = arr[i]; //initially sets the minimum value to the first number in the array.
//   for (var j = i; j <= arr.length - 1; j++) {
//     if (arr[j] < min) {
//       //then, if we find a number that is less than what the minimum is, we swap those values around. Once swapped, we move to the next index in the array.
//       min = arr[j];
//       arr[j] = arr[i];
//       arr[i] = min;
//     }
//   }
// }

for (var i = 0; i <= arr.length - 1; i++) {
  for (var j = i; j <= arr.length - 1; j++) {
    if (arr[j] < arr[i]) {
      //in this case, as opposed to above, we dont need the min variable. With a nested loop, the first loop is basically holding only a value, and in the second loop, we are comparing all numbers in the array (that are past the number we are holding onto), with the number we are holding onto. 
      var temp = arr[j];
      arr[j] = arr[i];
      arr[i] = temp;
    }
  }
}// in this case we dont need the min variable at all.

console.log(arr);
