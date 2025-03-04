#!/usr/bin/env python3

import sys
import string

def main():
    for line in sys.stdin:
        company_id, count = line.strip().split("\t")
        print(f'{company_id}\t{count}')

if __name__ == "__main__":
    main()