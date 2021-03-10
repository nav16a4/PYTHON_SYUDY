
def test(buffer :bytearray , size , data):
    buffer.extend(data.to_bytes(size,"little"))

def test1(buffer :bytearray , size , data : [int,float]):
    buffer.extend(data.to_bytes(size,"little"))
    buffer[0]=len(buffer)

def test2(buffer :bytearray , string : str):
    buffer.extend(string.encode())
    buffer[0]=len(buffer)
def test3(buffer :bytearray , string : bytes):
    buffer.extend(string)
    buffer[0]=len(buffer)


def main():
    buffer = bytearray((0,3,))
    print(buffer)
    test(buffer,4,255)
    test(buffer,2,255)
    print(buffer)
    print(len(buffer))

    buffer = bytearray((0,2))
     
    string = "abcdefg가나다라마바사"
    
    print(string.encode("utf-8"))
    print(string.encode("euc-kr"))

    test3(buffer,string.encode())
    print(buffer)
    print(len(buffer))






    return
 