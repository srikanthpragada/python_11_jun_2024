import threading


class PrintThread(threading.Thread):
    def run(self):
        for n in range(1, 50):
            print(f"Child : {n}")


print(threading.main_thread())
pt = PrintThread()
pt.start()
print(threading.active_count())
for n in range(1, 10):
    print(f"Main : {n}")
