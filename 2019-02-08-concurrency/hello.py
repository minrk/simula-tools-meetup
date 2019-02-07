#!/usr/bin/env python3
import time

def sleep():
    print('Hello')
    time.sleep(3)
    print('World')

def main():
    for _ in range(3):
        sleep()

if __name__ == '__main__':
    start_time = time.time()
    main()
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
