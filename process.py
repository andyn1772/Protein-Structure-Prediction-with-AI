

"""
Secondary structure info downloaded from the PDB:
   https://www.rcsb.org/pages/download/http#ss

Secondary Structure Files

A FASTA-formatted file ("ss.txt.gz") with sequences and secondary structure information generated using DSSP is available:
https://cdn.rcsb.org/etl/kabschSander/ss.txt.gz (compressed)

A separate file, ss_dis.txt.gz, includes notation of regions which have not been experimentally observed, in addition to the secondary structure:
https://cdn.rcsb.org/etl/kabschSander/ss_dis.txt.gz (compressed)

"""

"""
Unzip ss.txt.gz; this script will process and extract a subset of the data
Creates three files, each with one line per protein:
  T = protein name; X = sequence data;  Y = structure data
"""


with open('ss.txt','r') as f: text  = f.read();

no_nl = text.replace('\n',"");

splt = no_nl.split('>')
splt = splt[1:]  # remove initial blank
m = int(len(splt)/2)

T,X,Y = [None]*m,[None]*m,[None]*m
for i in range(m):
  T[i] = splt[2*i][:4]
  X[i] = splt[2*i][15:]
  Y[i] = splt[2*i+1][13:]

with open('X.txt',"w") as f: f.writelines(x+"\n" for x in X[:500]);

with open('Y.txt',"w") as f: f.writelines(y+"\n" for y in Y[:500]);

with open('T.txt',"w") as f: f.writelines(t+"\n" for t in T[:500]);


