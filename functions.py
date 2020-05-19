
code = list('zyxwvutsrqponmlkjihgfedcba ')

def changer(x):
    answer = {
        'a':code[0],
        'b':code[1],
        'c':code[2],
        'd':code[3],
        'e':code[4],
        'f':code[5],
        'g':code[6],
        'h':code[7],
        'i':code[8],
        'j':code[9],
        'k':code[10],
        'l':code[11],
        'm':code[12],
        'n':code[13],
        'o':code[14],
        'p':code[15],
        'q':code[16],
        'r':code[17],
        's':code[18],
        't':code[19],
        'u':code[20],
        'v':code[21],
        'w':code[22],
        'x':code[23],
        'y':code[24],
        'z':code[25],
        ' ':code[26],
    }[x]
    return answer

def fixer(x):
    answer = {
        code[0]:'a',
        code[1]:'b',
        code[2]:'c',
        code[3]:'d',
        code[4]:'e',
        code[5]:'f',
        code[6]:'g',
        code[7]:'h',
        code[8]:'i',
        code[9]:'j',
        code[10]:'k',
        code[11]:'l',
        code[12]:'m',
        code[13]:'n',
        code[14]:'o',
        code[15]:'p',
        code[16]:'q',
        code[17]:'r',
        code[18]:'s',
        code[19]:'t',
        code[20]:'u',
        code[21]:'v',
        code[22]:'w',
        code[23]:'x',
        code[24]:'y',
        code[25]:'z',
        code[26]:' ',
    }[x]
    return answer

def encode(string):
    ex = list(string)
    final = [changer(ex[i]) for i in range(len(ex))]
    final = ''.join(final)
    return final

def decode(string):
    ex = list(string)
    final = [fixer(ex[i]) for i in range(len(ex))]
    final = ''.join(final)
    return final
