import os
import yaml


def loadConfig():
    with open('./config.yaml') as f:
        data = yaml.safe_load(f)
        return data


