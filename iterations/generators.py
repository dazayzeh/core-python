"""
iterables defined by functions
lazy evaluation
can model sequences with no definite end
composable into pipelines

 ** Must include at least one yield statement (yield = return)
 ** Help preserve local states within a g-function
"""


def try_lazy_evaluation_with_generators():
    x = 2
    y = 3
    print('first print')
    yield x, y

    x, y = 0, x + y
    print('second print')
    yield x, y

    if StopIteration:
        print('evaluations is done')


g = try_lazy_evaluation_with_generators()
print(next(g))
print(next(g))
print(next(g))
