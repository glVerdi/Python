myfile = open('filename.txt')

# Write mode
open('filename.txt', 'w')

# read mode
open('filename.txt', 'r')
open('filename.txt')

# binary write code
open('filename.txt', 'wb')

file = open('filename.txt', 'w')
# do stuff to the file
file.close()

file = open('filename.txt', 'r')
cont = file.read()
print(cont)
file.close()

file = open('filename.txt', 'r')
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()

file = open('filename.txt', 'r')
file.read()
print('Re-reading')
print(file.read())
print('Finished')
file.close()

file = open('filename.txt', 'r')
print(file.readlines())
file.close()

file = open('filename.txt', 'w')
file.write('This has been writen to a file')
file.close()
file = open('filename.txt', 'r')
print(file.read())
file.close()

file = open("filename.txt", "w")
file.write("Some new text")
file.close()
file = open("filename.txt", "r")
print("Reading new contents")
print(file.read())
print("Finished")
file.close()

msg = 'Hello World'
file = open('filename.txt', 'w')
amount_writen = file.write(msg)
print(amount_writen)
file.close

try:
    f = open('filename.txt')
    print(f.read())
finally:
    f.close()

with open('filename.txt') as f:
    print(f.read())