import queue
import time
import random

request_queue = queue.Queue()
request_id = 0

def generate_request():
    global request_id
    request_id += 1
    request = f"Request #{request_id}"
    request_queue.put(request)
    print(f"[+] Added: {request}")

def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"[-] Processing: {request}")
        # time imitation
        time.sleep(random.uniform(0.5, 1.5))
        print(f"[✓] Done: {request}")
    else:
        print("[!] Queue is empty.")

def main():
    try:
        while True:
            if random.choice([True, False]):
                generate_request()

            process_request()

            time.sleep(random.uniform(0.5, 1.0))

    except KeyboardInterrupt:
        print("\n[×] Buy-buy.")

if __name__ == "__main__":
    main()
