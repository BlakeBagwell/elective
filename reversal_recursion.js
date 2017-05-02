function pallycheck(arr, index) {
  if (index >= arr.length - 1 - index) {
    console.log('true');
  } else if (arr[index] === arr[arr.length - 1 - index]) {
    return pallycheck(arr, index + 1);
  } else {
    console.log('false');
  }
}


// pallycheck(['h','a', 'n', 'n', 'a', 'h'], 0);
// pallycheck(['b', 'l', 'a', 'k', 'e'], 0);

function arrayMe(string) {
  return pallycheck(string.split(''), 0);
}

arrayMe('blake');
arrayMe('racecar');
