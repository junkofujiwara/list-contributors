#!/usr/bin/env python3
# -*- coding: utf_8 -*-
import csv
import logging
import settings
import util.github as github
import util.util as util

def write_to_csv(contributors, filename):
    """write contributors to csv"""
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['name', 'contributor', 'contributions']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for contributor in contributors:
            writer.writerow(contributor)

def main():
    '''main function'''
    # set up logging
    logging.basicConfig(
        level = logging.INFO,
        format = "%(asctime)s [%(levelname)s] %(message)s",
        handlers = [
            logging.FileHandler("get-contributors.log"),
            logging.StreamHandler()
        ])
    
    # get repositories and contributors
    github_org, github_token = util.init()
    repos = github.list_repos(settings.API_ENDPOINT, github_org, github_token)
    logging.info(f"Found {len(repos)} repositories")
    contributors = github.get_contributors(repos, github_token)
    logging.info(f"Found {len(contributors)} contributors")
    write_to_csv(contributors, settings.OUTPUT_FILE)

if __name__ == "__main__":
    main()