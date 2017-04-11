var arr = [2, 3, 5, 6, 7, 4, 5, 8, 9];

var find = function(number, array) {
  for (var i = 0; i < array.length - 1; i++) {
    if (number === array[i]) {
      console.log(i);
    }
  }
};

find(7, arr);
find(0, arr);
