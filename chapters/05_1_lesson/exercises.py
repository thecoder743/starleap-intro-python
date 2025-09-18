
##### Template for Chapter 5.14, Exercises 1 - 4 ######


print("********** Ch 5 Exercise 1 **********")

import time
time.time()

def time_since():
    import time
    s = 60
    m = 60
    h = 24
    t = time.time()
    days = int(t // s // m // h)
    hours = int(t // s // m)
    minutes = int(t // s)
    seconds = t
    print("days = ", days, "hours =", hours,  "minutes =", minutes,  "seconds =", seconds)


time_since()


print("********** Ch 5 Exercise 2 **********")

def check_fermat():
    A = input("what is the value of A? ")
    B = input("what is the value of B ")
    C = input("what is the value of C ")
    N = input("what is the value of N ")
    print(A, B, C, N)

check_fermat()
print("********** Ch 5 Exercise 3 **********")



# Do your work for Exercise 3 here.

print("Ch 5 Exercise 3: Not implemented") # Delete this line when you write your code!



print("********** Ch 5 Exercise 4 **********")

# Do your work for Exercise 4 here.

print("Ch 5 Exercise 4: Not implemented") # Delete this line when you write your code!
