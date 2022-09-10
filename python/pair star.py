"""
Pair Star
Given a string S, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".

Input format :
String S

Output format :
Modified string

Constraints :
0 <= |S| <= 1000
where |S| represents length of string S.

Sample Input 1 :
hello
Sample Output 1:
hel*lo

Sample Input 2 :
aaaa
Sample Output 2 :
a*a*a*a
"""

## Read input as specified in the question.
## Print output as specified in the question.

def pairStar(string):
    if len(string)<=1:
        return string

    if string[0]!=string[1]:
        return string[0]+pairStar(string[1:])
    return string[0]+"*"+pairStar(string[1:])

n=str(input())
print(pairStar(n))
