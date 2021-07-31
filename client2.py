import urllib.request

# HTTP level
fhand = urllib.request.urlopen('http://127.0.0.1:9000/romeo.txt')
# Print the file line by line
for line in fhand:
    print(line.decode().strip())

