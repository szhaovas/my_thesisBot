import pickle
import constants as c
from population import POPULATION


class GENEALG:
    def __init__(self, play_back=False):
        if play_back:
            f = open('robot.p', 'rb')
            self.parent = pickle.load(f)
            f.close()
        else:
            self.parent = POPULATION(c.popSize)
            self.parent.Initialize()
            self.parent.Evaluate()

    def Evolve(self):
        for g in range(c.numGens):
            print(g, end=' ')
            self.parent.Print()
            child = POPULATION(c.popSize)
            child.Fill_From(self.parent)
            child.Evaluate()
            self.parent.ReplaceWith(child)

    def Show_Best(self):
        bestIndividual = self.parent.Best_Individual()
        self.parent.p[bestIndividual].Start_Evaluation(pb=False, pp=True)
        self.parent.p[bestIndividual].Compute_Fitness()
        print(self.parent.p[bestIndividual].fitness)

    def Save(self):
        f = open('robot.p', 'wb')
        pickle.dump(self.parent, f)
        f.close()
