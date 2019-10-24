import numpy as np
import constants as c
from environments import ENVs
from robot import ROBOT


class INDIVIDUAL:
    def __init__(self, i):
        self.ID = i
        self.genome = {}
        self.genome['wtg_sn_h1'] = np.random.random((8, c.num_hidden1)) * 2 - 1
        self.genome['wtg_h1_h2'] = np.random.random((c.num_hidden1, 6)) * 2 - 1
        for i in range(1, 7):
            in_h_key = c.pool[2*i]
            h_mn_key = c.pool[2*i+1]
            self.genome[in_h_key] = np.random.random(
                (c.num_local_hidden,)) * 2 - 1
            self.genome[h_mn_key] = np.random.random(
                (c.num_local_hidden, 3)) * 2 - 1
        self.fitness = 0

    def Start_Evaluation(self, pb, pp):
        self.envs = ENVs(pb, pp).envs
        self.robots = {}
        for e in self.envs:
            self.robots[e] = ROBOT(self.envs[e], self.genome)
            self.envs[e].start()

    def Compute_Fitness(self):
        fitnessSum = 0
        for e in self.envs:
            self.envs[e].wait_to_finish()
            thisFitness = self.envs[e].get_sensor_data(
                sensor_id=self.robots[e].light_sensor)[-1]
            # if self.envs[e].get_sensor_data(
            #         sensor_id=self.robots[e].P4)[-1] < c.R:
            #     thisFitness = 0
            fitnessSum += thisFitness
        self.fitness = fitnessSum / c.numEnvs
        del self.envs
        del self.robots

    def Mutate(self):
        # FIXME: mutation strategy?
        target_wt = self.genome[np.random.choice(c.pool, p=c.weights)]

        target_r = np.random.randint(target_wt.shape[0])
        try:
            target_c = np.random.randint(target_wt.shape[1])
        except IndexError:
            target = target_wt[target_r]
            target_wt[target_r] = np.random.normal(target, abs(target))
            if target_wt[target_r] > 1:
                target_wt[target_r] = 1
            elif target_wt[target_r] < -1:
                target_wt[target_r] = -1
        else:
            target = target_wt[target_r, target_c]
            target_wt[target_r, target_c] = np.random.normal(
                target, abs(target))
            if target_wt[target_r, target_c] > 1:
                target_wt[target_r, target_c] = 1
            elif target_wt[target_r, target_c] < -1:
                target_wt[target_r, target_c] = -1

    def Print(self):
        print('[ID:', self.ID, ' ', 'Fitness:', self.fitness, ']', end=' ')
