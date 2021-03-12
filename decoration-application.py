# decorator function to convert to lowercase
def lowercase_decorator(function):
    def wrapper():
        first_name, last_name = function()
        first_name, last_name = first_name.lower(), last_name.upper()
        return first_name, last_name
    return wrapper

# decorator function to split words
def stripper_decorator(function):
    def wrapper():
        first_name, last_name = function()
        first_name, last_name = first_name.strip(), last_name.strip()
        return f'{first_name} {last_name}'
    return wrapper

@stripper_decorator # this is executed next
@lowercase_decorator # this is executed first
def convert_case():
    return '  Amardeep  ', '  ChaUHan'

print(convert_case()) # output => [ 'Amardeep' , 'ChaUHan' ]
