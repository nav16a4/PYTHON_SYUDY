import io
import sys
import time
import threading
import msvcrt
class MyClass:
    def __init__(self,fileobj):
        self.fileobj=fileobj
        self.buffer=io.StringIO()
    def readline(self):
        print("111111\n")
        buffer=bytearray()
        line=io.TextIOWrapper(buffer)
        print("line:{}".format(self.buffer.encoding()))
        if not line.endswith('\n'):
            print("2222222\n")
            line+=self.fileobj.readline()
            self.buffer=io.StringIO()
        return line
 #   def read(self):

class ConsoleIo:
     def __init__(self,stream=sys.stdout,set="utf-8"):
         self.stream=stream
         self.bytearray=bytearray()
         self.set=set
     def write(self,str):
         #동기화
         self.stream.write("\t\t[{}]\n".format(str))
         self.stream.write(self.bytearray.decode(self.set))
         return
     def read(self):
         flag=True
         while True==flag:
             char = msvcrt.getwche()
             if u'\r'==char:
                self.stream.write('\n')
                char=u'\0'
                flag=False
             self.bytearray.extend(char.encode(self.set))

         string="{}".format(self.bytearray.decode(self.set))
         self.bytearray.clear()
         return string


def do(test):
    while True:
        test.write("hello")
        time.sleep(3)

def main():
    test = ConsoleIo()
    t=threading.Thread(target=do,args=(test,))
    t.start()
    while True:
        test.write(test.read())  
        

    print("My20210210.py")




if __name__ =="__main__" :
    main()


