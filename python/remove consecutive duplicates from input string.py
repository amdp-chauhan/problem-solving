# Approach 1

# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(string):
    # Please add your code here
    if len(string)==0:
        return string

    if string[0]==string[1]:
        remaining = removeConsecutiveDuplicates(string[2:])
        # print(string[:2],remaining)
        if len(remaining)>0 and string[0]==remaining[0]:
            return remaining

        return string[0]+remaining
    else:
        remaining = removeConsecutiveDuplicates(string[1:])
        # print(string[:2],remaining)
        return string[0]+remaining

#  Approach 2 

# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(string):
    # Please add your code here
    if len(string)<=1:
        return string

    if string[0]!=string[1]:
        return string[0] + removeConsecutiveDuplicates(string[1:]
    return removeConsecutiveDuplicates(string[1:] 
    
# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
