# Will successfully convert Numbers from 1 to 1000

unique_numerals = {1:'I', 4: 'IV', 5:'V', 9: 'IX', 10:'X', 40: 'LX', 45: 'VL', 50:'L', 90:'XC', 95:'VC', 100:'C', 
                   400: 'CD', 450: 'LD', 490: 'XD', 495:'VD', 500:'D', 900: 'CM', 950:'LM', 990:'XM', 995:'VM', 1000:'M'}


def convert_to_roman(num):
    copy_num = num
    result = ''
    # for 50
    for roman_n in sorted(unique_numerals.keys(), reverse=True):
        resp = copy_num/roman_n
        if int(resp)==0:
            continue
        # print(roman_n, resp)
        roman_representation = unique_numerals[roman_n]*int(resp)
        # print(roman_representation)

        result = result+roman_representation
        copy_num = copy_num%roman_n

    return result

print(convert_to_roman(786))
