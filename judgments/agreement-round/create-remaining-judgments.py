#!/usr/bin/env python3
from glob import glob
import json

for i in glob('*.jsonl'):
    with open(i, 'r') as f:
        lines = []
        already_covered = {}
        already_labeled = {}
        for l in f:
            l = json.loads(l)

            if l['query_id'] not in already_covered:
                already_covered[l['query_id']] = set()

            if l['query_id'] not in already_labeled:
                already_labeled[l['query_id']] = set()

            if l['doc_id'] not in already_covered[l['query_id']]:
                lines.append(l)


            if len(l['label']) > 0:
                already_labeled[l['query_id']].add(l['doc_id'])

            already_covered[l['query_id']].add(l['doc_id'])
    remaining_lines = []

    for l in lines:
        if l['doc_id'] in already_labeled[l['query_id']]:
            continue
        remaining_lines.append(l)

    print(i, len(remaining_lines))
    if len(remaining_lines) > 0:
        with open(f'remaining/{i}', 'w') as f:
            for i in remaining_lines:
                f.write(json.dumps(i) + '\n')

