import os
import json

with open(os.environ["GITHUB_EVENT_PATH"], "r") as event_file:
    print(event_file.read())