from simplex_method import SimplexMethod

sm = SimplexMethod()
sm.load_problem('problem.txt')
answer = sm.get_solution()
print(answer)