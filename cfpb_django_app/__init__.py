#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import logging
import os
import sys


# Setup a logger
logging.debug('hi')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# This is a list of files in the skeleton that will be ignored
IGNORE=[
        '.git', 
        '.DS_Store',
]


def makedirs(path, dry=True):
    """ Wrap os.makedirs() in some general error-handling with dry-run
        support """

    if not dry:
        # Refuse to do anything if the destination already exists
        if os.path.exists(path):
            logger.debug('destination already exists at {}'.format(path))
            return False

        # Try to create the destination, if we can't, error out
        try:
            os.makedirs(path)
        except OSError as e:
            logger.debug('unable to create destination {}'.format(path))
            logger.debug(e)
            return False

    logger.debug('creating {}'.format(path))
    return True


def makeapp(name, url, version, template_dir, dest_dir, dry=True):
    """ Create the file structure for a new app with the given name,
        url, and version in the destination direcrory based on the 
        template directory."""

    # If we can't make the destination directory, bail 
    if not makedirs(dest_dir, dry=dry):
        logger.error('unable to create destination {}'.format(dest_dir))
        sys.exit(1)

    # String replacements for file contents
    replacements = {
            'app_name': name,
            'app_url': url,
            'app_version': version,
    }

    # Copy each path and file, and do the necessary text substitution
    for root, dirs, files in os.walk(template_dir):
        for filename in files:
            # If it's an ignorable file, skip it
            if filename in IGNORE: 
                continue

            # Get our source and destination paths
            source = os.path.join(root, filename)
            dest = source.replace(template_dir, dest_dir)

            # Replace 'app_name' in the dest string
            dest = dest.replace('app_name', name)

            makedirs(os.path.dirname(dest), dry=dry)
            
            logger.info('creating {}'.format(dest))

            if dry:
                continue

            with open(source, 'r', encoding='utf-8') as source_file, \
                    open(dest, 'w', encoding='utf-8') as dest_file:
                source_str = source_file.read()

                # Replace all our {{...}} varaibles
                for k, v in replacements.items():
                    source_str = source_str.replace('{{' + k + '}}', v)

                dest_file.write(source_str)


def main():
    parser = argparse.ArgumentParser(description='CFPB Django App')
    parser.add_argument('name', metavar='name', 
            help='Python-friendly app name')
    parser.add_argument('--url', default='http://cfpb.github.io/',
            help='url to the app project')
    parser.add_argument('--version', default='1.0', 
            help='initial app version')

    parser.add_argument('-t', '--template', 
            default=os.path.join(os.path.dirname(__file__), 'skel'),
            help='app template directory (default: skel/app_name)')
    parser.add_argument('-d', '--dest', default=os.getcwd(),
            help='destination path for the django app')
    parser.add_argument('-n', '--dry-run', action="store_true", 
            help='perform a dry run')
    # This is done by default... it might be nice if it's optional
    # parser.add_argument('-p', '--django-proj', default=False, type=bool,
    #         help='include a django project for local development')

    args = parser.parse_args()

    makeapp(args.name, args.url, args.version, args.template,
            args.dest, dry=args.dry_run)
    
    
if __name__ == "__main__":
    main()
