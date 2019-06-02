def check(a):
    b = ''.join(reversed(a))
    if a==b:
        return True
    else:
        return False
if __name__ == "__main__":
    print(check(input()))