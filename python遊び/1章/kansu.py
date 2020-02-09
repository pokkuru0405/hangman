def f():
    """
    Returns x * x
    :param x: int
    
    """
    x = input("2乗する数を入力:")
    x = int(x)
    print(x*x)  
f()

def y(y):
    print(y)
y("おちんぽ")

def z(x,y=2,z=3):
    return x+y+z
print(z(1,3))

def f(x):
    return x//3
def y(y):
    return y*4
a = f(122)
print(y(a))

def f(x):
    try:
        print(float(x))
    except ValueError:
        print("それはおちんちん")
a = 3
f(a)
