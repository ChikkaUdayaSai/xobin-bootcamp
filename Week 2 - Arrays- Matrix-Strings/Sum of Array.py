'''
Given an integer array of size N, Write a Program to find sum of elements in it.

Input:
The First Line of the Testcase contatain an Integer N Denoting the size of array. The nextline of the testcase contains N space separated integers.

Output:
Print the sum of all elements of the array of the testcase

Example:
Input:
3
3 2 1


Output:
6

'''

n = int(raw_input())
l = [int(x) for x in raw_input().split()]
s = 0
for i in l:
  s += i
  
print s
