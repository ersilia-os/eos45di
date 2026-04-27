# imports
import os
import sys
import csv
import tempfile
import numpy as np
import pandas as pd
from lazychemvis.transform import Pipeline
from ersilia_pack_utils.core import write_out, read_smiles

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))
checkpoints = os.path.join(root, "..", "..", "checkpoints")

# read SMILES from .csv file, assuming one column with header
cols, smiles_list = read_smiles(input_file)

with tempfile.TemporaryDirectory() as tmp_dir:
    pipe = Pipeline(lib_input=input_file, dir_path=checkpoints, output_path=tmp_dir, no_plots=True)
    pipe.run()
    df = pd.read_csv(os.path.join(tmp_dir, "coordinates.csv"))

# reindex by input order — missing molecules become NaN rows
df = df.set_index("smiles").reindex(smiles_list).reset_index(drop=True)

outputs = df.values.tolist()

# check input and output have the same length
assert len(smiles_list) == len(outputs)

headers = list(df.columns)
write_out(outputs, headers, output_file, np.float32)
