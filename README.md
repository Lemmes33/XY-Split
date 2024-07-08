# XY-Split
Problem Statement

Given a string S consisting of N lowercase English letters, find the number of ways to split S into two non-empty parts such that in at least one part, the letter 'x' and the letter 'y' occur the same number of times.

Solution

The solution is implemented in the solution.js file. It takes a string S as input and returns the number of splits that satisfy the condition.

Algorithm

The algorithm works as follows:

Count the total occurrences of 'x' and 'y' in the string.
Iterate through the string and count the number of splits.
For each split, count the number of 'x's and 'y's in the left part and the right part.
Check if the number of 'x's and 'y's in either the left part or the right part are equal. If they are, increment the count.
Return the count.
Time Complexity

The time complexity of the algorithm is O(N), where N is the length of the string.

Space Complexity

The space complexity of the algorithm is O(1), since we only use a few extra variables to store the counts.

Examples

Given S = "ayxbx", the function returns 3.
Given S = "xzzzy", the function returns 0.
Given S = "toyxmy", the function returns 5.
Given S = "apple", the function returns 4.
Usage

To use the solution, simply call the solution function and pass the input string as an argument. For example:

Edit
Copy code
const result = solution("ayxbx");
console.log(result); // Output: 3
License

This solution is licensed under the MIT License. See the LICENSE file for details.




