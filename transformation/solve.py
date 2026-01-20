enc = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸形㝦㘲捡㕽"
flag = "picoCTF{"

#print([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
#print(enc.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)]))
target = '形'
res = ""
for target in enc:
    for i in range(32,127):
        for j in range(32,127):
            if target == chr(( i << 8) + j):
               
               res_next = chr(i)
               res_next = res_next + chr(j)
               res = res + res_next
print(res)
