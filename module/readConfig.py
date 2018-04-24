#import library
import configparser
import os


def read_config(cfg_files):
    if(cfg_files != None):
        config = configparser.ConfigParser()
        for i, cfg_file in enumerate(cfg_files):
            if(os.path.exists(cfg_file)):
                config.read(cfg_file)
        return config