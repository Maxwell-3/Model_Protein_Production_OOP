from Model_Protein_Production_OOP import Environment, DNAstrand, RNAP
import Model_Protein_Production_OOP as mo
namespace 
import os
import numpy as np
from numpy import random as rand
import random
import scipy
import matplotlib.pyplot as plt
import timeit
import math
import time

env = Environment(30, pause_profile = "flat")
env.DNA.loading_list = mo.RNAP_loading_list(mo. uniform_promoter_time_list(mo.total_time, 50, 500), 1/mo.tau_loading)
env.start()