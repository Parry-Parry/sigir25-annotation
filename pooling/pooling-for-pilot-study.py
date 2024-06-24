#!/usr/bin/env python3
#export IR_DATASETS_HOME=/mnt/ceph/tira/state/ir_datasets/
import ir_datasets
from trectools import TrecRun, TrecPoolMaker
from glob import glob
from tqdm import tqdm

queries = {
    'trec-dl-2019': {i.query_id: i.default_text() for i in ir_datasets.load("msmarco-passage/trec-dl-2019/judged").queries_iter()},
    'trec-dl-2020': {i.query_id: i.default_text() for i in ir_datasets.load("msmarco-passage/trec-dl-2019/judged").queries_iter()}
}

def all_runs(track):
    runs = []
    for r in tqdm(glob(f'runs/{track}/*'), f'Parse runs from {track}'):
        runs += [TrecRun(r)]
    return runs


for track in queries:
    runs = all_runs(track)
    print(len(runs))
