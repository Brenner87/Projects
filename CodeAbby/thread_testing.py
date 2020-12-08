import concurrent.futures
import threading
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleep {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done sleeping...{seconds}'



#t1 = threading.Thread(target=do_something)
#t2 = threading.Thread(target=do_something)

#t1.start()
#t2.start()

#t1.join()
#t2.join()

# do_something()
# do_something()

#


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)
    # results = [executor.submit(do_something, sec) for sec in secs]
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())



#    f1 = executor.submit(do_something, 1)
#    f2 = executor.submit(do_something, 1)
#    print(f1.result())
#    print(f2.result())

finish = time.perf_counter()
print(f'Finished in {round(finish - start, 2)} second(s)')