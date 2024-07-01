import argparse
from tot.methods.bfs import solve
from tot.tasks.navtree import NavTree

args = argparse.Namespace(backend='gpt-4o', temperature=0.7, task='navtree', naive_run=False, prompt_sample=None, method_generate='sample', method_evaluate='compare', method_select='greedy', n_generate_sample=1, n_evaluate_sample=2, n_select_sample=5)

task = NavTree()
ys, infos = solve(args, task, 900)
print(ys[0])
