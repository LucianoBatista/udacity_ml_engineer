# writing modular code

# bad way (spagety code)

import numpy as np
import math
s = [88, 92, 79, 93, 85]
print(sum(s)/len(s))

s1 = []
for x in s:
    s1.append(x + 5)

print(sum(s1)/len(s1))

s2 = []
for x in s:
    s2.append(x + 10)

print(sum(s2)/len(s2))

s3 = []
for x in s:
    s3.append(x ** .5 * 10)

print(sum(s3)/len(s3))


# batter way

test_scores = [88, 92, 79, 93, 85]
print(np.mean(test_scores))

curved_5 = [score + 5 for score in test_scores]
print(np.mean(curved_5))

curved_10 = [score + 10 for score in test_scores]
print(np.mean(curved_10))

curved_sqrt = [math.sqrt(score) * 10 for score in test_scores]
print(np.mean(curved_sqrt))


# much better

def flat_curve(arr, n):
    return [i + n for i in arr]


def square_root_curve(arr):
    return [math.sqrt(i) * 10 for i in arr]


test_scores = [88, 92, 79, 93, 85]
curved_5 = flat_curve(test_scores, 5)
curved_10 = flat_curve(test_scores, 10)
curved_sqrt = square_root_curve(test_scores)

for score_list in test_scores, curved_5, curved_10, curved_sqrt:
    print(np.mean(score_list))
