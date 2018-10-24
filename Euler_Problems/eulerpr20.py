def main(num):
    nerm = factorial(num)
    ans = Sum1(str(nerm))
    return ans
def factorial(num):
    if num > 1:
        return num * factorial(num-1)
    else:
        return 1

def Sum1(string):
    if len(string)>0:
        return int(string[0])+Sum1(string[1:])
    else:
        return 0

print(main(100))
