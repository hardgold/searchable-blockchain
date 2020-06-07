# !/usr/bin/python
# -*- coding: utf-8 -*-

from sklearn.cluster import KMeans
# simhash_list=[10000,10001,10011,10100,10101,10111,11000,11001,11010,11011,11100]
# sim_hash = [[10000,1],[10001,2],[10011,3],[10100,4],[10101,5],[10111,6],[11000,7],[11001,8],[11010,9],[11011,10],[11100,11]]
sim_hash = [[10000],[10001],[10011],[10100],[10101],[10111],[11000],[11001],[11010],[11011],[11100]]
sim_clu_number = KMeans(n_clusters = 4)
sim_clu_result = sim_clu_number.fit(sim_hash)
print(sim_clu_number.cluster_centers_)