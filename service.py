#!/bin/python3

import requests
import os
import subprocess
import logging
from sys import argv
from datetime import date

from settings import *

def main():
    logging.basicConfig(filename=logfile, level=loglevel, format=formatstr)
    subprocess.run([gitpath, "fetch"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run([gitpath, "pull"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    ip = requests.get(url).text
    os.chdir(os.path.sep.join(__file__.split(os.path.sep)[:-1]))
    try:
        with open("myip", "r") as f:
            old_ip = f.read()
    except Exception as e:
        old_ip = None
        logging.info("File {} not found. Creating it...".format(ipfile))
    if old_ip == ip:
        logging.info("New ip equals old ip, exiting...")
        return
    logging.info("New ip retrieved, writing to file")
    with open("myip", "w") as f:
        f.write(ip)
    f.close()
    logging.info("Commiting to git")
    subprocess.run([gitpath, "commit", ipfile, "-m", "\"Update ip to {} on {} \"".format(ip, date.today())], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    logging.info("Pushing to git")
    subprocess.run([gitpath, "push"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if __name__ == "__main__":
    main()
