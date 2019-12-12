# -*- encoding: UTF-8 -*-

from surprise import SVD
from surprise import Dataset
from surprise import evaluate, print_perf
from surprise import Reader

# 载入movielens数据集
reader=Reader(line_format='user item rating timestamp',sep='::')
data = Dataset.load_from_file('../dataset/ml-1m/ratings.dat',reader=reader)
# k折交叉验证 k=3
data.split(n_folds=5)
# SVD矩阵分解
algo = SVD()
perf = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf)