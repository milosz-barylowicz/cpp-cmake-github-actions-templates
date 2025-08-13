#!/usr/bin/python3

import sys
import argparse
import subprocess

def parse_arguments():
    args_parser = argparse.ArgumentParser(description='Pass release informations')
    args_parser.add_argument('--release_version', '-r', type=str, required=True)
    args_parser.add_argument('--release_title', '-t', type=str, required=False)

    return args_parser.parse_args()

def create_branch(release_version):
    branch_name = "release/" + release_version
    is_branch_existing = subprocess.run(['git', 'ls-remote', '--heads', 'origin', branch_name], capture_output=True)

    if not is_branch_existing.stdout:
        print(f"Creating {branch_name} branch...")
        subprocess.run(['git', 'branch', branch_name])
        subprocess.run(['git', 'push', 'origin', '-u', branch_name])
    else:
        print(f"Branch {branch_name} already exists!")
        sys.exit()

def create_release(release_version, release_title):
    if release_title is not None:
        print("title")
        subprocess.run(['gh', 'release', 'create', 'v' + release_version, '--title', 'v' + release_version, ':', release_title, '--generate-notes'])
    else:
        subprocess.run(['gh', 'release', 'create', 'v' + release_version, '--title', 'v' + release_version, '--generate-notes'])

if __name__ == "__main__":
    parameters = parse_arguments()
    create_branch(parameters.release_version)
    create_release(parameters.release_version, parameters.release_title)
