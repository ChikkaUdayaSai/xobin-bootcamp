'''
Bravo is preparing for his CA (Chartered Accountancy) Exam. Being a sincere student, Bravo wants to read every chapter in all the books. He writes down and keeps updating the remaining number of unread chapters on the back cover of each book.

Bravo has a lot of books messed on the floor. Therefore, he wants to pile up the books that still have some remaining chapters into a single pile. He will grab the books one-by-one and add the books that still have unread chapters to the top of the pile. Whenever he wants, he will pick the book with the minimum number of unread chapters from the pile.

In order to pick the book, he has to remove all the books above it. Therefore, if there are more than one books with the minimum number of remaining chapters, he will take the one which requires the least number of books to remove. The removed books are returned to the messy floor. After he picks the book, he will do all the remaining chapters and trash the book.

Since number of books is rather large, he needs your help to tell him the number of books he must remove, for picking the book with the minimum number of exercises.

Input

The first line contains a single integer N denoting the number of actions. Then N lines follow. Each line contains an integers . If the integer is -1, that means Bravo wants to finish a book. Otherwise, the integer is number of the remaining chapters in the book he grabs. This is space separated by a string denoting the name of the book.

Output

For each -1 in the input, output a single line containing the number of books Bravo must remove, followed by the name of the book that Bravo must pick.

Constraints

Example

Input:

4

4 economics

5 mathematics

3 finance

-1

Output:

0 finance

'''

t = int(raw_input())
b = []
s = 1000
for test in range(t):
  q = raw_input()
  if q != '-1':
    q = q.split()
    b.append(q[1])
    if int(q[0]) < s:
      s = int(q[0])
      index = test
  else:
    print t-2-index,b[index]
