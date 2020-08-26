print("##### With Break #####")
# With Break
for i in range(1, 10):
    if i == 5:
        break
    else:
        print(i)
    print("Executing for ", i)

print("\n\n##### With Continue #####")
# With Continue
for i in range(1, 10):
    if i == 5:
        continue
    else:
        print(i)
    print("Executing for ", i)

print("\n\n##### With Pass #####")
# With Pass
for i in range(1, 10):
    if i == 5:
        pass
        # Suppose we have a loop or a function that is not implemented yet,
        # but we want to implement it in the future.
        # They cannot have an empty body. The interpreter would complain.
        # So, we use the pass statement to construct a body that does nothing.
    else:
        print(i)
    print("Executing for ", i)

print("\n\n##### With Else #####")
# For with else
print("A for loop's else part runs if no break occurs. even if condition is false always")

for i in range(1, 10):
    if i == 5:
        break
    else:
        print(i)
    print("Executing for ", i)
else:
    print("No Breaks occurred")

print("\n\n")

for i in range(1, 10):
    if i == 10:
        break
    else:
        print(i)
    print("Executing for ", i)
else:
    print("No Breaks occurred")
