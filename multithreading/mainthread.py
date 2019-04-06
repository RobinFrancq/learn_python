import threading

print("Current Thread that is running: " +str(threading.current_thread().getName()))

# Checken of dit de mainthread is
if isinstance(threading.current_thread(), threading._MainThread):
    print("Main Thread")
else:
    print("Some other thread") 