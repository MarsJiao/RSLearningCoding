# -*- encoding: UTF-8 -*-

import time
import datetime
import math

'''
    Author: Jiao Xu
'''

if __name__ == "__main__":
    start = time.clock()
    print("Started @ " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
########################################################################################################################
### 1. 用户相似度
    # 两两用户的余弦相似度
    def UserSimilarity(train):
        # 先构建倒排表
        item_users = dict()
        for u,items in train.items():
            for i in items.keys():
                if i not in item_users:
                    item_users = set()
                item_users[i].add(u)

        # 再计算用户u和v都评价过的商品
        C = dict()
        N = dict()
        for i, users in item_users.items():
            for u in users:
                N[u] += 1
                for v in users:
                    if

        # 最后计算用户相似矩阵W
