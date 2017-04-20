var binary_search = function(array, target) {

  var start = 0;
  var end = array.length - 1;
  while (start < end) {

    var mid = start + (Math.floor(((end - start) / 2)));
  
    if(target === array[mid]) {
      return mid;
    }
    else if (target > array[mid]){
      start = mid + 1;
    }
    else {
      end = mid - 1;
    }
  }
};

console.log(binary_search([1, 3, 4, 7, 8, 10], 2));
