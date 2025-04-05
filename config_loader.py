import json
import os

CONFIG_PATH = "config.json"

with open(CONFIG_PATH, 'r') as f:
    _CONFIG = json.load(f)

def get_config():
    return _CONFIG