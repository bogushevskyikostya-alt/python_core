#try:
   # number = float(input("Enter a number: "))
#except Exception:
    #print('Unknown error')
#except ValueError:
   # print('Incorrect value')

file= open(file_path,"a")

file.close()
file_path = "test.txt"

# file = open(file_path, "r")

# file.close()

# with open(file_path, 'a') as f:
#     print("File created successfully!")

# читання
with open("new_file.txt", 'r') as file:
    all_text = file.read(10)
    print(all_text)

with open("new_file.txt", 'r') as file:
    print(file.readline().strip())
    print(file.readline().strip())

with open("new_file.txt", 'r') as file:
    for line in file:
        print(line.strip())

with open("new_file.txt", 'r') as file:
    lines = file.readlines()
    print(lines)

    with open(file_path, 'a') as file:
    file.write("\nhello, this is line written by code!")
    file_path = "new_file.txt"
# запис
with open(file_path, 'w') as file:
    file.write("\nhello, this is line written by code!")
try:
    with open(file_path, 'x'):
        print('File created successfully!')
except FileExistsError:
    print('File is already exists!')