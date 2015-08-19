## August-19-2015

# [Click here to give us feedback and let us know what you want!](http://goo.gl/forms/FbV0D7K5ww)

### Problem 1: Length of Last Word
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string. If the last word does not exist, return 0.

Example:

Input: `"Welcome to the Interview Prep and Algorithm Study Group"`

Output: `5`

### Problem 2: Valid Parentheses
Given a string containing just the characters `(`, `)`, `{`, `}`, `[` and `]`, determine if the input string is valid.

The brackets must close in the correct order, `'()'` and `'()[]{}'` are all valid but `'(]'` and `'([)]'` are not.

### Problem 3: Hill
Given an array of integer elements, write a function that finds the minimum value X that makes possible the following: generate a new array that is sorted in strictly ascending order by increasing or decreasing each of the elements of the initial array with integer values in the `[0, X]` range. Print the result `X` to the standard output/console.

Example:

Having the initial array `[5, 4, 3, 2, 8]` the minimum value for `X` is `3`. 

Explanation:

Decrease the first element (5) by 3, decrease the second one (4) by 1, increase the third one (3) by 1, increase the forth one (2) by 3 and do nothing to the last one (8). In the end we obtain the array [2, 3, 4, 5, 8] which is sorted in strictly ascending order.

Note: strictly ascending order means that each element is greater than the preceding one (e.g. [1, 2, 2, 3] is NOT strictly ascending order)

### Problem 4: Deviation
Given an array of integer elements and an integer d please consider all the sequences of d consecutive elements in the array. For each sequence we compute the difference between the maximum and the minimum value of the elements in that sequence and name it the deviation.

Example:

Input
```
   v: [6, 9, 4, 7, 4, 1]
   d: 3
```

Output
```
   6
```

Explanation

The sequences of length 3 are:
- `6 9 4` having the median 5 (the minimum value in the sequence is 4 and the maximum is 9)
- `9 4 7` having the median 5 (the minimum value in the sequence is 4 and the maximum is 9)
- `7 4 1` having the median 6 (the minimum value in the sequence is 1 and the maximum is 7)
The maximum value among all medians is 6

### Problem 5
Given an array of integer elements, a subsequence of this array is a set of consecutive elements from the array (i.e: given the array `[7, 8, -3, 5, -1]`, a subsequence is `8, -3, 5`), write a function that finds a left and a right subsequence of the array that satisfy the following conditions:

- the two subsequences are unique (they don't have shared elements)
- the difference between the sum of the elements in the right subsequence and the sum of the elements in the left subsequence is maximum

Print the difference to the standard output (stdout)

Example:

Input
```
   [3, -5, 1, -2, 8, -2, 3, -2, 1]
```
Output
```
   15
```

Explanation:

- The left sequence is `-5, 1, -2 (sum = -6)`
- The right sequence is: `8, -2, 3 (sum = 9)`
- `9 - -6 = 15`
