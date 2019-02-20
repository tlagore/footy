import time
import requests
import os

def main():
    i = 8
    variable = os.environ.get("NAME")
    while i > 0:
        print(variable)
        time.sleep(1)
        i=i-1


if __name__ == "__main__":
    main()
