numb= input ("Enter the number you want")
numbSplit = numb.split()
listnumb = []
for n in numbSplit:
    listnumb.append(float(n))
print("the list of number entered is: " + str(listnumb))
numbSearch= float(input("Hit the number that you want to select"))
print ("The number hited is: " + str(numbSearch))
findme= False
for x in listnumb:
    if x == numbSearch:
        findme = True
        break
if findme ==True:
    print("the number searched exist")
else:
    print("doesn't exist")