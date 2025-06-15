
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

def print_B():
    c = "b"
    print((c*22))
    for i in range(2):
        print((c*4) + (c*4).rjust((18 + (i+1))))
    for i in range(3, 0, -1):
        print((c*4) + (c*4).rjust((18 + i)))
    print((c*22))
    for i in range(2):
        print((c*4) + (c*4).rjust((18 + (i+1))))
    for i in range(3, 0, -1):
        print((c*4) + (c*4).rjust((18 + i)))
    print((c*22))

def print_C():
    c = 'c'
    print((c*22).center(30))
    print(((c*4) + (" ") * 18 + (c*4)).center(30))
    for i in range(2):
        print((c*4) +  (" ") * (20 + i+1) + (c*4))
    for i in range(6):
        print((c*4))
    for i in range(2):
        print(((c*4) + (" ") * (21 - i*2) + (c*4)).center(30))
    print((c*22).center(30))

def print_D():
    c = 'd'
    for i in range(1, 4, 2):
        print((c*(20 + i)))
    for i in range(4):
        print((c*4) + (" ") * (17 + i) + (c*4))
    for i in range(4):
        print((c*4) + (" ") * (20 - i) + (c*4))
    for i in range(0, 3, 2):
        print((c*(23 - i)))

def print_E():
    c = "e"
    for _ in range(2):
        for _ in range(2):
            print((c*25))
        for _ in range(3):
            print((c*6))
    for _ in range(2):
            print((c*25))

def print_F():
    c = "f"
    for _ in range(2):
        for _ in range(2):
            print((c*25))
        for _ in range(3):
            print((c*6))
    for _ in range(3):
            print((c*6))

def print_G():
    c = "g"
    for i in range(2):
        print((c * (20 + i * 4)).center(30))
    for i in range(4):
        print((c*4))
    for i in range(4):
        print((c*4) + (c*(10 - i*2)).rjust(24))
    for i in range(2):
        print((c * (25 - i * 4)).center(30))

def print_H():
    c = "h"
    for i in range(5):
        print((c*4) + (c*4).rjust(21))
    for i in range(3):
        print((c*25))
    for i in range(6):
        print((c*4) + (c*4).rjust(21))

def print_I():
    c = "i"
    for i in range(2):
        print(c*25)
    for i in range(8):
        print((c*4).center(25))
    for i in range(2):
        print(c*25)

def print_J():
    c = 'j'
    for i in range(8):
        print((c*5).rjust(20))
    for i in range(3):
        print((c*(8-i)).rjust(8)+(""*7).center(7) + (c*(5-i)))
    print((c*13).rjust(17))

def print_K():
    c = "k"
    for i in range(6):
        print((c*5) + ("  ") * (5 - i) + (c*5))
    for i in range(6):
        print((c*5) + ("  ") * (0 + i) + (c*5))

def print_L():
    c = "l"
    for i in range(9):
        print(c*6)
    for i in range(3):
        print(c*25)

def print_M():
    c = 'm'
    for i in range(12):
        # print((c*4)+(" "*((i*2)//2))+(c*4)+(" "*(11-((i*2)//2)))+(c*4).rjust(15-((i*2)//2))+(" "*((i*2)//2))+(c*4))
        print((c*3) + (" ") * ( i) + (c*3) + (" ") * (22 - i*2) + (c*3) + (" ") * ( i) + (c*3)) # work same but easy to understand

