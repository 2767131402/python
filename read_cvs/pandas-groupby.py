#!/usr/bin/python
# -*- coding:utf8 -*-

import pandas as pd
import numpy as np

company=["A","B","C"]

data=pd.DataFrame({
    "company":[company[x] for x in np.random.randint(0,len(company),10)],
    "salary":np.random.randint(5,50,10),
    "age":np.random.randint(15,50,10)
}
)

# 分组
group = data.groupby("company").agg('mean')
print(type(group))
print(group)

print(data.groupby('company').agg({'salary':'median','age':'mean'}))

#新增一列avg_salary，代表员工所在的公司的平均薪水（相同公司的员工具有一样的平均薪水）
# 第一种方法
avg_salary_dict = data.groupby('company')['salary'].mean().to_dict()
data['avg_salary'] = data['company'].map(avg_salary_dict)
# 第二种方法
data['avg_salary1'] = data.groupby('company')['salary'].transform('mean')
print(data.sort_values(by=["avg_salary","salary"],ascending=[False,True]).reset_index(drop=True))