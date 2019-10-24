import constants as c


class ROBOT:
    def __init__(self, sim, wts):
        # /////////////////////////////////////////////////////////////////////
        # /////////////////////////////////////////////////////////////////////
        # body objects
        # /////////////////////////////////////////////////////////////////////
        # /////////////////////////////////////////////////////////////////////
        # ---------------------------------------------------------------------
        # main body
        body = sim.send_box(
            x=0,
            y=0,
            z=c.calf_length + c.thigh_radius,
            length=c.body_length,
            width=c.body_width,
            height=2 * c.body_height,
            mass=c.body_mass,
            r=0.5,
            g=0.5,
            b=0.5)
        # joint linkers, workaround for 2 DOF joints
        # assigned counter-clockwise, from the right bottom leg
        linkers = {
            0: sim.send_sphere(
                x=c.body_width/2,
                y=-c.body_length/2,
                z=c.calf_length + c.thigh_radius,
                radius=c.thigh_radius,
                mass=c.body_mass/10000,
                r=0.5,
                g=0.5,
                b=0.5),
            1: sim.send_sphere(
                x=c.body_width/2,
                y=0,
                z=c.calf_length + c.thigh_radius,
                radius=c.thigh_radius,
                mass=c.body_mass/10000,
                r=0.5,
                g=0.5,
                b=0.5),
            2: sim.send_sphere(
                x=c.body_width/2,
                y=c.body_length/2,
                z=c.calf_length + c.thigh_radius,
                radius=c.thigh_radius,
                mass=c.body_mass/10000,
                r=0.5,
                g=0.5,
                b=0.5),
            3: sim.send_sphere(
                x=-c.body_width/2,
                y=c.body_length/2,
                z=c.calf_length + c.thigh_radius,
                radius=c.thigh_radius,
                mass=c.body_mass/10000,
                r=0.5,
                g=0.5,
                b=0.5),
            4: sim.send_sphere(
                x=-c.body_width/2,
                y=0,
                z=c.calf_length + c.thigh_radius,
                radius=c.thigh_radius,
                mass=c.body_mass/10000,
                r=0.5,
                g=0.5,
                b=0.5),
            5: sim.send_sphere(
                x=-c.body_width/2,
                y=-c.body_length/2,
                z=c.calf_length + c.thigh_radius,
                radius=c.thigh_radius,
                mass=c.body_mass/10000,
                r=0.5,
                g=0.5,
                b=0.5)
        }
        # ---------------------------------------------------------------------
        # ---------------------------------------------------------------------
        # thighs
        # assigned counter-clockwise, from the right bottom leg
        thighs = {
            0: sim.send_cylinder(
                x=c.body_width/2 + c.thigh_length/2,
                y=-c.body_length/2,
                z=c.calf_length + c.thigh_radius,
                length=c.thigh_length,
                radius=c.thigh_radius,
                r1=1,
                r2=0,
                r3=0,
                r=0,
                g=0,
                b=1),
            1: sim.send_cylinder(
                x=c.body_width/2 + c.thigh_length/2,
                y=0,
                z=c.calf_length + c.thigh_radius,
                length=c.thigh_length,
                radius=c.thigh_radius,
                r1=1,
                r2=0,
                r3=0,
                r=0,
                g=1,
                b=0),
            2: sim.send_cylinder(
                x=c.body_width/2 + c.thigh_length/2,
                y=c.body_length/2,
                z=c.calf_length + c.thigh_radius,
                length=c.thigh_length,
                radius=c.thigh_radius,
                r1=1,
                r2=0,
                r3=0,
                r=0,
                g=1,
                b=1),
            3: sim.send_cylinder(
                x=-(c.body_width/2 + c.thigh_length/2),
                y=c.body_length/2,
                z=c.calf_length + c.thigh_radius,
                length=c.thigh_length,
                radius=c.thigh_radius,
                r1=1,
                r2=0,
                r3=0,
                r=1,
                g=0,
                b=0),
            4: sim.send_cylinder(
                x=-(c.body_width/2 + c.thigh_length/2),
                y=0,
                z=c.calf_length + c.thigh_radius,
                length=c.thigh_length,
                radius=c.thigh_radius,
                r1=1,
                r2=0,
                r3=0,
                r=1,
                g=0,
                b=1),
            5: sim.send_cylinder(
                x=-(c.body_width/2 + c.thigh_length/2),
                y=-c.body_length/2,
                z=c.calf_length + c.thigh_radius,
                length=c.thigh_length,
                radius=c.thigh_radius,
                r1=1,
                r2=0,
                r3=0,
                r=1,
                g=1,
                b=0)
        }
        # ---------------------------------------------------------------------
        # ---------------------------------------------------------------------
        # calves
        # assigned counter-clockwise, from the right bottom leg
        calves = {
            0: sim.send_cylinder(
                x=c.body_width/2 + c.thigh_length,
                y=-c.body_length/2,
                z=(c.calf_length + c.thigh_radius)/2,
                length=c.calf_length,
                radius=c.calf_radius,
                r1=0,
                r2=0,
                r3=1,
                r=0,
                g=0,
                b=1),
            1: sim.send_cylinder(
                x=c.body_width/2 + c.thigh_length,
                y=0,
                z=(c.calf_length + c.thigh_radius)/2,
                length=c.calf_length,
                radius=c.calf_radius,
                r1=0,
                r2=0,
                r3=1,
                r=0,
                g=1,
                b=0),
            2: sim.send_cylinder(
                x=c.body_width/2 + c.thigh_length,
                y=c.body_length/2,
                z=(c.calf_length + c.thigh_radius)/2,
                length=c.calf_length,
                radius=c.calf_radius,
                r1=0,
                r2=0,
                r3=1,
                r=0,
                g=1,
                b=1),
            3: sim.send_cylinder(
                x=-(c.body_width/2 + c.thigh_length),
                y=c.body_length/2,
                z=(c.calf_length + c.thigh_radius)/2,
                length=c.calf_length,
                radius=c.calf_radius,
                r1=0,
                r2=0,
                r3=1,
                r=1,
                g=0,
                b=0),
            4: sim.send_cylinder(
                x=-(c.body_width/2 + c.thigh_length),
                y=0,
                z=(c.calf_length + c.thigh_radius)/2,
                length=c.calf_length,
                radius=c.calf_radius,
                r1=0,
                r2=0,
                r3=1,
                r=1,
                g=0,
                b=1),
            5: sim.send_cylinder(
                x=-(c.body_width/2 + c.thigh_length),
                y=-c.body_length/2,
                z=(c.calf_length + c.thigh_radius)/2,
                length=c.calf_length,
                radius=c.calf_radius,
                r1=0,
                r2=0,
                r3=1,
                r=1,
                g=1,
                b=0)
        }
        # ---------------------------------------------------------------------
        # /////////////////////////////////////////////////////////////////////
        # /////////////////////////////////////////////////////////////////////

        # /////////////////////////////////////////////////////////////////////
        # /////////////////////////////////////////////////////////////////////
        # joints
        # /////////////////////////////////////////////////////////////////////
        # /////////////////////////////////////////////////////////////////////
        # ---------------------------------------------------------------------
        # body-thigh joints, horizontal direction
        # assigned counter-clockwise, from the right bottom leg
        body_thigh_joints_h = {
            0: sim.send_hinge_joint(
                first_body_id=body,
                second_body_id=linkers[0],
                x=c.body_width/2,
                y=-c.body_length/2,
                z=c.calf_length + c.thigh_radius,
                n1=0,
                n2=1,
                n3=0),
            1: sim.send_hinge_joint(
                first_body_id=body,
                second_body_id=linkers[1],
                x=c.body_width/2,
                y=0,
                z=c.calf_length + c.thigh_radius,
                n1=0,
                n2=1,
                n3=0),
            2: sim.send_hinge_joint(
                first_body_id=body,
                second_body_id=linkers[2],
                x=c.body_width/2,
                y=c.body_length/2,
                z=c.calf_length + c.thigh_radius,
                n1=0,
                n2=1,
                n3=0),
            3: sim.send_hinge_joint(
                first_body_id=body,
                second_body_id=linkers[3],
                x=-c.body_width/2,
                y=c.body_length/2,
                z=c.calf_length + c.thigh_radius,
                n1=0,
                n2=1,
                n3=0),
            4: sim.send_hinge_joint(
                first_body_id=body,
                second_body_id=linkers[4],
                x=-c.body_width/2,
                y=0,
                z=c.calf_length + c.thigh_radius,
                n1=0,
                n2=1,
                n3=0),
            5: sim.send_hinge_joint(
                first_body_id=body,
                second_body_id=linkers[5],
                x=-c.body_width/2,
                y=-c.body_length/2,
                z=c.calf_length + c.thigh_radius,
                n1=0,
                n2=1,
                n3=0)
        }
        # ---------------------------------------------------------------------
        # ---------------------------------------------------------------------
        # body-thigh joints, vertical direction
        # assigned counter-clockwise, from the right bottom leg
        body_thigh_joints_v = {
            0: sim.send_hinge_joint(
                first_body_id=linkers[0],
                second_body_id=thighs[0],
                x=c.body_width/2,
                y=-c.body_length/2,
                z=c.calf_length + c.thigh_radius,
                n1=0,
                n2=0,
                n3=1),
            1: sim.send_hinge_joint(
                first_body_id=linkers[1],
                second_body_id=thighs[1],
                x=c.body_width/2,
                y=0,
                z=c.calf_length + c.thigh_radius,
                n1=0,
                n2=0,
                n3=1),
            2: sim.send_hinge_joint(
                first_body_id=linkers[2],
                second_body_id=thighs[2],
                x=c.body_width/2,
                y=c.body_length/2,
                z=c.calf_length + c.thigh_radius,
                n1=0,
                n2=0,
                n3=1),
            3: sim.send_hinge_joint(
                first_body_id=linkers[3],
                second_body_id=thighs[3],
                x=-c.body_width/2,
                y=c.body_length/2,
                z=c.calf_length + c.thigh_radius,
                n1=0,
                n2=0,
                n3=1),
            4: sim.send_hinge_joint(
                first_body_id=linkers[4],
                second_body_id=thighs[4],
                x=-c.body_width/2,
                y=0,
                z=c.calf_length + c.thigh_radius,
                n1=0,
                n2=0,
                n3=1),
            5: sim.send_hinge_joint(
                first_body_id=linkers[5],
                second_body_id=thighs[5],
                x=-c.body_width/2,
                y=-c.body_length/2,
                z=c.calf_length + c.thigh_radius,
                n1=0,
                n2=0,
                n3=1)
        }
        # ---------------------------------------------------------------------
        # ---------------------------------------------------------------------
        # thigh-calf joints
        # assigned counter-clockwise, from the right bottom leg
        thigh_calf_joints = {
            0: sim.send_hinge_joint(
                first_body_id=thighs[0],
                second_body_id=calves[0],
                x=c.body_width/2 + c.thigh_length,
                y=-c.body_length/2,
                z=c.calf_length + c.thigh_radius,
                n1=0,
                n2=1,
                n3=0),
            1: sim.send_hinge_joint(
                first_body_id=thighs[1],
                second_body_id=calves[1],
                x=c.body_width/2 + c.thigh_length,
                y=0,
                z=c.calf_length + c.thigh_radius,
                n1=0,
                n2=1,
                n3=0),
            2: sim.send_hinge_joint(
                first_body_id=thighs[2],
                second_body_id=calves[2],
                x=c.body_width/2 + c.thigh_length,
                y=c.body_length/2,
                z=c.calf_length + c.thigh_radius,
                n1=0,
                n2=1,
                n3=0),
            3: sim.send_hinge_joint(
                first_body_id=thighs[3],
                second_body_id=calves[3],
                x=-(c.body_width/2 + c.thigh_length),
                y=c.body_length/2,
                z=c.calf_length + c.thigh_radius,
                n1=0,
                n2=1,
                n3=0),
            4: sim.send_hinge_joint(
                first_body_id=thighs[4],
                second_body_id=calves[4],
                x=-(c.body_width/2 + c.thigh_length),
                y=0,
                z=c.calf_length + c.thigh_radius,
                n1=0,
                n2=1,
                n3=0),
            5: sim.send_hinge_joint(
                first_body_id=thighs[5],
                second_body_id=calves[5],
                x=-(c.body_width/2 + c.thigh_length),
                y=-c.body_length/2,
                z=c.calf_length + c.thigh_radius,
                n1=0,
                n2=1,
                n3=0)
        }
        # ---------------------------------------------------------------------
        # ---------------------------------------------------------------------
        # sensors
        sensors = {}
        # touch sensors on calves
        # assigned counter-clockwise, from the right bottom leg
        for i in range(6):
            sensors[i] = sim.send_touch_sensor(body_id=calves[i])
        # proprioceptive sensor on main body
        sensors[6] = sim.send_position_sensor(body_id=body)
        # light sensor on main body, used for both control and evaluation
        self.light_sensor = sim.send_light_sensor(body_id=body)
        sensors[7] = self.light_sensor
        # ---------------------------------------------------------------------
        # /////////////////////////////////////////////////////////////////////
        # /////////////////////////////////////////////////////////////////////

        # /////////////////////////////////////////////////////////////////////
        # /////////////////////////////////////////////////////////////////////
        # neural network
        # /////////////////////////////////////////////////////////////////////
        # /////////////////////////////////////////////////////////////////////
        # ---------------------------------------------------------------------
        # check dimensions of the weight arrays in wts
        # wts = {
        #   'wtg_sn_h1': nparr(8, num_hidden1),
        #   'wtg_h1_h2': nparr(num_hidden1, 6),
        #   'wt[0-5]_in_h': nparr(num_local_hidden,),
        #   'wt[0-5]_h_mn': nparr(num_local_hidden, 3)
        # }
        # try:
        assert wts['wtg_sn_h1'].shape == (8, c.num_hidden1)
        assert wts['wtg_h1_h2'].shape == (c.num_hidden1, 6)
        for i in range(1, 7):
            in_h_key = c.pool[2*i]
            h_mn_key = c.pool[2*i+1]
            assert wts[in_h_key].shape == (c.num_local_hidden,)
            assert wts[h_mn_key].shape == (c.num_local_hidden, 3)
        # except AssertionError:
        #     print(wts)
        # ---------------------------------------------------------------------
        # ---------------------------------------------------------------------
        # global network
        # sensor neurons
        sensor_neurons = {}
        for i in sensors:
            sensor_neurons[i] = sim.send_sensor_neuron(sensor_id=sensors[i])
        # slow layer1 hidden neurons
        hidden1_neurons = {}
        for i in range(c.num_hidden1):
            hidden1_neurons[i] = sim.send_hidden_neuron()
        # slow layer2 hidden neurons
        hidden2_neurons = {}
        for i in range(6):
            hidden2_neurons[i] = sim.send_hidden_neuron()
        # global network synapses
        for sn in sensor_neurons:
            for h1 in hidden1_neurons:
                sim.send_synapse(source_neuron_id=sensor_neurons[sn],
                                 target_neuron_id=hidden1_neurons[h1],
                                 weight=wts['wtg_sn_h1'][sn, h1])
                for h2 in hidden2_neurons:
                    sim.send_synapse(source_neuron_id=hidden1_neurons[h1],
                                     target_neuron_id=hidden2_neurons[h2],
                                     weight=wts['wtg_h1_h2'][h1, h2])
        # ---------------------------------------------------------------------
        # local networks
        for leg in range(6):
            leg_motor_neurons = {
                0: sim.send_motor_neuron(joint_id=body_thigh_joints_h[leg]),
                1: sim.send_motor_neuron(joint_id=body_thigh_joints_v[leg]),
                2: sim.send_motor_neuron(joint_id=thigh_calf_joints[leg])
            }

            leg_hidden_neurons = {}
            for i in range(c.num_local_hidden):
                # FIXME: alpha?
                leg_hidden_neurons[i] = sim.send_hidden_neuron(tau=0.3)

            in_h_key = c.pool[2*(leg+1)]
            h_mn_key = c.pool[2*(leg+1)+1]
            for lh in leg_hidden_neurons:
                sim.send_synapse(source_neuron_id=hidden2_neurons[leg],
                                 target_neuron_id=leg_hidden_neurons[lh],
                                 weight=wts[in_h_key][lh])
                for lm in leg_motor_neurons:
                    sim.send_synapse(source_neuron_id=leg_hidden_neurons[lh],
                                     target_neuron_id=leg_motor_neurons[lm],
                                     weight=wts[h_mn_key][lh, lm])
        # ---------------------------------------------------------------------
        # /////////////////////////////////////////////////////////////////////
        # /////////////////////////////////////////////////////////////////////
