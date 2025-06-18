

def print_A():
    c = "a"
    s = ' '
    # top of A
    for i in range(1, 7, 2):
        print((c*(i+2)).center(30))
    #top gap of A
    for i in range(1, 5):
        print((((c*2) + s*(2*i + 1) + (c*4)).center(30)))
    #middle of A
    print((c*17).center(30))
    #bottom gap
    for i in range(5, 8):
        print(((c*2) + s*(2*i+3) + (c*4)).center(30))
    #bottom
    print(((c*4) + s*15 + (c*7)).center(30))

def print_B():
    c = "b"
    s = " "
    print((c*22) + (s * 3))
    for i in range(2):
        print((c*4) + (c*4).rjust((18 + (i+1))) + s* ( 2 - i))
    for i in range(3, 0, -1):
        print((c*4) + (c*4).rjust((18 + i)) + s* ( 3 - i))
    print((c*22) + (s * 3))    
    for i in range(2):
        print((c*4) + (c*4).rjust((18 + (i+1))) + s* ( 2 - i))
    for i in range(3, 0, -1):
        print((c*4) + (c*4).rjust((18 + i)) + s* ( 3 - i))
    print((c*22) + (s * 3))

def print_C():
    c = 'c'
    s = " "
    print((c*22).center(30))
    print(((c*4) + s * 18 + (c*4)).center(30))
    for i in range(2):
        print((c*4) +  s * (20 + i+1) + (c*4) + s * (1-i))
    for i in range(6):
        print((c*4) + s*26)
    for i in range(2):
        print(((c*4) + s * (21 - i*2) + (c*4)).center(30))
    print((c*22).center(30))

def print_D():
    c = 'd'
    s = ' '
    for i in range(1, 4, 2):
        print((c*(20 + i) + s*(8 - i)))
    for i in range(4):
        print((c*4) + s * (17 + i) + (c*4) + s* (3 - i))
    for i in range(4):
        print((c*4) + s * (20 - i) + (c*4) + s* (i))
    for i in range(0, 3, 2):
        print((c*(23 - i) + s*(5+ i)))

def print_E():
    c = "e"
    s = " "
    for _ in range(2):
        for _ in range(2):
            print((c*25))
        for _ in range(3):
            print((c*6) + s*19)
    for _ in range(2):
            print((c*25))

def print_F():
    c = "f"
    s = " "
    for _ in range(2):
        for _ in range(2):
            print((c*25))
        for _ in range(3):
            print((c*6) + s*19)
    for _ in range(2):
            print((c*6) + s*19)

def print_G():
    c = "g"
    s = " "
    for i in range(2):
        print((c * (20 + i * 4)).center(30))
    for i in range(4):
        print((c*4) + s * 26)
    for i in range(4):
        print((c*4) + (c*(10 - i*2)).rjust(24) + s * 2)
    for i in range(2):
        print((c * (25 - i * 4)).center(30))

def print_H():
    c = "h"
    for i in range(5):
        print((c*4) + (c*4).rjust(21))
    for i in range(3):
        print((c*25))
    for i in range(5):
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
    s = " "
    for i in range(8):
        print((c*5).rjust(20))
    for i in range(3):
        print((c*(8-i)).rjust(8)+ s*7 + (c*(5-i)).ljust(5))
    print((c*13).rjust(17) + s*3)

def print_K():
    c = "k"
    s = " "
    for i in range(6):
        print((c*5) + s * (10 - i*2) + (c*5) + s *( i *2))
    for i in range(6):
        print((c*5) + s * i * 2 + (c*5) + s * (10 - (i*2)))

def print_L():
    c = "l"
    s = " "
    for i in range(9):
        print(c*6 + s*19)
    for i in range(3):
        print(c*25)

def print_M():
    c = 'm'
    s = " "
    for i in range(12):
        # print((c*4)+(" "*((i*2)//2))+(c*4)+(" "*(11-((i*2)//2)))+(c*4).rjust(15-((i*2)//2))+(" "*((i*2)//2))+(c*4))
        print((c*3) + s * ( i) + (c*3) + s * (22 - i*2) + (c*3) + s * ( i) + (c*3)) # work same but easy to understand

