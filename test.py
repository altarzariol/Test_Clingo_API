import clingo
import sys

ctl = clingo.Control()
ctl.load(sys.argv[1])
ctl.ground([("base", [])])
ctl.configuration.solve.models = 1
ctl.configuration.solver.rand_freq = "0.5"
ctl.configuration.solver.seed = 2
ctl.configuration.solver.sign_def = "rnd"

# find a random solution and store the assignment of atoms in answer_set
with ctl.solve(yield_=True, async_=True) as handle:
	for model in handle:
		answer_set = [(atom,True) for atom in model.symbols(atoms=True)]
		answer_set.extend([(atom,False) for atom in model.symbols(atoms=True,complement=True)])
		print("Solution to ignore:")
		print(model)

# search for all solutions, starting from a different seed
ctl.configuration.solve.models = 0
ctl.configuration.solver.seed = 23

num_of_solutions = 0
with ctl.solve(yield_=True, async_=True) as handle:
	for model in handle:
		if num_of_solutions < 1:
			print("\nFirst model found (it has to be different from the one to ignore):")
			print(model)
			model.context.add_nogood(answer_set)
		num_of_solutions += 1

print("\nNumber of returned solutions: {}/24".format(num_of_solutions))
