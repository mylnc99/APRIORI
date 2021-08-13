# -*- codeing = utf-8 -*-
# @Author : mylnc99
# @File : 宁浩导演最喜欢使用哪个演员.py
# @software: PyCharm

'''使用APrior算法计算宁浩导演最喜欢使用哪个演员'''


from efficient_apriori import apriori
import csv
director = u'宁浩'
file_name = './'+director+'_.csv'
lists = csv.reader(open(file_name, 'r', encoding='utf-8-sig'))

print(lists)# 数据加载

data = []
for names in lists:
     name_new = []
     for name in names:
           # 去掉演员数据中的空格
           name_new.append(name.strip())
     data.append(name_new[1:])

print(data)
#print(name_new)


# 挖掘频繁项集和关联规则
itemsets, rules = apriori(data, min_support=0.4,  min_confidence=1) #注意使用min_support=0.4，这个设置的太高就不会出结果，因此要多次尝试
print(itemsets)
print(rules)

