def modulus(num, div):
    '''Returns the remainder of num / div
(int, div) -> int'''
    num = int(num)
    div = float(div)
    times_subtracted = 0
    while num > div: #Continuously subtracts div from num until num stopping when subtracting would make num negative
        num = num - div
        times_subtracted += 1 #The answer without remainder
    return int(num) #The remainder without the answer
