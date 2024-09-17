#!/usr/bin/env python3
from glob import glob
import os
import json
import ir_datasets

dataset = ir_datasets.load('msmarco-passage/trec-dl-2019/judged')
qrels = {}
for qrel in dataset.qrels_iter():
    if qrel.query_id not in qrels:
        qrels[qrel.query_id] = {}
    qrels[qrel.query_id][qrel.doc_id] = qrel.relevance

dataset = ir_datasets.load('msmarco-passage/trec-dl-2020/judged')
for qrel in dataset.qrels_iter():
    if qrel.query_id not in qrels:
        qrels[qrel.query_id] = {}
    qrels[qrel.query_id][qrel.doc_id] = qrel.relevance

LOOKUP = {}

def to_qrels(file_name):

    print(file_name)
    with open(f'main/doccano/{file_name}.jsonl', 'r') as src:
        LOOKUP[file_name] = {
            'missing' : [], 
            'duplicates' : []
        }
        for i, l in enumerate(src):
            l = json.loads(l)
            if len(l['label']) < 1:
                LOOKUP[file_name]['missing'].append(i)
                continue
            if len(l['label']) > 1:
                LOOKUP[file_name]['duplicates'].append(i)
                #raise ValueError('Missing judgment')
            
if __name__ == '__main__':
    for f in ['harry-scells', 'froebe', 'guglielmo-faggioli', 'andrew-parry', 'ferdinand-schlatt', 'saber-zerhoudi', 'sean-macavaney', 'eugene-yang']: #glob('pilot-round-01/doccano/*.jsonl'):
        if not os.path.exists(f'main/doccano/{f}.jsonl'):
            print(f'main/doccano/{f}.jsonl does not exist')
            continue
        to_qrels(os.path.basename(f.split('.')[0]))
        for k, v in LOOKUP.items():
            print(k)
            print('missing:', v['missing'])
            print('duplicates:', v['duplicates'])
            print()
        print(LOOKUP)