
class MyHashTable:
   def __init__(self):
       self.t = []

   def myHash(self,string):
    first_letter = string[0].lower()
    if first_letter == 'a':
        return 0
    if first_letter == 'b':
        return 1
    if first_letter == 'c':
        return 2
    if first_letter == 'd':
        return 3
    if first_letter == 'e':
        return 4
    if first_letter == 'f':
        return 5
    if first_letter == 'g':
        return 6
    if first_letter == 'h':
        return 7
    if first_letter == 'i':
        return 8
    if first_letter == 'j':
        return 9
    if first_letter == 'k':
        return 10
    if first_letter == 'l':
        return 11
    if first_letter == 'm':
        return 12
    if first_letter == 'n':
        return 13
    if first_letter == 'o':
        return 14
    if first_letter == 'p':
        return 15
    if first_letter == 'q':
        return 16
    if first_letter == 'r':
        return 17
    if first_letter == 's':
        return 18
    if first_letter == 't':
        return 19
    if first_letter == 'u':
        return 20
    if first_letter == 'v':
        return 21
    if first_letter == 'w':
        return 22
    if first_letter == 'x':
        return 23
    if first_letter == 'y':
        return 24
    if first_letter == 'z':
        return 25

   def myHashNum(self, stringNum):
       return stringNum[:3]

   def myHashNameCombo(self, name):
       nameArray = name.split(' ')
       product = 1
       for i in range(len(nameArray)):
           product *= self.myHash(nameArray[i])
       return product



something = MyHashTable()
print something.myHash('Abe')
print something.myHash('Hope')
print something.myHashNameCombo('Blake Jonathan Bagwell')
