# import library
import configparser
import os


def read_config(cfg_file):
    config = None
    if cfg_file is not None:
        config = configparser.ConfigParser()
        if os.path.exists(cfg_file):
            config.read(cfg_file)
    return config
