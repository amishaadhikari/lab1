data = {}
for i in range(5):
    name = input(f"Enter name {i+1}: ")
    age = int(input(f"Enter age: "))
    data[name] = age
print(data)
search_name = input("Enter a name to search: ")
if search_name in data:
    print(f"Age ='{search_name}' is: {data[search_name]}")
else:
    print(f"Name '{search_name}' not found in the dictionary.")
