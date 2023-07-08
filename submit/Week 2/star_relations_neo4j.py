from py2neo import Graph
from py2neo import Node,Relationship
import pandas as pd

graph = Graph('bolt://localhost:7687',auth=('neo4j','12345678'))
graph.delete_all()
node_stars = pd.read_csv('./data/star_infos_new2.csv')
# print(len(node_stars))
nodes = {}
for i in range(len(node_stars)):
    # print(node_stars.loc[i,'name'])
    node = Node('明星',name=node_stars.loc[i,'name'],image=node_stars.loc[i,'image'],homeland=node_stars.loc[i,'homeland'],weight=node_stars.loc[i,'weight'],birth=node_stars.loc[i,'birth'],baike_url=node_stars.loc[i,'baike_url'])
    graph.create(node)
    nodes[node_stars.loc[i,'name']] = node
# print(nodes)
path_stars = pd.read_csv('./data/all_star_relations.csv')
for i in range(len(path_stars)):
    relation = Relationship(nodes[path_stars.loc[i,'subject']],path_stars.loc[i,'relation'],nodes[path_stars.loc[i,'object']])
    graph.create(relation)
print('End...')