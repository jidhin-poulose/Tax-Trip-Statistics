#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin:
        company_id, total_count = line.strip().split('\t')
        try:
            total_count = int(total_count)
        except ValueError:
            continue
        if total_count == 0:
            print(f"000\t{company_id}")
        if total_count < 10:
            print(f"00{total_count}\t{company_id}")
        elif total_count < 100:
            print(f"0{total_count}\t{company_id}")
        elif total_count < 1000:
            print(f"{total_count}\t{company_id}")
        
if __name__ == "__main__":
    main()