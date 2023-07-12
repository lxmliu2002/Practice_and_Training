import pandas as pd
from py2neo import Graph
import re
from tqdm import tqdm 

data = pd.read_csv('./data/star_infos_old.csv')
print(data['name'])

new_homeland = []
new_weight = []
new_birth = []
for i in tqdm(range (len(data)),total = len(data), desc='Searching'):
    info = re.findall(r"'.+?'",data['infos'][i])
    new_homeland.append(info[0].replace("'",''))
    new_weight.append(info[1].replace("'",''))
    new_birth.append(info[2].replace("'",''))
data['homeland'] = new_homeland
data['weight'] = new_weight
data['birth'] = new_birth
print(data[['homeland','weight','birth']])
data = data.drop(['infos'],axis=1)
data['baike_url'] = "https://baike.baidu.com/item/" + data['name']
print(data['baike_url'])
data = data.drop(['url'],axis=1)
data.to_csv('./data/star_infos_new.csv',index=False)