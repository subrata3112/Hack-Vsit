import re
list1 = ['Near G3S Cinema, R..\t\t\t\t|', 'VD Honda, Dwarka S..\t\t\t\t|', 'Chacha Bhaturewala..\t\t\t\t|', 'Club Road, Punjabi..\t\t\t\t|', 'Main Road, New Ash..\t\t\t\t|', 'Rajiv Chowk, Gurga..\t\t\t\t|', 'Vikas Marg, Chitra..\t\t\t\t|', 'Lajpat Rai Chowk, ..\t\t\t\t|', 'Block A, Dilshad G..\t\t\t\t|', 'Sector VI, Vaishal..\t\t\t\t|']
b=""
c=""
for i in range(0,len(list1)):
    b=list1[i]
    for j in range(0,len(b)):
        if b[j]=="," or b[j]==".":
            break
        else:
            c=c+b[j]
    list1[i]=c
    c=""
for i in range(0,len(list1)):
    b= list1[i]
    for j in range(0,len(b)):
        if b[j]==" ":
            c=c+"-"
        else:
            c=c+b[j]
    list1[i]=c
    c=""
print(list1)