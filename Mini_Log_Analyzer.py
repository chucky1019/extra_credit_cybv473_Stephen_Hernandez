# stephen Hernandez
#extra credit

from datetime import datetime
import random


def mini_log_analyzer():
    print("Welcome to Mini Log Analyzer")

    log_types = ["Information", "Warning", "Error"]
    log_messages = [

        "System started",
        "Connection established",
        "Connection lost",
        "User logged in",
        "User logged out",
        "Service restarted"
    ]

    logs = []

    how_many = int(input("How many log messages would you like? "))


    #make fake logs
    for i in range(how_many):
        time_now = datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")
        level = random.choice(log_types)
        message = random.choice(log_messages)

        line = f"{time_now} {level} {message}"
        logs.append(line)

    print("\nYour logs:")
    for l in logs:
        print(l)

    # counters
    info_total = 0
    warning_total = 0
    error_total = 0

    # count each type
    for entry in logs:
        if "Information" in entry:
            info_total += 1
        if "Warning" in entry:
            warning_total += 1
        if "Error" in entry:
            error_total += 1

    print("\nLog Results:")
    print("Information total:", info_total)
    print("Warning total:", warning_total)
    print("Error total:", error_total)




if __name__ == "__main__":
    mini_log_analyzer()
