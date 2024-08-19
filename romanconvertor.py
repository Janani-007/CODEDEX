num_input=input("Enter the romen numeral that you want to convert: ")

def rom_to_int(num):
    result=0
    if "CM" in num:
       result += 900
       num = num.replace("CM", "")
    if "CD" in num:
       result += 400
       num = num.replace("CD", "")
    if "XC" in num:
       result += 90
       num = num.replace("XC", "")
    if "XL" in num:
       result += 40
       num = num.replace("XL", "")
    if "IX" in num:
       result += 9
       num = num.replace("IX", "")
    if "IV" in num:
       result += 4
       num = num.replace("IV", "")
    for i in num:
        if i=="M":
            result +=1000
        elif i=="D":
            result +=500
        elif i=="C":
            result +=100
        elif i=="L":
            result +=50
        elif i=="X":
            result +=10
        elif i=="V":
            result +=5
        elif i=="I":
            result +=1
    print("The roman numerals you entered translates to: "+str(result)+"!")
rom_to_int(num_input)        