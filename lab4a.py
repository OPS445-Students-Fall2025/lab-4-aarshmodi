#!/usr/bin/env python3
# Author ID: asmodi2

def join_sets(s1, s2):
    return s1 | s2

def match_sets(s1, s2):
    return s1 & s2

def diff_sets(s1, s2):
    return s1 ^ s2

if __name__ == '__main__':
    set1 = set(range(1,10))
    set2 = set(range(5,15))
    print('join:', join_sets(set1, set2))
    # etc.

