input_list = [4, 54, 41, 0, 112, 32, 25, 49, 33, 3, 0, 0, 57, 32, 108, 23, 48, 4, 9, 70, 7, 110, 36, 8, 108, 7, 49, 10, 4, 86, 43, 106, 123, 89, 87, 18, 62, 47, 10 ,78]
key_str = 'J'

key_str = '_' + key_str

key_str = key_str + 'o'

key_str = key_str + '3'

key_str = 't' + key_str

print(key_str)

key_list = key_str

while len(input_list) > len(key_list):
    key_list = key_list + key_list
print(len(key_list))
res = ''

for i in range(0,len(input_list)):
    num = ord(key_list[i]) ^  input_list[i]
    res = res + chr(num)
print(res)

print(1 << 8)