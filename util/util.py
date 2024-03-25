#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""common.py"""
import csv
import getopt
import logging
import sys

def init():
    """init"""
    try:
        github_org = None
        github_token = None
        script = sys.argv[0]
        usage_text = (f"Usage: {script} "
                "-o <organization_name> -t <github_personal_token>")
        opts, _args = getopt.getopt(
            sys.argv[1:], "o:t:h", ["org=", "token=", "help"]
        )
        for opt, arg in opts:
            if opt in ("-o", "--org"):
                github_org = arg
            if opt in ("-t", "--token"):
                github_token = arg
            elif opt in ("-h", "--help"):
                logging.info(usage_text)
                sys.exit()
        if github_org is None:
            logging.info(usage_text)
            sys.exit()
        if github_token is None:
            logging.info(usage_text)
            sys.exit()
        return github_org, github_token
    except (getopt.GetoptError, IndexError) as exception:
        logging.error(exception)
        logging.info(usage_text)
        sys.exit(1)

