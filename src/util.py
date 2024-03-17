import threading

def create_threads(function_with_args):
    threads = []

    for functions, args in function_with_args:
        thread = threading.Thread(target=functions, args=args)
        threads.append(thread)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

