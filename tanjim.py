def print_T():
    c = 't'
    for _ in range(3):
        print(c.ljust(30, c))
    for _ in range(9):
        print((c*6).center(30))

def print_A():
    c = "a"
    # top of A
    for i in range(1, 8, 2):
        print((c*i).center(30))
    #top gap of A
    for i in range(1, 5):
        print((((c*2) + " "*(2*i + 1) + (c*4)).center(30)))
    #middle of A
    print((c*17).center(30))
    #bottom gap
    for i in range(5, 8):
        print(((c*2) + " "*(2*i+3) + (c*4)).center(29))
    #bottom
    print(((c*4) + " "*15 + (c*7)).rjust(28))

def print_N():
    c = 'n'
    for i in range(12):
        print((c*4)+(" "*((i*2)//2))+(c*4)+(c*4).rjust(15-((i*2)//2)))

def print_J():
    c = 'j'
    for i in range(8):
        print((c*5).rjust(20))
    for i in range(3):
        print((c*(8-i)).rjust(8)+(""*7).center(7) + (c*(5-i)))
    print((c*13).rjust(17))

def print_I():
    c = "i"
    for i in range(2):
        print(c*25)
    for i in range(8):
        print((c*4).center(25))
    for i in range(2):
        print(c*25)

def print_M():
    c = 'm'
    for i in range(12):
        print((c*4)+(" "*((i*2)//2))+(c*4)+(" "*(11-((i*2)//2)))+(c*4).rjust(15-((i*2)//2))+(" "*((i*2)//2))+(c*4))

print_T()
print_A()
print_N()
print_J()
print_I()
print_M()