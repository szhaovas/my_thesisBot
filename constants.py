# FIXME: mass distribution?
# robot body parameters
body_mass = 1.0
body_length = 0.5
body_width = 0.25
body_height = 0.02
thigh_length = 0.1
thigh_radius = 0.02
calf_length = 0.1
calf_radius = 0.02

# robot network parameters
num_hidden1 = 4
num_local_hidden = 2
# pool and weights for mutation and indexing
num_total = 14*num_hidden1 + 24*num_local_hidden
pool = ['wtg_sn_h1', 'wtg_h1_h2']
for i in range(0, 6):
    in_h_key = 'wt'+str(i)+'_in_h'
    h_mn_key = 'wt'+str(i)+'_h_mn'
    pool.append(in_h_key)
    pool.append(h_mn_key)
weights = [8*num_hidden1/num_total, num_hidden1*6/num_total]
for i in range(0, 6):
    weights.append(num_local_hidden/num_total)
    weights.append(num_local_hidden*3/num_total)

# environment parameters
lightSource_size = 0.5
lightSource_dist = 3
numEnvs = 4

# evolution parameters
evalTime = 300
popSize = 10
numGens = 1
