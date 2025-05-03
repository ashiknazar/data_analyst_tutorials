from datetime import datetime

with open("log.txt", "a") as file:
    file.write(f"{datetime.now()}\n")
