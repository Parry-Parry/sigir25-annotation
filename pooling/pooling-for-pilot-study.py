#!/usr/bin/env python3
#export IR_DATASETS_HOME=/mnt/ceph/tira/state/ir_datasets/
import ir_datasets
import pandas as pd
from trectools import TrecRun, TrecPoolMaker
from glob import glob
from tqdm import tqdm
import random

queries = {
    'trec-dl-2019': {i.query_id: i.default_text() for i in ir_datasets.load("msmarco-passage/trec-dl-2019/judged").queries_iter()},
    'trec-dl-2020': {i.query_id: i.default_text() for i in ir_datasets.load("msmarco-passage/trec-dl-2019/judged").queries_iter()}
}

docsstore = ir_datasets.load("msmarco-passage").docs_store()

def all_runs(track):
    runs = []
    for r in tqdm(glob(f'runs/{track}/*'), f'Parse runs from {track}'):
        runs += [TrecRun(r)]
    return runs

ret = []

for track in queries:
    runs = all_runs(track)
    pool = TrecPoolMaker().make_pool(runs, strategy="topX", topX=10).pool
    
    # select 5 random judged queries
    queries_pool = list(set([i for i in pool.keys() if i in queries[track]]))
    random.seed(42)
    random.shuffle(queries_pool)
    queries_pool = queries_pool[:5]


    for q in queries_pool:
        #select random 10 documents
        docs = sorted(list(pool[q]))
        random.seed(42)
        random.shuffle(docs)
        docs = docs[:10]

        for d in docs:
            ret += [{
                'text': docsstore.get(d).default_text(),
                'query': queries[track][str(q)],
                'doc_id': d,
                'query_id': str(q),
                'label': [],
            }]

pd.DataFrame(ret).to_json(f'pooling/pool-pilot-study.jsonl', lines=True, orient='records')

