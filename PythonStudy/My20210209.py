import sys
import threading
import time
def do(*args):
    for i in args:
        print("variable : {} ".format(i))

def do1(file):
    while True:
        #print("{}\n".format(sys.stdin.))
        #print(file.seekable())
        print(sys.stdin.buffer.read(1))
       # print("1\n")
        time.sleep(1)
    return

def main():
    print ("My20210209")
    do(2,5,30,50,1.4,"hell")

    mystdout = sys.stdout
    #mystdout.write("adadad")

    file = open("file.txt",mode='r+')

    file.readline()


    a=(mystdout,file)
    for i in a:
        i.write("HELLLLLL")
    
    t=threading.Thread(target=do1,args=(file,))
    t.start()

    aa= file.readline()
    print(aa)
    t.join()




