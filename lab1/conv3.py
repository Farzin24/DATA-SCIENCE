data = raw_input("Enter comma-separated key:value pairs (e.g., a:1,b:2,c:3): ")
pairs = data.split(",")

tuple_data = []

for pair in pairs:
    key, value = pair.split(":")
    tuple_data.append((key, int(value)))

converted_dict = dict(tuple_data)
print "Converted dictionary:", converted_dict

