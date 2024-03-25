#!/usr/bin/env python3
# -*- coding: utf_8 -*-
import requests
import logging

def list_repos(endpoint, org, token):
    """list repos"""
    repos = []
    endpoint_url = f'{endpoint}/orgs/{org}/repos?per_page=100'
    print(endpoint_url)
    while endpoint_url:
        response = requests.get(endpoint_url, headers={'Authorization': f'bearer {token}'})
        if response.status_code == 200:
            response_json = response.json()
            for repo in response_json:
                repos.append({'name': repo['name'], 'contributors_url': repo['contributors_url']})
            if 'next' in response.links:
                endpoint_url = response.links['next']['url']
            else:
                endpoint_url = None
        else:
            logging.error(f"Error: {response.status_code}")
            endpoint_url = None
    return repos

def get_contributors(repos, token):
    """get contributors"""
    contributors = []
    for repo in repos:
        contributors_url = repo['contributors_url']
        repo_name = repo['name']
        endpoint_url = f'{contributors_url}?anon=1&per_page=100'
        while endpoint_url:
            response = requests.get(endpoint_url, headers={'Authorization': f'bearer {token}'})
            if response.status_code == 200:
                response_json = response.json()
                for contributor in response_json:
                    contributors.append({'name': repo_name, 'contributor': contributor['login'], 'contributions': contributor['contributions']})
                if 'next' in response.links:
                    endpoint_url = response.links['next']['url']
                else:
                    endpoint_url = None
            elif response.status_code == 204:
                logging.info(f"Empty Repository: {repo_name}")
                endpoint_url = None
            else:
                logging.error(f"Error: {response.status_code}")
                endpoint_url = None
    return contributors
