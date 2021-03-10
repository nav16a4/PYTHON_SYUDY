
class Class20210207:
    a=2


def main():
    x=bytearray(1)
    x[0]=1
    x.append(65)
    a=65535
   # x.append(a)
    print(x)
    y=a.to_bytes(2,"little")
    print(y)
    aaa = '가나다라마바사'.encode('ascii')

    print("Hello world!")




if __name__ =="__main__" :
    main()

def main20210207():
    print("Hello world!")
