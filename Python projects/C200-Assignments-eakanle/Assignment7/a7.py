import numpy as np
import random as rn
import csv
import math
# import matplotlib
# import matplotlib.pyplot as plt
import os 
import csv
from sklearn.linear_model import LinearRegression


# Problem 1
# Input: data in the file payrollwins.txt
# Output: slope, intercept, R^2 and the model

# Please remeber the basics of File I/O form the labs and lectures.
# For testing you code in VSC, you have to use path that works on your system.
# Although, it's not a good practise but even using a hard-coded path would work, but
# before submitting to the Autograder, you should keep path as "", because Autograder has 
# it's own OS and it's own FileSystem, and the path which works on your system may not be valid on the Autograder. 
# Please remember to comment out all code for plotting (and the import of matplotlib) before submitting to the Autograder.


# Input: path and filename
# Output: the data in the format as expected by the LinearRegression function of sklearn
# CONSTRAINT use csv reader
# file containig payroll data
def get_data(path, filename):
    with open(path + filename, newline='') as csvfile:
        datareader = csv.reader(csvfile)
        data = ([(float(i[0]), float(i[1])) for i in datareader])
    return data


#input data for univariate regression
# Output: slope, intercept, R^2 and the model object returned by sklearn
def my_scikit_LR(data6):
    x = [x for x,_ in data6]
    y = [y for _,y in data6]
    x = np.array(x).reshape((-1, 1))
    y = np.array(y)
    model = LinearRegression().fit(x, y)
    r_sq = model.score(x, y)
    return model.coef_, model.intercept_, r_sq, model.predict




# Problem 2
# The recursive version of the functions is give by us
# You need to complete the tail_recursive, while and generator version

#recursive functions

def p(n):
    if n:
        return p(n-1) + 0.02*p(n-1)
    else:
        return 10000

#MUST be implemented with tail recursion
def p_t(n, acc=10000):
    if n:
        return p_t(n-1, acc + 0.02*acc) 
    elif n == 0:
        return acc

#MUST be implemented with a WHILE LOOP
def p_w(n, acc=10000):
    while n != 0:
        acc = acc + 0.02 * acc 
        n -= 1 
    return acc

#MUST be implemented with generator
def p_g():
    acc = 10000
    while True:
        yield acc
        acc = acc + 0.02*acc


def c(n):
    if n > 1:
        return 9*c(n-1) + 10**(n-1) - c(n-1)
    else:
        return 9

#MUST be implemented with tail recursion
def c_t(n, acc1=9, acc2=0):
    if n == 1:
        return acc1 
    else:
        return c_t(n-1, 9 * acc1 + 10**(acc2+1) - acc1, acc2 + 1)
        
#MUST be implemented with a WHILE LOOP
def c_w(n, acc1=9, acc2=0):
    if n == 1:
        return acc1
    while acc2 < n - 1:
        acc1, acc2 = 9 * acc1 + 10**(acc2+1) - acc1, acc2 + 1
    return acc1 

#MUST be implemented with generator
def c_g():
    n = 1
    acc = 9
    while True:
        yield acc
        acc = 9 * acc + 10 ** n - acc
        n += 1



def d(n):
    if n:
        return 3*d(n-1) + 1
    else:
        return 1

#MUST be implemented with tail recursion
def d_t(n, acc=1):
    if n:
        return d_t(n-1,3 * acc + 1)
    elif n == 0:
        return acc

#MUST be implemented with a WHILE LOOP 
def d_w(n, acc=1):
    while n != 0:
        acc = 3 * acc + 1
        n -= 1
    return acc

#MUST be implemented with generator
def d_g():
    acc, n = 1, 0
    while True:
        yield acc
        # n += 1
        acc = 3 * acc + 1



# Problem 3
def c_2(n, m):
    if m == 0 or n == m:
        return 1
    else:
        return c_2(n-1, m) + c_2(n-1, m-1)

def B(n):
    if n == 0:
        return 1
    else:
        numerator = sum(B(k) * c_2(n + 1, k) for k in range (n))
        denominator = n + 1
        return -numerator / denominator



# problem 4
# input function and epsilon
# output lambda expression (derivative)
def derivative(f, epsilon):
    return lambda x :(f(x + epsilon) - f(x - epsilon))/ (2*epsilon)
    
def f(x):
    return x**2 - 3*x



# Problem 5
# INPUT path and file name
# OUTPUT two lists of incomes and happiness 
# from income_data.csv
# use scikit-learn_LR 
def get_data_2(path, name):
    with open(path + name, newline='') as csvfile:
        datareader = csv.reader(csvfile)
        next(datareader)
        data = []
        # data.extend[(float(i[0]), float(i[1])) for i in datareader]
        data = ([(float(i[0]), float(i[1])) for i in datareader])
        # for × in datareader:
        #     data.append(x)
    return data  




# problem 6 

# INPUTS ith candle, starting value of x, default width, and the four critical values: open, close, max_p, min_p.
# RETURN three tuples: The first being the data of the rectangle I.E. point, width, height, and color. 
# Next tuple should be the topline. And lastly the last tuple should be the bottom line.  
# (point, width, height, color), topline, bottomline
# point: coordinates of the lower left point of the rectangle, width of rectangle, height of rectangle and color of rectangle 
# topline ((xt0, yt0),(xt1, yt1)) coordinates of the line from max to top middle of box
# bottomline ((xb0, yb0),(xb1, yb1)) coordinates of the line from min to bottom middle of box

