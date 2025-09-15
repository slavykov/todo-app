# user_input = input("Add a new member: ")

# file = open("../files/members.txt", "r")
# users_list = file.readlines()
# file.close()

# users_list.append(user_input)

# file = open("../files/members.txt", "w")
# file.writelines(users_list)
# file.close()

# filenames = ['doc.txt', 'report.txt', 'presentation.txt']

# for filename in filenames:
#     file = open(filename, "w")
#     file.write("Hello")
#     file.close()

filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    file = open(f"../files/{filename}", "r")
    print(file.read())
