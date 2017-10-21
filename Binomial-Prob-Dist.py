# Evan Douglass
# Binomial Probability Distribution

# This program computes a binomial probability distribution and
# sums the probabilities of a given range of random variables.
# It also has the option of plotting a histogram of the data.

import math
import matplotlib.pyplot as plt

def main():
    # get constants
    p = 0.50          # probability of success
    q = 1 - p         # probability of failure
    n = 50            # total number in trial
    x = range(20, 31) # random variable range of interest

    # output the probability distribution
    dist = probDist(p, q, n)
    print('Probability Distribuiton')
    for var, prob in dist:
        print('{:^12d}{:.5f}'.format(var, prob))
    print()

    # output x range probability sum
    print('The probability of x from', x[0], 'to', x[-1], 'is',
            format(sumX(dist, x), '.5f'))
    print()

    # if user wants a histogram, display it
    if ask():
        histogram(dist)

# compute the binomial probability distribution for each value of x in n
# return a list of tuples in the form (variable, probability)
def probDist(p, q, n):
    dist = list()
    for var in range(n+1):
        prob = nCr(n, var) * (p ** var) * (q ** (n - var))
        dist.append((var, prob))
    return dist

# compute the sum of a range of random variables in the distribution
def sumX(lst, rnge):
    return sum(prob for _, prob in lst[rnge[0]:rnge[-1]+1])

# plot a histogram of the probability distribution
def histogram(lst):
    # split arrays in lst into seperate lists
    varbs = list()
    probs = list()
    for var, prob in lst:
        varbs.append(var)
        probs.append(prob)

    # set up histogram
    plt.bar(varbs, probs, width=1, align='center', edgecolor='black')
    plt.title('Probability Distribution')
    plt.xlabel('Random Variable')
    plt.ylabel('Probability')

    # display histogram
    plt.show()

# compute a combination of given values for n and r
def nCr(n, r):
    return math.factorial(n) / ((math.factorial(n - r) * math.factorial(r)))

# ask user if they want to see a histogram of the data
# return a boolean value
def ask():
    choice = input('Do you want to see a histogram? ')
    choice = choice.lower()
    if choice == '':
        return False
    elif choice not in 'yes':
        return False
    else:
        return True

main()
