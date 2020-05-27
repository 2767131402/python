#!/usr/bin/python
# -*- coding:utf8 -*-

import pandas as pd
import numpy as np
import json

# 初始化数据
boolean = [True, False]
gender = ["男", "女"]
color = ["white", "black", "yellow"]
data = pd.DataFrame({
    "height": np.random.randint(150, 190, 100),
    "weight": np.random.randint(40, 90, 100),
    "smoker": [boolean[x] for x in np.random.randint(0, 2, 100)],
    "gender": [gender[x] for x in np.random.randint(0, 2, 100)],
    "age": np.random.randint(15, 90, 100),
    "color": [color[x] for x in np.random.randint(0, len(color), 100)],
    "data": [""""success":false,"statusCode":2000,"message":"系统异常，请联系管理员。","data":"哈哈哈"}""" for x in range(100)]
}
)
# 将 gender 男替换为1，女替换为0
data["gender"] = data["gender"].map({"男":1,"女":0})

#调用方法
def apply_age(x,param):
    return x+param
#以元组的方式传入额外的参数
data["age"] = data["age"].apply(apply_age,args=(-3,))

df1 = data[["height","weight","age"]].apply(np.sum, axis=0)

def BMI(series):
    weight = series["weight"]
    height = series["height"]/100
    BMI = weight/height**2
    return BMI

data["BMI"] = data.apply(BMI,axis=1)
print(data[["weight","height","BMI"]])


df = pd.DataFrame(
    {
        "A":np.random.randn(5),
        "B":np.random.randn(5),
        "C":np.random.randn(5),
        "D":np.random.randn(5),
        "E":np.random.randn(5),
    }
)
# 保留2位小数
df2 = df.applymap(lambda x: round(x,2))
print(df2)

print(type(data["BMI"]))