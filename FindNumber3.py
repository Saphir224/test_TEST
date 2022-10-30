numbwant= input("Enter the numbers do you want")
numbwantSplit= numbwant.split()
listOfnumber=list(map(float, numbwantSplit))
print(listOfnumber)
numblook= float(input("Enter the number you will want to find: "))
print(numblook)

"To find the number in the list of element and return the index of this element"

findme= False 
indexlist= 0
for elem in listOfnumber:
    if elem==numblook:
        findme=True
        elemPosition= indexlist
        break
    indexlist= indexlist +1
if findme==True:
    print ("we found the element" + "and the index of element is: "+ str(elemPosition))
else:
    print ("we didn't find the number you would like to find in the list")