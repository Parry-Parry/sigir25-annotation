#!/usr/bin/env python3
from glob import glob
import os
import json
import ir_datasets

QREL_MAPPING = {"Highly Relevant (2)": 2, "Not Relevant (0)": 0, "Relevant (1)": 1, "Perfectly Relevant (3)": 3}

def to_qrels(file_name):
    print(file_name)
    with open(f'{file_name}.jsonl', 'r') as src, open(f'qrels/{file_name}-qrels.txt', 'w') as target:
        qrels = {}
        for l in src:
            l = json.loads(l)
            if not l['label'] or len(l['label'][0]) <= 0:
                continue
            if l['query_id'] not in qrels:
                qrels[l['query_id']] = {}
            if l['doc_id'] in qrels[l['query_id']]:
                continue

            qrels[l['query_id']][l['doc_id']] = QREL_MAPPING[l['label'][0]]
        for qid in qrels:
            for docno in qrels[qid]:
                target.write(f'{qid} 0 {docno} {qrels[qid][docno]}\n')

if __name__ == '__main__':
    for f in ['harry-scells', 'froebe', 'guglielmo-faggioli', 'andrew-parry', 'ferdinand-schlatt', 'saber-zerhoudi']:
        to_qrels(os.path.basename(f.split('.')[0]))
