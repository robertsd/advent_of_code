import os

def input_data(year="2022", day="01"):
    with open(os.path.join(f"{year}","data", f"{day}.txt")) as f:
        return f.read()