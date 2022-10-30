listofnumbers= list(map(float, input("Enter a lot of number").split()))
numSearch=float(input("enter the number want to find"))
print("The numbers selected are: "+ str(listofnumbers)+ " " + " and the number you want to find is: " + str(numSearch))
numreAdd= float(input("The number you would like to replace"))
findme= False
indexElem= 0

"Find the number we want we would like to find and replace it by another"
for elem in listofnumbers:
    if elem == numSearch:
        findme=True
        elementPosition= indexElem
        listofnumbers[indexElem]=numreAdd
        break
    indexElem += 1
if findme== True:
    print("The number has been found and the position is: " + str(elementPosition)+ str(listofnumbers))
else:
    print("We didn't find the number")
