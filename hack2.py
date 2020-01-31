list1 = ['Dacc', 'Dr. Singh', 'Tulsi Holistic Clinic', 'Qi Spine Clinic', 'Ajay Clinic', 'Dr. Saurabh Malhotra (Medan..', 'Dr. Rohit Sharma (Aarogya H..', 'Dr. Rohit Sharma (Goyal Hos..', 'Dr. Rohit Sharma (neuro-psy..', 'Dr. Rohit Sharma (Aarogya M..']
a = ""
b= " "
for i in range(0,len(list1)):
      a = list1[i]
      for j in range(0,len(a)):
          if a[j]=='(':
              break
          elif a[j]==" ":
              b=b+"-"
          else:
              b=b+a[j]
      list1[i]=b
      b = " "
print(list1)