# CryoEM-GB-workflow-analysis
Analysis of workflow runs for the CryoEM-MD-AI Gordon Bell Submission

Analysis input files stored in: `/lambda_stor/homes/abrace/data/intelligent-resolution-cryoem-2022.tar.gz`


Runs in: `/global/cfs/cdirs/m1759/msalim/`

- production-thetagpu-0 : the first cross site run where we had big reservation on both systems, but ThetaGPU was lagging a lot
- perlmutter-production-final: the Thursday night run with only 1 GPU on Theta for AI; and 40 nodes going fast on Perlmutter (bottlenecked by tarring!)
- production-cross2: Friday morning's new run with 4 Theta nodes + 40 perlmutter (we think we fixed stuff)  
