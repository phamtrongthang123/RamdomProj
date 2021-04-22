# never, never never name the file `random.py`, it's the same name of the np module and it get conflicted for some reason.
import numpy as np

with open("inputfile.txt") as f:
    lines = f.readlines()
    p = int(lines[0])
    q = int(lines[1])
# p = 9
# q = 8  
n = p+q
prob_p = p/n
rng = np.random.default_rng(42)
print('data include number of sucess p = {}, failure q = {}, total n = {}, probability {}'.format(p,q,n,prob_p))
pred = rng.binomial(n=1, p=prob_p)
print('predict next is {}'.format(pred))
