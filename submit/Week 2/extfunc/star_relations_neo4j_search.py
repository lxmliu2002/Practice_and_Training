from py2neo import Graph

def find_related_relationships(node_name):
    # 连接到Neo4j数据库
    graph = Graph("bolt://localhost:7687", auth=('neo4j', '12345678'))

    # 构建查询语句
    cypher_query = (
        f"MATCH (n {{name: '{node_name}'}})-[r]-(related) "
        "RETURN r, related.name AS related_name"
    )
    
    result = graph.run(cypher_query)

    relationships = [(record["r"], record["related_name"]) for record in result]

    return relationships

node_name = input("请输入明星的姓名：")
related_relationships = find_related_relationships(node_name)

if related_relationships:
    print(f"{node_name} 相关的关系：")
    for relationship, related_name in related_relationships:
        print(f"关系：{relationship}")
        print(f"对方姓名：{related_name}")
        print("-" * 20)
else:
    print(f"{node_name} 没有找到相关的关系")
print('End...')