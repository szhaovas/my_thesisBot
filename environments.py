import constants as c
import pyrosim
import math


class ENVs:
    def __init__(self, pb, pp):

        self.envs = {}

        for e in range(c.numEnvs):

            sim = pyrosim.Simulator(
                play_blind=pb,
                play_paused=pp,
                eval_time=c.evalTime)

            lightSource_angle = e / c.numEnvs * (2 * math.pi)

            lightSource = sim.send_box(
                x=c.lightSource_dist * math.cos(lightSource_angle),
                y=c.lightSource_dist * math.sin(lightSource_angle),
                z=c.lightSource_size / 2,
                length=c.lightSource_size,
                width=c.lightSource_size,
                height=c.lightSource_size,
                r=1,
                g=1,
                b=1)

            sim.send_light_source(body_id=lightSource)

            self.envs[e] = sim
