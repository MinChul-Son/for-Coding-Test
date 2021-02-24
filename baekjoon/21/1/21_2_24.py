def main():
    b = input()
    if b.count('(') > b.count(')'):
        print('NO')
    else:
        print('YES')
    

if __name__=="__main__":
    main()