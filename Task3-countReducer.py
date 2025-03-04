#!/usr/bin/env python3

import sys
import string

def main():
    cur_comp_id = None
    total_count = 0    
        
    for line in sys.stdin:
        line = line.strip()
        company_id, count = line.split("\t")
        
        try:
            count = int(count)
        except ValueError:
            continue
        
        if cur_comp_id == company_id:
            total_count += count
        else:
            if cur_comp_id:
                print(f'{cur_comp_id}\t{total_count}')
            cur_comp_id = company_id
            total_count = count

    if cur_comp_id:
        print(f'{cur_comp_id}\t{total_count}')
        
if __name__ == "__main__":
    main()