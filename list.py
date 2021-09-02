protocolList = []
protocolList.append("ftp")
protocolList.append("ssh")
protocolList.append("https")
protocolList.append("smtp")
print(protocolList)

print()
position = protocolList.index("https")      #To access specific positions, we can use the index() method. 
print("https position" + str(position))

print()

protocolList.remove("ssh")                  #TO delete an element, we can use the remove() method:
print(protocolList)

print()

count = len(protocolList)
print("Protocol elements " +str(count))

print()

for protocol in protocolList:                #To print out the whole protocol list. Use for loop.
    print(protocol)

print()

protocolList.reverse()                       #Getting elements in a reverse way in the list through the reverse() method:
print(protocolList)

print()

toFine = "https"
found = False

for i in range (len(protocolList)):          #Searching elements in a list
    found = protocolList[i] == toFine
    if found:
        break
if found:
    print("Element found at index", i)
else:
    print("Element not found!")