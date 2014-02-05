

from time import time
import os
import binascii
import subprocess
import math

def mean(dist):
        total = 0
        for element in dist:
                total += element
        return float(total) / float(len(dist))

def stddev(dist):
        avg = mean(dist)
        squared_deviations = []
        for element in dist:
                squared_deviations.append( abs((element - avg))**2 )
        return math.sqrt(mean(squared_deviations))

def run_test(num_trials, max_iters, target_score, print_all=False):
	itersList = []
	print("num_trials = %d max_iters=%d target_score=%d" % (num_trials, max_iters, target_score))
	for x in range(num_trials):
		pseudokey = binascii.b2a_hex(os.urandom(16))
		# os.system("./keyname %s %d %d" % (pseudokey, max_iters, target_score))
		cmd = subprocess.Popen(["./keyname", pseudokey, str(max_iters), str(target_score)], stdout=subprocess.PIPE)
		cmd_out, cmd_err = cmd.communicate()
		idx = cmd_out[:-1].rfind("\n")
		iters = int(cmd_out[idx+1:])
		itersList.append(iters)
		if print_all:
			print cmd_out
		else:
			print iters
	print("mean = %d, stddev=%d" % (mean(itersList), stddev(itersList)))


run_test(1, 1000000, 17, print_all=True)