def print_N():
    c = 'n'
    s = " "
    for i in range(12):
        print((c*4)+(s*((i*2)//2))+(c*4)+(c*4).rjust(15-((i*2)//2)))

def print_O():
    c = "o"
    s = " "
    for i in range(1, -1, -1):
        print((c*(23 - i * 2)).center(29))
    for i in range(1, -1, -1):
        print(((c*4) + s * (19 - i * 2)+ (c*4)).center(29))
    for i in range(4):
        print((c*4) + ((c*4)).rjust(25))
    for i in range(2):
        print(((c*4) + s * (19 - i * 2)+ (c*4)).center(29))
    for i in range(2):
        print((c*(23 - i * 2)).center(29))

def print_P():
    c = "p"
    s = " "
    print((c*18) + s * 4)
    for i in range(2):
        print((c*4) + s * (13 + i) + (c*3) + s*(2-i))
    for i in range(3, 0, -1):
        print((c*4) + s * (15 - (3 - i)) + (c*3) + s * (3 - i))
    print((c*18) + s * 4)
    for i in range(6):
        print((c*4) + s * 18)

def print_Q():
    c = "q"
    s = ' '
    for i in range(1, -1, -1):
        print((c*(23 - i * 2)).center(29) + s * 2)
    for i in range(1, -1, -1):
        print(((c*4) + s * (19 - i * 2)+ (c*4)).center(29)+ s * 2)
    for i in range(4):
        if i == 3:
            print((c*4) + ((c*2) + s * 4 + (c*4)).rjust(25)+ s * 2)
        else:
            print((c*4) + ((c*4)).rjust(25)+ s * 2)
    for i in range(2):
        print(((c*4) + s * (16)+ (c*2) * ( 1 - i) + s * (1)+ (c*4)).center(29)+ s * 2)
    for i in range(2):
        print((c*(23 - i * 2) + s * i).rjust(26) + (s * (i*2)) + s+ (c*2)+ s * (2-(i*2)))

def print_R():
    c = 'r'
    s = " "
    print((c*18) + s * 4)
    for i in range(2):
        print((c*4) + s * (12 + i)+ (c*4) + s * (2 -i))
    for i in range(3, 0, -1):
        print((c*4) + s * (14 - (3-i))+ (c*4) + s *(3 - i))
    print((c*18) + s * 4)
    for i in range(6):
        print((c*4) + ("  ") * ( i) + (c*4) + s * (14 - (i*2)) )

def print_S():
    c = "s"
    s = ' '
    for i in range(2):
        print(s * (5 - (i*3)) + (c * (20 + i * 4)) + s* (3 -i))
    for i in range(4):
        print((c*4) + (c*(10 - i*2 - 4)).rjust(24))
    print((c * (20 +4)) + s * 4)
    for i in range(3, -1 , -1):
        print((c*(10 - i*2 - 4))+(" ") * i * 2 + (c*4).rjust(22)  )
    for i in range(1, -1, -1):
        print((s * (3 + (1 - i) * 2) + c * (20 + i * 4) + s * (3-(i*2))))

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
    s = ' '
    for i in range(12):
        print( s * i+(c*4) + s * (22 - (i*2))+ ((c*4)) + s * i)

def print_W():
    c = "w"
    s = " "
    for i in range(12):
        print((c*3) + s * (- i) + ((c*3).rjust(14 - i)) + ((c*3).rjust(3 + i))  + s * (-i)+  ((c*3).rjust(14 - i)) + s * i)

def print_X():
    c = 'x'
    s = "  "
    for i in range(5):
        print(((c*5) + s * (9 - i * 2)+ (c*5)).center(30))
    for i in range(6, -1, -1):
        print(((c*5) + s * (9 - i * 2)+ (c*5)).center(30))

def print_Y():
    c = 'y'
    for i in range(6):
        print(((c*5) + ("  ") * (9 - i * 2)+ (c*5)).center(30))
    for i in range(6):
        print((c*4).center(30))

def print_Z():
    c = 'z'
    for i in range(2):
        print(c*25)
    for i in range(1, 9):
        print((c*7).rjust((25 - i*2)) + (" ") * (i *2))
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
