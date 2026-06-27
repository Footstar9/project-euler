permutations = {""}

def create_permutations(perm):
    new_perm= set()
    for x in perm:
            for i in range(10):
                if str(i) not in x:
                    new_perm.add(x + str(i))
    perm = new_perm
    return perm

for _ in range(10):
    permutations = create_permutations(permutations)
ordered = sorted(permutations)
print(ordered[10**6 - 1])