def print_N():
    c = 'n'
    for i in range(12):
        print((c*4)+(" "*((i*2)//2))+(c*4)+(c*4).rjust(15-((i*2)//2)))

def print_O():
    c = "o"
    for i in range(1, -1, -1):
        print((c*(23 - i * 2)).center(29))
    for i in range(1, -1, -1):
        print(((c*4) + (" ") * (19 - i * 2)+ (c*4)).center(29))
    for i in range(4):
        print((c*4) + ((c*4)).rjust(25))
    for i in range(2):
        print(((c*4) + (" ") * (19 - i * 2)+ (c*4)).center(29))
    for i in range(2):
        print((c*(23 - i * 2)).center(29))

def print_P():
    c = "p"
    print((c*18))
    for i in range(2):
        print((c*4) + (c*3).rjust((15 + (i+1))))
    for i in range(3, 0, -1):
        print((c*4) + (c*3).rjust((15 + i)))
    print((c*18))
    for i in range(6):
        print((c*4))

def print_Q():
    c = "q"
    for i in range(1, -1, -1):
        print((c*(23 - i * 2)).center(29))
    for i in range(1, -1, -1):
        print(((c*4) + (" ") * (19 - i * 2)+ (c*4)).center(29))
    for i in range(4):
        if i == 3:
            print((c*4) + ((c*2) + (" ") * 4 + (c*4)).rjust(25))
        else:
            print((c*4) + ((c*4)).rjust(25))
    for i in range(2):
        print(((c*4) + (" ") * (16)+ (c*2) * ( 1 - i) + (" ") * (1)+ (c*4)).center(29))
    for i in range(2):
        print((c*(23 - i * 2) + (" ") * i).rjust(26) + ((" ") * (i*2)) + (" ")+ (c*2))

def print_R():
    c = 'r'
    print((c*18))
    for i in range(2):
        print((c*4) + (c*4).rjust((15 + (i+1))))
    for i in range(3, 0, -1):
        print((c*4) + (c*4).rjust((15 + i)))
    print((c*18))
    for i in range(5):
        print((c*4) + ("  ") * ( i) + (c*4) )

def print_S():
    c = "s"
    for i in range(2):
        print((c * (20 + i * 4)).center(30))
    for i in range(4):
        print((c*4) + (c*(10 - i*2 - 4)).rjust(24))
    print((c * (20 +4)).rjust(24))
    for i in range(3, -1 , -1):
        print((c*(10 - i*2 - 4))+(" ") * i * 2 + (c*4).rjust(22)  )
    for i in range(1, -1, -1):
        print((c * (20 + i * 4)).center(30))

def print_T():
    c = 't'
    for _ in range(3):
        print(c.ljust(30, c))
    for _ in range(9):
        print((c*6).center(30))

def print_U():
    c = "u"
    for i in range(8):
        print((c*4) + ((c*4)).rjust(25))
    for i in range(2):
        print(((c*4) + (" ") * (19 - i * 2)+ (c*4)).center(29))
    for i in range(2):
        print((c*(23 - i * 2)).center(29))

def print_V():
    c = "v"
    for i in range(12):
        print( (" ") * i+(c*4) + (" ") * (22 - (i*2))+ ((c*4)))

def print_W():
    c = "w"
    for i in range(12):
        print((c*3) + (" ") * (- i) + ((c*3).rjust(14 - i)) + ((c*3).rjust(3 + i))  + (" ") * (-i)+  ((c*3).rjust(14 - i)))

def print_X():
    c = 'x'
    for i in range(6):
        print(((c*5) + ("  ") * (9 - i * 2)+ (c*5)).center(30))
    for i in range(6, -1, -1):
        print(((c*5) + ("  ") * (11 - i * 2)+ (c*5)).center(30))

def print_Y():
    c = 'y'
    for i in range(6):
        print(((c*5) + ("  ") * (11 - i * 2)+ (c*5)).center(30))
    for i in range(6):
        print((c*4).center(30))

def print_Z():
    c = 'z'
    for i in range(2):
        print(c*25)
    for i in range(1, 9):
        print((c*7).rjust((25 - i*2)))
    for i in range(2):
        print(c*25)


name = (input("Enter your name: ")).lower()

for chr in name:
    if chr == 'a':
        print_A()
        print()
    elif chr == 'b':
        print_B()
        print()
    elif chr == 'c':
        print_C()
        print()
    elif chr == 'd':
        print_D()
        print()
    elif chr == 'e':
        print_E()
        print()
    elif chr == 'f':
        print_F()
        print()
    elif chr == 'g':
        print_G()
        print()
    elif chr == 'h':
        print_H()
        print()
    elif chr == 'i':
        print_I()
        print()
    elif chr == 'j':
        print_J()
        print()
    elif chr == 'k':
        print_K()
        print()
    elif chr == 'l':
        print_L()
        print()
    elif chr == 'm':
        print_M()
        print()
    elif chr == 'n':
        print_N()
        print()
    elif chr == 'o':
        print_O()
        print()
    elif chr == 'p':
        print_P()
        print()
    elif chr == 'q':
        print_Q()
        print()
    elif chr == 'r':
        print_R()
        print()
    elif chr == 's':
        print_S()
        print()
    elif chr == 't':
        print_T()
        print()
    elif chr == 'u':
        print_U()
        print()
    elif chr == 'v':
        print_V()
        print()
    elif chr == 'w':
        print_W()
        print()
    elif chr == 'x':
        print_X()
        print()
    elif chr == 'y':
        print_Y()
        print()
    elif chr == 'z':
        print_Z()
        print()
