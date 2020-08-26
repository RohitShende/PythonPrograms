def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)


def f(n): return n*f(n-1) if n > 1 else 1     # one liner factorial program


print(fact(5))
print(f(5))


# anonymous functions (lambda functions) (functions without names)

double_the_number = lambda x: x * 2

print("\n", double_the_number(5))
