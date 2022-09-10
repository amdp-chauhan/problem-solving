"""Check AB

Suppose you have a string, S, made up of only 'a's and 'b's. Write a recursive function that checks if the string was generated using the following rules:
a. The string begins with an 'a'
b. Each 'a' is followed by nothing or an 'a' or "bb"
c. Each "bb" is followed by nothing or an 'a'

If all the rules are followed by the given string, return true otherwise return false.

Input format :
String S

Output format :
'true' or 'false'

Constraints :
1 <= |S| <= 1000

where |S| represents length of string S.
Sample Input 1 :
abb
Sample Output 1 :
true

Sample Input 2 :
abababa
Sample Output 2 :
false

Explanation for Sample Input 2
In the above example, a is not followed by either 'a' or 'bb', instead it's followed by 'b' which results in false to be returned.
"""
## Read input as specified in the question.
## Print output as specified in the question.
def checkAB(string, ci):
    if ci==len(string):
        return 'true'

    if string[0]!='a':
        return 'false'

    if string[ci]=='a' and (len(string[ci:])==1 or string[ci+1]=='a' or (string[ci+1]=='b' and string[ci+2]=='b')):
        return checkAB(string, ci+1)
    elif string[ci]=='b' and string[ci+1]=='b' and (len(string[ci:])==2 or string[ci+2]=='a'):
        return checkAB(string, ci+2)
    else:
        return 'false'

string = "abbaabb"# str(input())
print(checkAB(string, 0))
