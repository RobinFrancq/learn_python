from threading import Thread, current_thread

class MyThread(Thread):
    
    # overschrijven van run methode dat runt bij start()
    def run(self):
        i = 0
        print(current_thread().getName())
        while(i<=10):
            print(i)
            i+=1
            
t = MyThread()
t.start()