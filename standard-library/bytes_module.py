# Create an empty bytes object i.e 4 bytes long
# It is not casting the integer
b = bytes(4)
print(b)

smileyBytes = bytes("🙄", "utf-8")
# print(smileyBytes)


decoded = smileyBytes.decode("utf-8")
# print(decoded)


# Bytearray is mutable
smileyBytesArray = bytearray("🙄", "utf-8")
# print(smileyBytesArray)


part = smileyBytesArray[3] = int("85", 16)
# print(part)

print(smileyBytesArray.decode("utf-8"))
