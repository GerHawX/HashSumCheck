import hashlib, sys

argument = sys.argv[1]
print(argument)


hashFunction = "sha512"
file = "fileToHash.txt"  # Location of the file (can be set a different way)
BLOCK_SIZE = 65536  # The size of each read from the file

# Create the hash object, can use something other than `.sha256()` if you wish
if hashFunction.lower() == "md5":
    file_hash = hashlib.md5()
elif hashFunction.lower() == "sha1":
    file_hash = hashlib.sha1()
elif hashFunction.lower() == "sha256":
    file_hash = hashlib.sha256()
elif hashFunction.lower() == "sha512":
    file_hash = hashlib.sha512()

with open(file, 'rb') as f:  # Open the file to read it's bytes
    fb = f.read(BLOCK_SIZE)  # Read from the file. Take in the amount declared above
    while len(fb) > 0:  # While there is still data being read from the file
        file_hash.update(fb)  # Update the hash
        fb = f.read(BLOCK_SIZE)  # Read the next block from the file

print(file_hash.hexdigest())  # Get the hexadecimal digest of the hash
