# Decorators example 1 - Smart Divide

def smartDivide(func):
    def valueCheck(a,b):
        print(f"dividing {a} and {b}:")
        if b == 0:
            print("Whoops! cannot divide")
        else:
            return func(a, b)
    return valueCheck


@smartDivide
def divide(a, b):
    print(a/b)

a,b = map(int,input("Enter a,b: ").split())
divide(a,b)
