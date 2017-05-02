function first_unique(string) {
   var hash = {};
   for (var i = 0; i < string.length; i++) {
       if (hash.hasOwnProperty(string[i])) {
           hash[string[i]] += 1;
       } else {
           hash[string[i]] = 1;
       }
   }
   console.log(hash);
   for (var prop in hash) {
       if (hash[prop] === 1) {
           console.log(prop);
           break;
       }
   }
}

first_unique(‘bballs’);
