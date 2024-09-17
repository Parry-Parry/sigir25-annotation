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

def to_qrels(file_name):
    print(file_name)
    with open(f'main/doccano/{file_name}.jsonl', 'r') as src, open(f'main/qrels/{file_name}-qrels.txt', 'w') as target:
        for l in src:
            l = json.loads(l)
            if len(l['label']) != 1:
                print(file_name, ':', l)
                continue
            else:
                #raise ValueError('Missing judgment')
                label = int(l['label'][0].split('(')[1].split(')')[0])
                target.write(f'{l["query_id"]} 0 {l["doc_id"]} {label}\n')
            
def to_ground_truth(file_name):

    with open(f'main/doccano/{file_name}.jsonl', 'r') as src, open(f'pilot-round-01/qrels/ground-truth-qrels.txt', 'w') as target:
        for l in src:
            l = json.loads(l)
            if len(l['label']) != 1:
                print(file_name, ':', l)
                continue
                #raise ValueError('Missing judgment')
            label = qrels[l['query_id']].get(l['doc_id'], 0)
            target.write(f'{l["query_id"]} 0 {l["doc_id"]} {label}\n')
            

if __name__ == '__main__':
    for f in ['harry-scells', 'froebe', 'guglielmo-faggioli', 'andrew-parry', 'ferdinand-schlatt', 'saber-zerhoudi', 'sean-macavaney', 'eugene-yang']: #glob('pilot-round-01/doccano/*.jsonl'):
        if not os.path.exists(f'main/doccano/{f}.jsonl'):
            print(f'main/doccano/{f}.jsonl does not exist')
            continue
        to_qrels(os.path.basename(f.split('.')[0]))


