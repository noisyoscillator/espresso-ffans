"""
This sample illustrates how various observables of interest can be checkpointed.
"""
from __future__ import print_function
import espressomd
from espressomd import checkpointing
import numpy as np

checkpoint = checkpointing.Checkpoint(checkpoint_id="mycheckpoint")
checkpoint.load()

# print out actors

print("\n### current active actors ###")
for act in system.actors.active_actors:
    print(act)

# test user variable
print("\n### user variable test ###")
print("myvar = {}".format(myvar))

# test "system"
print("\n### system test ###")
print("system.time = {}".format(system.time))
print("system.box_l = {}".format(system.box_l))

# test "system.non_bonded_inter"
print("\n### system.non_bonded_inter test ###")
print("system.non_bonded_inter[0, 0].lennard_jones.get_params() = {}".format(system.non_bonded_inter[0, 0].lennard_jones.get_params()))

# test "system.part"
print("\n### system.part test ###")
print("system.part[:].pos = {}".format(system.part[:].pos))

# test "system.thermostat"
print("\n### system.thermostat test ###")
print("system.thermostat.get_state() = {}".format(system.thermostat.get_state()))

# test "p3m"
print("\n### p3m test ###")
print("p3m.get_params() = {}".format(p3m.get_params()))


# test registered objects
# all objects that are registered when writing a checkpoint are automatically registered after loading this checkpoint
print("\n### checkpoint register test ###")
print("checkpoint.get_registered_objects() = {}".format(checkpoint.get_registered_objects()))


# integrate system and finally save checkpoint
print("\n### Integrate until user presses ctrl+c ###")
print("Integrating...")

system.set_random_state_PRNG()
#system.seed = system.cell_system.get_state()['n_nodes'] * [1234]
np.random.seed(seed=system.seed)
while True:
    system.integrator.run(1000)
