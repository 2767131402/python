from elasticsearch7 import Elasticsearch
import json

"""
Python 操作ES7 实现增删改查功能 
"""

# elasticsearch集群服务器的地址
ES = [
    '39.98.152.206:9200',
    '39.98.152.206:9201'
]

# 创建elasticsearch客户端
es = Elasticsearch(
    ES,
    # 启动前嗅探es集群服务器
    sniff_on_start=True,
    # es集群服务器结点连接异常时是否刷新es节点信息
    sniff_on_connection_fail=True,
    # 每60秒刷新节点信息
    sniffer_timeout=60
)

## 查询
query = {
    "query": {
        "match_all": {}
    }
}
## 返回的是字典
ret_query = es.search(index='item', body=query)
print(ret_query['hits'])

## 添加数据
doc = {
    "id": 2,
    "title": "坚果手机R1",
    "category": "锤子",
    "price": 3699.0,
    "images": "http://image.baidu.com/13123.jpg"
}
data = es.index(index='item', body=doc, id="123456")
print(data)

## 修改
doc = {
    "doc":{ ## 记得加上 doc
        "title": "坚果手机R1-修改"
    }
}
data = es.update(index="item",id="123456",body=doc)
print(data)

## 删除
data = es.delete(index='item', id="123456")
print(data)