def make(i, start, width_default, d):
    open, close, max, min = d
    if open < close:
        color = "green"
        y_top = close
        y_bot = open
        height = y_top - y_bot
    else:
        color = "red"
        y_top = open
        y_bot = close
        height = y_top - y_bot

    mid_x = (width_default / 2) * (i +1)

    return ((start,y_bot),width_default,height, color), ((mid_x,max),(mid_x, y_top)), ((mid_x, y_bot),(mid_x,min))
 
 




if __name__ == "__main__":
    
    
    # Problem 1
    # Please revisit (if need be) the basics of File I/O from the labs and lectures.
    # For testing you code in VSC, you have to use path that works on your system.
    # For submitting to the Autograder, you should keep path as "", because Autograder has 
    # it's own OS and it's own FileSystem, and the path which works on your system may not be valid on the Autograder.
    
    # Please remember to comment out all code for plotting (and the import of matplotlib) before submitting to the Autograder.
    # You can uncomment it for testing on your system and VSC. 
    
    # data6 = get_data("path_to_the_directory_where_file_resides", "payrollwins.txt")
    # print(f"Model built from parameters applied to 10: {(lambda x:0.1250*x + 67.498)(10)}")
    # plt.plot([x for x,_ in data6],[y for _,y in data6],'ro')
    # m_hat, b_hat, R_sq, model = my_scikit_LR(data6)
    # print(f"m_hat: {m_hat}, b_hat: {b_hat}, R^2: {R_sq}")
    # plt.plot([x for x,_ in data6],model(np.array([[x] for x,_ in data6])),'b')
    # print(f"Scikit Model applied to 10: {model(np.array([[10]]))[0][0]}")
    # plt.xlabel("$M cost")
    # plt.ylabel("Wins")
    # plt.title(f"Wins as function of $M cost R^2 = {round(R_sq,3)}")
    # plt.show()
    
    
    
    # Problem 2 
    # for i,j in zip(range(5),p_g()):
    #     print(p(i),p_t(i),p_w(i),j)
    
    # 10000 10000 10000 10000
    # 10200.0 10200.0 10200.0 10200.0
    # 10404.0 10404.0 10404.0 10404.0
    # 10612.08 10612.08 10612.08 10612.08        
    # 10824.3216 10824.3216 10824.3216 10824.3216
    
    # for i,j in zip(range(1,7),c_g()):
    #     print(c(i),c_t(i),c_w(i),j)
    
    # # 9 9 9 9
    # # 82 82 82 82
    # # 756 756 756 756
    # # 7048 7048 7048 7048
    # # 66384 66384 66384 66384
    # # 631072 631072 631072 631072
    
    
    # for i,j in zip(range(5),d_g()):
    #     print(d(i),d_t(i),d_w(i),j)
    # # 1 1 1 1
    # # 4 4 4 4
    # # 13 13 13 13
    # # 40 40 40 40
    # # 121 121 121 121

    
    # Problem 3
    # for i in range(6):
    #     print(f"B({i}) = {B(i)}")
    # # B(0) = 1
    # # B(1) = -0.5
    # # B(2) = 0.16666666666666666
    # # B(3) = -0.0
    # # B(4) = -0.033333333333333305
    # # B(5) = -7.401486830834377e-17
    
    
    # Problem 4
    # data = 2 
    # epsilon = 10e-8
    # print((derivative(f,epsilon)(data)))
    # f_prime = derivative((lambda x:x**2-3*x),epsilon)
    # print(f_prime(data))
    
    
    # problem 5
    
    # Please revisit (if need be) the basics of File I/O form the labs and lectures.
    # For testing you code in VSC, you have to use path that works on your system.
    # But, before submitting to the Autograder, you should keep the path as "", because Autograder has 
    # it's own OS and it's own FileSystem, and the path which works on your system may not be valid on the Autograder.
    
    # Please remember to comment out all code for plotting (and the import of matplotlib) before submitting to the Autograder.
    # You can uncomment it for testing on your system and VSC.
    
    # path,name = "path_to_the_directory_where_file_resides", "income_data.csv"
    # data4 = get_data_2(path,name)      
    # plt.plot([x for x,_ in data4],[y for _,y in data4],'ro')
    # m_hat, b_hat, R_sq, model = my_scikit_LR(data4)
    # print(f"m_hat: {m_hat}, b_hat: {b_hat}, R^2: {R_sq}")
    # plt.plot([x for x,_ in data4],model(np.array([[x] for x,_ in data4])),'b')
    # plt.xlabel("$M cost")
    # plt.ylabel("Wins")
    # plt.title(f"Wins as function of $M cost R^2 = {round(R_sq,3)}")
    # plt.show()
    
    
    #problem 6
    
    # data5 = [[20,15,32,10],[10,14,15,9],[22,23,27,9],[15,16,16,15],[26,12,30,2],[5,30,40,4]]
    
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # start = 0
    
    # default_width = 10
    
    # for i in range(len(data5)):
    #     candle_box,top_line,bottom_line = make(i, start, default_width, data5[i])
    #     print(candle_box)
    #     ax.add_patch(matplotlib.patches.Rectangle(*candle_box[0:3],color = candle_box[3]))
    #     plt.plot([x for x,_ in top_line],[y for _,y in top_line],'black')
    #     plt.plot([x for x,_ in bottom_line],[y for _,y in bottom_line],'black')
    #     start += default_width


    # plt.xlabel("time (hour)")
    # plt.ylabel("Stock X price")
    # plt.title("Candlestick for Stock X mm/dd/yyyy")  
    # plt.xlim([0, 60])
    # plt.ylim([0, 35])
  
    # plt.show()
    
    print()