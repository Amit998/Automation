import string
import random
def passwordGenerator(length):
    psw=[]
    new=""
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    num=string.digits
    punch=string.punctuation
    li1=[char for char in s1]
    li2=[char for char in s2]
    li3=[char for char in num]
    li4=[char for char in punch]


    mutlist=[li1,li2,num,punch]
    # r=random.randrange(s1,s1)
    for i in range(length):
        pw=random.choice(random.choice(mutlist))
        psw.append(pw)
    for x in psw:
        new+=x
    print(new)




if __name__ == "__main__":
    print("Please Enter The Length")
    # length=int(input())
    length=10
    passwordGenerator(length)