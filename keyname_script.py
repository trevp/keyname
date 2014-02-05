

from time import time
import os
import binascii
import subprocess
import math

def run_test(num_trials, max_iters, target_score, print_all=False):
	itersList = []
	print("num_trials = %d max_iters=%d target_score=%d" % (num_trials, max_iters, target_score))
	for x in range(num_trials):
		pseudokey = binascii.b2a_hex(os.urandom(16))
		cmd = subprocess.Popen(["./keyname", pseudokey, str(max_iters), str(target_score)], stdout=subprocess.PIPE)
		cmd_out, cmd_err = cmd.communicate()
		idx = cmd_out[:-1].rfind("\n")
		iters = int(cmd_out[idx+1:])
		itersList.append(iters)
		if print_all:
			print cmd_out
		else:
			print iters

run_test(1, 10000000, 17, print_all=True)
run_test(1, 10000000, 17, print_all=True)
run_test(1, 10000000, 17, print_all=True)

run_test(1, 100000000, 18, print_all=True)
run_test(1, 100000000, 18, print_all=True)
run_test(1, 100000000, 18, print_all=True)
