#week 1-1
def xor_with_zero(input_string):
    result = ''
    for char in input_string:
        result += chr(ord(char) ^ 0)
    return result

input_string = 'Hello world.'
result = xor_with_zero(input_string)
print("Result after XORing each character with 0:", result)

#week 1-2
def and_xor_with_127(input_string):
    and_result = ''
    xor_result = ''
    for char in input_string:
        and_result += chr(ord(char) & 127)
        xor_result += chr(ord(char) ^ 127)
    return and_result, xor_result

input_string = 'Hello world.'
and_result, xor_result = and_xor_with_127(input_string)
print("Result after ANDing each character with 127:", and_result)
print("Result after XORing each character with 127:", xor_result)



