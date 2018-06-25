def baseConverter(decNum, base):
    s=''
    l=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    while decNum>0:
        s=l[decNum%base]+s
        decNum=int(decNum/base)
    return s
print(baseConverter(int(input('Enter the decimal number: ')),int(input('Enter the base: '))))
