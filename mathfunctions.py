import math

def basic(voice_data):
    voice_data = voice_data.replace("what is","")
    voice_data = voice_data.replace("plus","+")
    voice_data = voice_data.replace("minus","-")
    voice_data = voice_data.replace("multiply","*")
    voice_data = voice_data.replace("x","*")
    voice_data = voice_data.replace("into","*")
    voice_data = voice_data.replace("times","*")
    voice_data = voice_data.replace("multiplied by","*")
    voice_data = voice_data.replace(" divided by ","/")
    voice_data = voice_data.replace("to the power of","**")
    voice_data = voice_data.replace("raise to","**")
    voice_data = voice_data.replace("raised to","**")
    voice_data = voice_data.replace(" ","")
    final = eval(voice_data)
    return round(final)

def factorial(n):
    
    n = int(n)
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

def roots(voice_data):
    print("in roots")
    voice_data=voice_data.replace("what is","")
    print(voice_data)
    voice_data=voice_data.replace("root","")
    print(voice_data)
    exp = voice_data.split('of')[0]
    print(exp)
    rexp = float(1/float(exp))
    print(rexp)
    base = voice_data.split('of')[1]
    print(base)
    result = round((float(base)**rexp),2)
    return (result)