function solution(S) {;
  let xCount = 0;
  let yCount = 0;
  let totalX = 0;
  let totalY = 0;

  // Count total occurrences of 'x' and 'y' in the string
  for (let i = 0; i < S.length; i++) {
    if (S[i] === 'x') {
      totalX++;
    } else if (S[i] === 'y') {
      totalY++;
    }
  }

  let count = 0;

  // Iterate through the string and count the number of splits
  for (let i = 1; i < S.length; i++) {
    if (S[i - 1] === 'x') {
      xCount++;
    } else if (S[i - 1] === 'y') {
      yCount++;
    }

    let leftX = xCount;
    let leftY = yCount;
    let rightX = totalX - leftX;
    let rightY = totalY - leftY;

    if (leftX === leftY || rightX === rightY) {
      count++;
    }
  }

  return count;
}