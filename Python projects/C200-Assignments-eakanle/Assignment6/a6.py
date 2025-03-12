import math
import random as rn
import numpy as np
import matplotlib.pyplot as plt
import os 
import csv


print(os.getcwd())

# PROBLEM ONE

data = []
#INPUT path and filename
#OUTPUT list of parent, child pairs
#CONSTRAINT use csv reader
def get_data(path, filename):
    pass


#input parent name
#output children
#constraint using comprehension
def get_child(name):
    for parent, child in data:
        if parent == name:
            return child



#input parent name
#output true if has children
#constraint using comprehension
def has_children(name):
    pass

#input child name
#output parent of child
#constraint using comprehension
def get_parent(name):
    pass


#input child name1, child name2
#output true if children have same parent
#constraint using comprehension
def siblings(name1,name2):
    pass
 
 
#input grandparent name1, grandchild name2
#output true if name1 is grandparent to name2
#constraint using comprehension 
def grandparent(name1, name2):
    pass

#input nothing
#output all names
#constraint list comprehension only
def get_all():
    pass

#input name1, name2
#output true if name1 and name 2 are cousins, i.e., have the same grandparents
def cousins(name1,name2):
    pass


# Problem 2
# input n: total space (size), v: tiles and 
# output all possible patterns where the tiles add exactly to the the space (n)
def tiles(n, v, lst):       
    if not bool(lst):
        return []
    else:
        n_t, n_s = [], []
        for sub in lst: 
            for i in v:
                if sum(sub) + i == n:
                    n_t.append(sub + [i])
                
                elif sum(sub) + i < n:
                    n_s.append(sub + [i])
        
        n_t += tiles(n, v, n_s) 
        return n_t



#problem 3
# input: a list of numbers
# output: a pair containing the sum and boolean vector (see PDF for sample output)
def max_adjacent(lst):
    max_sum = 0
    max_indices = []
    
    for i in range(len(lst)):
        current_sum = lst[i]
        current_indices = [0] * len(lst)
        current_indices[i] = 1

        for j in range(i + 1, len(lst)):
            current_sum += lst[j]
            current_indices[j] = 1
            
            if current_sum > max_sum:
                max_sum = current_sum
                max_indices = current_indices[:]
    
    return [max_sum, max_indices]



########################
# PROBLEM 4
########################


