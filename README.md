# permutations
Find permutations of a given list of items. Build permutations list of a given list of items and for a given length.

Problem Statement:
Input array is list of items. Find all permutations of this list for a given length.
If length is not given, it should defaults to array length.

```
Input:
a = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
```
```
Output for length 2: 
[[1, 2], [1,3], ..., [2,1], [2,3], ..., [9,1], [9, 2], [0,1], [0,2]]"
```

## Solution:
By its nature solutuion will be dfs. Termination condition is remaing length of array or length variable.
If it hits 0 then recursion will stop. Length variable determines max depth of recursion. 

If length is empty then max depth is determined by array length. Algorithm collects all
 possible permutation list on each branch and combines them.