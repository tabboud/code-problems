#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Find Duplicate Files

Thoughts:
    - Traverse the filesystem and compute the hash of every file
    - Store the hash into a dictionary, this way we can detect duplicates as we go
TODO:
    - Determine which file is the original and which is the copy
"""
import os
import hashlib

def hash_file(filepath):
    """ Return an md5 hash the file at filepath
    """
    BLOCKSIZE = 65536
    hasher = hashlib.md5()
    with open(filepath, 'rb') as fp:
        buf = fp.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = fp.read(BLOCKSIZE)
    return hasher.hexdigest()


def find_duplicate_files(start_directory):
    """ Return a list of duplicate files
    """
    duplicate_files = []
    file_map = {}

    # Recursively traverse the filesystem starting at start_directoru
    # and compute the hash of every file while adding it to a dictionary
    for root, dirs, files in os.walk(start_directory):
        for filename in files:
            # create the path
            filepath = os.path.join(root, filename)
            # compute the hash of every file
            file_hash = hash_file(filepath)
            if file_hash in file_map:
                # check the times to determine which is the original
                cur_file_time = os.path.getmtime(filepath)
                stored_file_time = os.path.getmtime(file_map[file_hash])

                # Stored file is original
                if cur_file_time > stored_file_time:
                    duplicate_files.append((file_map[file_hash], filepath))
                else:
                    duplicate_files.append((filepath, file_map[file_hash]))
            else:
                file_map[file_hash] = filepath

    return duplicate_files


if __name__ == "__main__":
    directory = "files"
    duplicates = find_duplicate_files(directory)
    for duplicate in duplicates:
        print duplicate

