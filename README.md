# Re-Annotating TREC-DL-2019

Annotation project for Deep Learning Queries

# Project Structure

- `judgements`: contains all data for main annotation studies in TREC and original JSON format. We use Doccano for all annotation.
- `cross-annotator-narrative`: Contains judgements and code to replicate our fixed narrative setting
- `analysis` contains notebooks which can produce all figures in the work


# How to Add new Runs

Please add new runs into the directories `runs/trec-dl-2019` (for runs passage retrieval runs for the TREC 2019 Deep Learning track) respectively to `runs/trec-dl-2020` (for runs passage retrieval runs for the TREC 2020 Deep Learning track).

Please use a prefix to easily track who is the "maintainer" of a set of runs:

- `dl-19-official-...`: runs submitted to the 2019 edition of DL
- `dl-20-official-...`: runs submitted to the 2020 edition of DL
- `maik-froebe-...`: runs added by XX
- `colbert_...`: runs added by XX which re-rank colbert as first stage
- `tirex_...`: runs added by XX which re-rank the initial BM25 run from tirex as first stage
