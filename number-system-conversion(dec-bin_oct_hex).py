# Convert to Decimal to Binary, Octal, Hex
number = 1234567
# Using built-in functions
print('** Using built-in functions **')
print(f'Binary: {bin(number)}')
print(f'Octal: {oct(number)}')
print(f'Hex: {hex(number)}')


# Using custom logic
hex_dict = {10 : 'A' , 11 : 'B' , 12 : 'C' , 13 : 'D' , 14 : 'E' , 15 : 'F'}
number = 1234567
print(f'\n** Using custom logic **')

def decimal_to_other(number, target_base):
    temp = number
    output = ''
    while True:
        if int(temp) == 0:
            break
        # division
        res = temp/target_base
        # find remainder        
        remainder = res - int(res)
        # find conversion = remainder * target
        conv_op = int(remainder*target_base)
        # consider remainder only, if it was less than target_base
        conv_op = remainder if conv_op>target_base else conv_op
        # convert to HEX if conv_op goes beyond 10
        converted_num = conv_op if conv_op<10 else hex_dict[conv_op]   
        # append output
        output = f'{converted_num}{output}'
        # pass whole for next itteration
        temp = int(res)

    return output

print('Binry: ',decimal_to_other(1234567, target_base=2))
print('Octal: ',decimal_to_other(1234567, target_base=8))
print('Hex: ',decimal_to_other(1234567, target_base=16))
