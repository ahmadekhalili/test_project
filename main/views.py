from django.shortcuts import render

from datetime import datetime
import multiprocessing
import threading
import time

from .crawl import *


def akh(thread_id):
    print(f"[Thread-{thread_id}] started")
    time.sleep(1)
    print(f"[Thread-{thread_id}] finished")

def crawl(thread_id):
    driver = setup()
    driver.get("https://softgozar.com")
    print(driver.title)
    time.sleep(5)
    driver.quit()

def threads_run():
    threads = []
    for i in range(3):
        t = threading.Thread(target=crawl, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    print("[Process] All threads finished.")


def index(request):
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    request.session['datetime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    process = multiprocessing.Process(target=threads_run)
    process.start()
    print("[Main] Process started.")
    process.join()
    print("[Main] Process finished.")
    return render(request, 'main/index.html', {})


def test(request):
    return render(request, 'main/index.html', {})