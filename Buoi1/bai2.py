a = [a for a in open("path.txt").read().split('\n')]
b = [b.split('/')[-1] for b in a ]
r = '[\n' 
for i in range(len(a)):
    r += '\t{\n\t\t"path": "'+a[i]+'",\n\t\t"file_name": "'+b[i]+'"\n\t},\n'
r = r[0:-2]
r += '\n]'
output = open("path.json", "w")
output.write(r)
output.close()