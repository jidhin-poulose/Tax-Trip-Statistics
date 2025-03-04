#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin:
        total_count, company_id = line.strip().split('\t')
        try:
            total_count = int(total_count)
        except ValueError:
            continue
        print(f'{company_id}\t{int(total_count)}')
        
if __name__ == "__main__":
    main()