#!/bin/env python
#coding:utf-8

'''
Project description:
====================
SGX publishes derivative data daily at the address below.

http://www.sgx.com/wps/portal/sgxweb/home/marketinfo/historical_data/derivatives/


Design a job to download the following files daily from the above website.
1) WEBPXTICK_DT-*.zip
2) TickData_structure.dat
3) TC_*.txt
4) TC_structure.dat


Requirements:
=============
1) It should be written in python and run like usual Linux commands, i.e. accepting command line options or even config file.
2) It should be able to download both historical files (files not on today) and today's file based on user's instructions.
3) Logging must be implemented.
   Use logging module provided by python, which can provide flexible logging configurations, e.g. some messages are logged to both stdout and file and some to file only.
   Make decisions on what messages/levels to log by yourself. The logs should help to debug/resolve issues.
4) The recovery plan should be considered. For example, you may ask yourself the following questions:
   If the downloading failed on one day or on some days how do you redownload the missed file(s)?
   Is the redownloading automatic or it requires manual intervention?
   The website only lists the recent files. Is it possible to download older files?
   Address any of your concerns in your design.
'''

import sys
import os
import datetime
import argparse
import logging.config
import requests
from bs4 import BeautifulSoup


BASE_URL = 'http://infopub.sgx.com/Apps?A=COW_Tickdownload_Content&B=TimeSalesData&F=%s&G=%s'


def parseArg():
    p = argparse.ArgumentParser()
    p.add_argument('--day', dest='day', type=int, default=0,
                    help='days before today')
    args = p.parse_args()
    return args


def cfgLogging():
    conf = {
            'version': 1,
            'disable_existing_loggers': True,
            'incremental': False,

            'formatters': {
            'detail': {
                    'format': '%(asctime)s %(name)s %(levelname)s [%(pathname)s:%(lineno)d] %(message)s'
                },
            },
            'handlers': {
                'console':{
                        'level':'INFO',
                        'class':'logging.StreamHandler',
                        'stream':sys.stderr,
                        'formatter': 'detail'
                    },
                    'file':{
                        'level':'DEBUG',
                        'class':'logging.handlers.RotatingFileHandler',
                        'filename': os.path.join(os.getcwd(), "run.log"),
                        'formatter': 'detail',
                        'maxBytes': 1024*1024*3,
                        'backupCount': 2,
                    },
            },

            'loggers': {
                'stdout': {
                    'handlers': ['console', 'file'],
                    'level': 'INFO',
                    'propagate': True,
                },
                'file': {
                    'handlers':['file'],
                    'level':'DEBUG',
                },
            },
    }
    logging.config.dictConfig(conf)


def downloadFile(fileUrl):
    pass


def parseHtml(data):
    pass


def crawler(day):
    today = datetime.datetime.now()
    realDay = today - datetime.timedelta(day)
    dateStr = realDay.strftime("%Y%m%d")

    stdLogger = logging.getLogger('stdout')
    fileLogger = logging.getLogger('file')

    headers = {
        'user-agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36",
    }

    ### method 1, not fully implemented
    # html = requests.get(URL, headers=headers)
    # # http://infopub.sgx.com/Apps?A=COW_Tickdownload_Content&B=TimeSalesData&F=4042&G=WEBPXTICK_DT-20180209.zip
    # bs = BeautifulSoup(html, 'html.parser')
    # stdLogger.info("bs = %s", bs)

    ### method 2,


def main():
    cfgLogging()
    args = parseArg()
    stdLogger = logging.getLogger('stdout')

    if args.day > 5:
        stdLogger.warn('day must be smaller then 6')
        return

    crawler(args.day)


if __name__ == "__main__":
    main()