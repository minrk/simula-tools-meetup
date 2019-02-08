#!/usr/bin/env python3
import concurrent.futures
import requests
import threading
import time


thread_local = threading.local()


def get_session():
    if not getattr(thread_local, "session", None):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_site, sites)

# def download_site(url):
#     response = requests.get(url)
#     print(f"Read {len(response.content)} from {url}")


        


if __name__ == "__main__":
    sites = [
        "http://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
