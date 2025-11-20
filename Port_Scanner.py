import random

import random


def Port_Scanner():
    print("Port Scanner")

    host = input("Enter Host: ")
    start_port = int(input("Enter Start Port: "))
    end_port = int(input("Enter End Port: "))
    fast_mode = input("Fast mode? (y/n): ").strip().lower()

    ports = list(range(start_port, end_port + 1))

    # Fast mode: skip every other port
    if fast_mode == "y":
        ports = ports[::2]

    print("\nPorts Scanned")
    print("No | Port | Status")
    print("--------------------")

    for i, port in enumerate(ports, start=1):
        status = random.choice(["open", "closed"])
        print(f"{i:>3} | {port:<4} | {status}")

    input("\nPress Enter to continue...")


if __name__ == "__main__":
    Port_Scanner()


