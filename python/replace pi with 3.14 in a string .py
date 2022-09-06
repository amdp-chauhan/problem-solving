# Problem: replace pi with 3.14 in a given string
def replace_pi(string): 
    if len(string)<=1:
        return string

    if string[:2]=='pi':
        remaining_str = replace_pi(string[2:])
        return '3.14'+remaining_str
    else:
        remaining_str = replace_pi(string[1:])
        return string[0]+remaining_str

# Main
string = input()
print('Input - ',string)
print('Output - ',replace_pi(string))
