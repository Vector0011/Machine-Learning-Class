def new_paragraph(a,b):
    c = [a[i*b:min(i*b+b,len(a))] for i in range(0,len(a)//b+1)]
    s = ''
    for i in c:
        s+= i
        s+='\n'
    return s
if __name__ == "__main__":
    a = input()
    b = int(input())
    print(new_paragraph(a,b))