# Input format: a:1,b:2 and c:3,d:4

input1 = raw_input("Enter first dictionary (e.g., a:1,b:2): ")
input2 = raw_input("Enter second dictionary (e.g., c:3,d:4): ")

dict1 = dict(pair.split(":") for pair in input1.split(","))
dict2 = dict(pair.split(":") for pair in input2.split(","))

# Convert values to int
for k in dict1:
    dict1[k] = int(dict1[k])
for k in dict2:
    dict2[k] = int(dict2[k])

dict1.update(dict2)

print "Merged dictionary:", dict1

