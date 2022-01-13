#!/bin/python3

# URL to retrive IP. Must contain global IP but no more
url = "http://ipecho.net/plain"
# File to save public to
ipfile = "myip"
# File to log to
logfile = "myip.log"
# Format string for logger
formatstr = "%(asctime)s %(levelno)s %(message)s"
# Log level for logger
loglevel = 1
# Path to git binary
gitpath = "/bin/git"