# INPUT path and filename (payrollwins.txt)
# OUTPUT payroll and number of wins as a list
# Ouptut example: [[209,89], [139,74]]
# CONSTRAINT use csv reader
def get_data_1(path, filename):
    datapoints = []
    with open(path + filename, 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            line = line.split(",")
            list = [int(line[0]), int(line[1])]
            datapoints. append (list)
    print (datapoints)
    return datapoints
        


#INPUT data points (x0,y0),...,(xn,yn)
#OUTPUT best regression slope m_hat, intercept b_hat, and R_sq
def std_linear_regression(data):
    def r(data,f) :
        return sum([f(x,y) for x,y in data])

    n = len(data)
    xy_p = r(data,lambda x,y: x*y)
    x_s = r (data, lambda x,y: x)   
    y_s = r(data, lambda x, y: y)
    x_sq = r(data, lambda x, y: x**2)

    S_xy = (xy_p - ((x_s * y_s) / n))
    S_xx = x_sq - ((x_s**2) / n)

    m = round (S_xy / S_xx, 3)
    b = round (((y_s - (m * x_s)) / n), 3)

    y_sq = r(data, lambda x, y: y**2)

    SST = y_sq - ( (y_s**2) / n)
    SSE = y_sq - (b * y_s) - (m * xy_p)

    R_sq = round(((SST - SSE) / SST) , 3)
    
    return (m, round(b, 3), round(R_sq, 3))




#### Problem 5

# INPUT path and filename (fish_data.txt)
# OUTPUT two separate lists, first one containing the age and second containing 
# the length as given in the fish_data.txt file 
# Ouptut example: [1,2,3, ...], [4.8, 8.8, 8.0, ...]
# CONSTRAINT use csv reader
# make sure to get rid of the first line that just contains the column names (we don't want that)
def get_fish_data(path, name):
    dir = ''
    named = "fish_data.txt"
    
    with open(dir + named, 'r') as file:
        view = csv.reader(file)
        next (view)
        
        a = []
        l = []
        
        for item in view:
            a.append(int(item[0]))
            l.append(float(item[1]))
    
    return a, l


#INPUT lists X values, Y values of data and degree of the polynomial
#RETURN a polynomial of degree three
def make_function(X,Y,degree):
    result = np.polyfit(X, Y, degree)
    return np.poly1d(result)    



#### Problem 6
#input string and positive integer n
#output a list of the longest string that have no more than n distinct symbols

def max_n(str, n):
    
    r = {}
    
    def count_L(array): return len(list(set(array)))
    
    for i in range(len(str)):
        
        for g in range(i + 1, len(str) + 1):
            
            if len(str[i:g]) in r:
                if str[i:g] in r == False:
                    flag = False
            else:
                flag = True
            if count_L(str[i:g]) - n and count_L(str[i:g]) > 0 and flag:
                if len(str[i:g]) in r:
                    r[len(str[i:g])].append(str[i:g])
                else:
                    r[len(str[i:g])] = []
                    r[len(str[i:g])].append(str[i:g])
    if len(r.keys()) == 0:
        return ['']
    else:
        return r[max(r.keys())]    



#problem 7

#input a tuple of model parameters, second parameter is the number of trials
#output the percent success rounded to two decimal places
def simulation(model_parameters, num_trials):
    pass




if __name__ == '__main__':
    
    # uncomment to test
    # Before sbmitting to the Autograder: 
    # Make sure to comment the code for plotting graph in P4 and also the import of matplotlib on the top of this file
    # You can use that code to make the graph on your system and test but comment it before the submission

    # problem 1
    # data = get_data("provide path", "family.txt")
    # print(data)
    # print(has_children('0')) #true
    # print(has_children('7')) #false
    # print(get_child('6'))
    # print(get_parent('g'))
    # print(siblings('7','A')) #true
    # print(siblings('2','7')) #false
    # print(grandparent('0','3')) #true
    # print(grandparent('0','7')) #false
    # print(get_all())
    # print(cousins('3','6')) #true
    # print(cousins('3','5')) #false


    #problem 2
    # n = 6
    # v = [1,2,3]
    # print(tiles(n,v,[[i] for i in v]))
    # for i in tiles(n,v,[[i] for i in v]):
    #     print(sum(i), end="")
    # n = 4
    # v = [1,2]
    # print(tiles(n,v,[[i] for i in v]))
    # for i in tiles(n,v,[[i] for i in v]):
    #     print(sum(i), end="")    

    #problem 3
    # data = [[5,1,4,1,5],[5,6,2,4],[4,5,1,1],[1,5,10,4,1],[1,1,1,1,1]]
    # for d in data:
    #     print(max_adjacent(d))

    #problem 4

    # data6 = get_data_1("provide path", "payrollwins.txt")
    # m_hat, b_hat, R_sq  = std_linear_regression(data6)
    # print(m_hat,b_hat,R_sq)
    
    # Comment the code for plotting (and the import of matplotlib up top) before you submit to the Autograder.
    # You can test as much as you want on your system but before the submission - please comment the code for
    # plotting.
    # plt.plot([x for x,_ in data6],[y for _,y in data6],'ro')
    # plt.plot([x for x,_ in data6],[m_hat*x + b_hat for x,_ in data6],'b')
    # plt.xlabel("$M Payroll")
    # plt.ylabel("Season Wins")
    # plt.title(f"Least Squares: m = {m_hat}, b = {b_hat}, R^2 = {R_sq} ")
    # plt.ylabel("Y")
    # plt.show()

    # #problem 5
    # name = "fish_data.txt"
    # X,Y = get_fish_data("provide path", name)
    # data5 = [[i,j] for i,j in zip(X,Y)]
    # print(data5)
      
    # plt.plot(X,Y,'ro')
    # xp = np.linspace(1,14,10)
    # degree = 3
    # p3 = make_function(X,Y,degree)
    # plt.plot(xp,p3(xp),'b')
    # plt.xlabel("Age (years)")
    # plt.ylabel("Length (inches)")
    # plt.title("Rock Bass Otolith")
    # plt.show()

    #problem 6
    # data = ["aaaba", "abcba", "abbcde","aaabbbaaaaaac","abcdeffg"]
    # for d in data:
    #     for i in range(1,7):
    #         print(f"{d} with {i} max is\n {max_n(d,i)}")
    
    
    #problem 7
    # model_parameters = (2,.6,4) #starting amount, probablity of win, goal
    # print(simulation(model_parameters,100000))
    
    print()