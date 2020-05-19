from functions import *
import time

while True:
    a = input('\nWould you like to encode or decode something?')

    if a == 'encode':
        print('type the text you would like to encode')
        txt = input('>>')
        etxt = encode(txt)
        print('encoded: ' + etxt)
    elif  a == 'decode':
        print('type the text you would like to decode')
        txt = input('>>')
        etxt = decode(txt)
        print('decoded: ' + etxt)

    else:
        print('\nThat is not a valid answer, please respond with "encode" or "decode"')
        time.sleep(2)
