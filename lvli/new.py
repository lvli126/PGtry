from tqdm import tqdm
import pandas as pd
import numpy as np

data = pd.read_csv('hits.txt')
print(data['eventID'])
def process_edep(g):
    return (np.array(g['x']), np.array(g['y']), np.array(g['z']), np.array(g['energy']))

def process_state(g):
    return (np.array(g.iloc[0]['momX']), np.array(g.iloc[0]['momY']), np.array(g.iloc[0]['momZ'],np.array(g.iloc[0]['x']), np.array(g.iloc[0]['y']), np.array(g.iloc[0]['z']))

data = pandas.read_csv('HitsPara.txt', sep='\s+',header=0,)
data = data[data['particalID']==22]
data = data.groupby('eventID')
result = []
for e in tqdm(data.groups, ascii=True, leave=False):
#    result.append(process_state(data.get_group(e)))
    result.append(process_edep(data.get_group(e))
print(result)

#data = pandas.read_csv('hits.txt', sep='\s+',header=0,)
#result=process_run(data)
#np.save('new.npy',result)



