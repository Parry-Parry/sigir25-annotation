import pandas as pd
import pyterrier as pt 
if not pt.started(): pt.init()
import ir_datasets as irds
from ir_measures import *
from ir_measures import evaluator
from fire import Fire


def run_evaluator(run_file : str,
               ir_dataset : str, 
               output_dir : str,
               qrels_file : str = None,
               rel : int = 2,
               iterate : bool = False,
                ):
    metrics = [AP(rel=rel), NDCG(cutoff=10), NDCG(cutoff=5), NDCG(cutoff=1), R(rel=rel)@100, R(rel=rel)@1000, P(rel=rel, cutoff=10), RR(rel=rel), RR(rel=rel, cutoff=10)]
    run = pt.io.read_results(run_file)
    dataset = irds.load(ir_dataset)
    qrels = pt.io.read_qrels(qrels_file) if qrels_file else pd.DataFrame(dataset.qrels_iter())
    evaluate = evaluator(metrics, qrels)

    frame = []

    if iterate:
        for elt in evaluate.iter_calc(run):
            frame.append(
                        {
                            'name' : run_file,
                            'query_id' : elt.query_id,
                            'metric' : str(elt.measure),
                            'value' : elt.value,
                        }
                    )
    else:
        result = evaluate.calc_aggregate(run)
        result = {str(k) : v for k, v in result.items()}
        result['name'] = run_file 
        frame.append(result)
    
    frame = pd.DataFrame.from_records(frame)
    frame.to_json(output_dir, orient='records', lines=True)

if __name__ == "__main__":
    Fire(run_evaluator)