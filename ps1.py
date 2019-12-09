# Function to validate the input string
def validate_string(input_string):
    for i in input_string:
        if i != '0' and i!='1':
            return False
    return True

# function to stuff the bits in the frame
def bit_stuff(input_string):
    tx_string = ''
    i = 0
    while(i< len(input_string)):
        if (input_string[i] == '0' and input_string[i+1] == '1' and input_string[i+2] == '0'):
            tx_string = tx_string + '0100'
            i = i + 3
        else:
            tx_string += input_string[i]
            i += 1
    tx_string = tx_string+'0101'
    return tx_string

# Execution starts here
if __name__ == "__main__":

    print("Enter binary data to transmit: ")
    input_string = input()
    if validate_string(input_string) == False:
        print("Invalid string!!\n")
        exit(-1)

    # parity string
    parity_str = input_string

    xor_res = 0
    for i in input_string:
        xor_res = xor_res ^ int(i)

    if xor_res == 0:
        parity_str = parity_str+'1'
    else:
        parity_str = parity_str+'0'

    print('Parity string: ',parity_str)


    '''
    Bit stuffed string
    '''
    tx_string = bit_stuff(parity_str)    
    print('Transmitted string: ',tx_string)
