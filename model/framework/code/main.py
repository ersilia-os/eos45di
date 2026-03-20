# imports
import os
import sys
import csv
import tempfile
import pandas as pd
from lazychemvis.transform import Pipeline

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))
checkpoints = os.path.join(root, "..", "..", "checkpoints")

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

with tempfile.TemporaryDirectory() as tmp_dir:
    pipe = Pipeline(lib_input=input_file, dir_path=checkpoints, output_path=tmp_dir, no_plots=True)
    pipe.run()
    df = pd.read_csv(os.path.join(tmp_dir, "coordinates.csv"))

# reindex by input order — missing molecules become NaN rows
df = df.set_index("smiles").reindex(smiles_list).reset_index(drop=True)

df.to_csv(output_file, index=False)
