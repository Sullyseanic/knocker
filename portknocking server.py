# import time
import subprocess
import select
position = 0
print("test0 OK")


def scanlogs():
    f = subprocess.Popen(['tail', '-F', "logpath here"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p = select.poll()
    p.register(f.stdout)
    x = 0
    while x <= 6:
        x = x + 1
        if p.poll(1):
            new_logsnip = f.stdout.readline()  # instead of print it could be reading lines from this as a variable
        else:
            print("test3 OK")


def checknock():
    print("test4 OK")
        #open text file

        #compare contens of log to


while True:
    scanlogs()
    print("test6 OK")
