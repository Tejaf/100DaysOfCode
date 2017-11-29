function findOdd(A) {
    let countObj = {};  
    // base case
    if (A.length === 1) {
      return A[0];
    } else {
      for (var i=0; i<A.length; i++) {
        if (A[i] in countObj) {
          countObj[A[i]] += 1;
        } else {
          countObj[A[i]] = 1;
        }
    }
    for (var j in countObj) {	
      if (countObj[j] % 2 !== 0) {
        return parseInt(j)
        } 
      }
    }
  }

module.exports = findOdd;