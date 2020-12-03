# AoC20
Advent of Code 2020

## Day 01
### Part 1
Given a list of numbers, find pairs of list elements who add up to a specific number (2020).

Approach:
* sort list
* for each list element e: binary search for 2020-e

### Part 2
Same as part 1 but with three numbers instead of two.

Approach:
* sort list
* fix first element of triplet (e1 = list[i])
* Then fix two pointers, one at i + 1 and the other at n – 1. And look at the sum,
  * If the sum is smaller than the required sum, increment the first pointer.
  * Else, If the sum is bigger, Decrease the end pointer to reduce the sum.
  * Else, if the sum of elements at two-pointer is equal to given sum then print the triplet and break.
