import json

from pathlib import Path

file = "details.txt"
filePath = Path("details.txt")
if filePath.is_file():
    open(file,"r+")
    passwords = json.load(open(file))
else:
    open(file,"w")
    passwords = {}
    print("This ")

class Credentials:
    """
    Class that generates new instances of details
    """

    user_details_list = []

    accounts = "details.txt"