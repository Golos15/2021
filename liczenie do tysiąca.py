import time

do_ilu = 1000

for x in range(0, do_ilu + 1):
    time.sleep(0.01)
    procent = round(float((x / do_ilu) * 100), 1)
    print (procent, "%", end="\r", flush=True)
