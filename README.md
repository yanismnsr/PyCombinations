# The package
combinations is a package used to generate all possible combinations of a given length `k` 
on a given set. The set is given as a list, and `k` must be equal to 0 or positive. 

# Usage examples 

## With integers 
```python
from combs import combinations

l = [89,32,6,7]
k = 2
combs = combinations.find_combinations(l, k)
print(combs)
```
Output :
```
[[89, 32], [89, 6], [89, 7], [32, 6], [32, 7], [6, 7]]
```

## With strings
```python
from combs import combinations

l = ["github", "gitlab", "azuredevops", "svn"]
k = 3
combs = combinations.find_combinations(l, k)
print(combs)
```

Output :
```
[['github', 'gitlab', 'azuredevops'], ['github', 'gitlab', 'svn'], ['github', 'azuredevops', 'svn'], ['gitlab', 'azuredevops', 'svn']]
```