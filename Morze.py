import RPi.GPIO as GPIO

def Morze_dot():
    GPIO.output(14, 0)
    time.sleep(0.2)
    GPIO.output(14, 1)
    time.sleep(0.2)
def Mozre_dash():
    GPIO.output(14, 1)
    time.sleep(0.9)
    GPIO.output(14, 0)
    time.sleep(0.3)
dot = Morze_dot()
dash = Mozre_dash()

Morze = {
A : dot dash time.sleep(3),
B : dash dot dot dot time.sleep(3),
W : dot dash dash time.sleep(3),
G : dash dash dot time.sleep(3),
D : dash dot dot time.sleep(3),
E : dot time.sleep(3),
V : dot dot dot dash time.sleep(3),
Z : dash dash dot dot time.sleep(3),
I : dot dot time.sleep(3),
J : dot dash dash dash time.sleep(3),
K : dash dot dash time.sleep(3),
L : dot dash dot dot time.sleep(3),
M : dash dash time.sleep(3),
N : dash dot time.sleep(3),
O : dash dash dash time.sleep(3),
P : dot dash dash dot time.sleep(3),
R : dot dash dot time.sleep(3),
S : dot dot dot time.sleep(3),
T : dash time.sleep(3),
U : dot dot dash time.sleep(3),
F : dot  dot dash dot time.sleep(3),
H : dot dot dot dot time.sleep(3),
C : dash dot dash dot time.sleep(3),
Q : dash dash dot dash time.sleep(3),
Y : dash dot dash dash time.sleep(3),
X : dash dot dot dash time.sleep(3),
}

s = input ()
print(s)
list (s)
for i in s:
    dict.get(i)