import time
import RPi.GPIO as GPIO
pin = 11 # pin number in board mode
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()
GPIO.setup(pin, GPIO.OUT)
unit = 0.35 #seconds

def dot():
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(unit)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(unit) #pause between parts of the same letter

def dash():
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(3*unit)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(unit) #pause between parts of the same letter

def lp(): #pause between letters
    time.sleep(2*unit) # +1 from the pause between parts of the same letter = 3 units for pause between letters

def wp(): #pause between words
    time.sleep(6*unit) # +1 ~~
    
def A():
    dot()
    dash()
    lp()
    
def B():
    dash()
    dot()
    dot()
    dot()
    lp()
    
def C():
    dash()
    dot()
    dash()
    dot()
    lp()
    
def D():
    dash()
    dot()
    dot()
    lp()
    
def E():
    dot()
    lp()
    
def F():
    dot()
    dot()
    dash()
    dot()
    lp()
    
def G():
    dash()
    dash()
    dot()
    lp()
    
def H():
    dot()
    dot()
    dot()
    dot()
    lp()
    
def I():
    dot()
    dot()
    lp()
    
def J():
    dot()
    dash()
    dash()
    dash()
    lp()
    
def K():
    dash()
    dot()
    dash()
    lp()
    
def L():
    dot()
    dash()
    dot()
    dot()
    lp()
    
def M():
    dash()
    dash()
    lp()
    
def N():
    dash()
    dot()
    lp()
    
def O():
    dash()
    dash()
    dash()
    lp()
    
def P():
    dot()
    dash()
    dash()
    dot()
    lp()
    
def Q():
    dash()
    dash()
    dot()
    dash()
    lp()
    
def R():
    dot()
    dash()
    dot()
    lp()
    
def S():
    dot()
    dot()
    dot()
    lp()
    
def T():
    dash()
    lp()
    
def U():
    dot()
    dot()
    dash()
    lp()
    
def V():
    dot()
    dot()
    dot()
    dash()
    lp()
    
def W():
    dot()
    dash()
    dash()
    lp()
    
def X():
    dash()
    dot()
    dot()
    dash()
    lp()
    
def Y():
    dash()
    dot()
    dash()
    dash()
    lp()
    
def Z():
    dash()
    dash()
    dot()
    dot()
    lp()
    
def one():
    dot()
    dash()
    dash()
    dash()
    dash()
    lp()
    
def two():
    dot()
    dot()
    dash()
    dash()
    dash()
    lp()
    
def three():
    dot()
    dot()
    dot()
    dash()
    dash()
    lp()
    
def four():
    dot()
    dot()
    dot()
    dot()
    dash()
    lp()
    
def five():
    dot()
    dot()
    dot()
    dot()
    dot()
    lp()
    
def six():
    dash()
    dot()
    dot()
    dot()
    dot()
    lp()
    
def seven():
    dash()
    dash()
    dot()
    dot()
    dot()
    lp()
    
def eight():
    dash()
    dash()
    dash()
    dot()
    dot()
    lp()
    
def nine():
    dash()
    dash()
    dash()
    dash()
    dot()
    lp()
    
def zero():
    dash()
    dash()
    dash()
    dash()
    dash()
    lp()
    
print("Morse Code Blinker")
print("Before you run the program please make sure your diode is connected to the correct pin")
print("Please enter the message you'd like to blink")
print("Use letters , numbers , and space only")
text = input(": ")
count = 0
while count < len(text):
    for letter in str(text):
        
        if letter == 'A' or letter == 'a':
            A()
            count += 1
            continue
        if letter == 'B' or letter == 'b':
            B()
            count += 1
            continue
        if letter == 'C' or letter == 'c':
            C()
            count += 1
            continue
        if letter == 'D' or letter == 'd':
            D()
            count += 1
            continue
        if letter == 'E' or letter == 'e':
            E()
            count += 1
            continue
        if letter == 'F' or letter == 'f':
            F()
            count += 1
            continue
        if letter == 'G' or letter == 'g':
            G()
            count += 1
            continue
        if letter == 'H' or letter == 'h':
            H()
            count += 1
            continue
        if letter == 'I' or letter == 'i':
            I()
            count += 1
            continue
        if letter == 'J' or letter == 'j':
            J()
            count += 1
            continue
        if letter == 'K' or letter == 'k':
            K()
            count += 1
            continue
        if letter == 'L' or letter == 'l':
            L()
            count += 1
            continue
        if letter == 'M' or letter == 'm':
            M()
            count += 1
            continue
        if letter == 'N' or letter == 'n':
            N()
            count += 1
            continue
        if letter == 'O' or letter == 'o':
            O()
            count += 1
            continue
        if letter == 'P' or letter == 'p':
            P()
            count += 1
            continue
        if letter == 'Q' or letter == 'q':
            Q()
            count += 1
            continue
        if letter == 'R' or letter == 'r':
            R()
            count += 1
            continue
        if letter == 'S' or letter == 's':
            S()
            count += 1
            continue
        if letter == 'T' or letter == 't':
            T()
            count += 1
            continue
        if letter == 'U' or letter == 'u':
            U()
            count += 1
            continue
        if letter == 'V' or letter == 'v':
            V()
            count += 1
            continue
        if letter == 'W' or letter == 'w':
            W()
            count += 1
            continue
        if letter == 'X' or letter == 'x':
            X()
            count += 1
            continue
        if letter == 'Y' or letter == 'y':
            Y()
            count += 1
            continue
        if letter == 'Z' or letter == 'z':
            Z()
            count += 1
            continue
        if letter == '1':
            one()
            count += 1
            continue
        if letter == '2':
            two()
            count += 1
            continue
        if letter == '3':
            three()
            count += 1
            continue
        if letter == '4':
            four()
            count += 1
            continue
        if letter == '5':
            five()
            count += 1
            continue
        if letter == '6':
            six()
            count += 1
            continue
        if letter == '7':
            seven()
            count += 1
            continue
        if letter == '8':
            eight()
            count += 1
            continue
        if letter == '9':
            nine()
            count += 1
            continue
        if letter == '0':
            zero()
            count += 1
            continue
        if letter == ' ':
            wp()
            count += 1
            continue
        if letter == ',' or letter == '"' :
            count += 1
            continue
        if letter == '.':
            wp()
            count += 1
            continue
        else :
            count += 1
            continue
        
GPIO.cleanup()