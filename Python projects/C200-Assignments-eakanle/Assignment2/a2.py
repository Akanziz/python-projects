import math
from turtle import st

#problem 1
#input real number
#return real number
def g(x):
    if not x == 0:
        x+= 2
    elif x == 0:
        x = 1
    return x


#problem 2
#input year 1977-1997
#return percent income or "YearError: year" if year 
#is outside range
def f(t):
    income = 0
    if 1977<= t <= 1984:
        income = 2/7*(t - 1977) + 12
    elif 1984 <= t <= 1987:
        income = (t -1977) + 7
    elif 1987 <= t <= 1997:
        income = 3/5*(t - 1977) + 11
    else:
        return f"year Error: {t}"
    return income


#problem 3
# input t years = 0, 1, then 2
# output dollars or error in the format YearError: t
def h(t):
    if 0 <= t <= 2:
        def h_0(t):
            output = 110 / ((1/2)*t + 1)
            return round(output,2)


        def h_1(t):
            output = 26*((1/4)*t**2 - 1)**2 + 52
            return round(output,2)
    

        return round((h_0(t) - h_1(t)),2)   
    else:
        return f"yearError: {t}"


#problem 4
#input tuple (a,b,c) coefficients
#output tuple roots (x_1, x_2) where x_1 >= x_2
def q(lst):
    a,b,c = lst
    x_1 = (-(b)+ ((b**2)-(4*a*c))**(1/2))/(2*a)
    x_2 = (-(b)- ((b**2)-(4*a*c))**(1/2))/(2*a)
    return  [x_1, x_2]


#problem 5
#input [arg1,op,arg2,ans]
#output boolean (True or False) depending on the result of arg1 op arg2 == ans
def eq(lst):
    if


#problem 6
#input string of COVID symptoms "ABC", "ACB",...,"CBA"
#output 'very likely', 'likely', 'somewhat likely' based on severity
def covid(symptoms):
    if symptoms in ['ABC', 'ABC']:
        return 'very likely'
    if symptoms in ['BAC', 'BCA']:
        return 'likely'
    if symptoms in ['CAB', 'CBA']:
        return 'somewhat likely'


#problem 7
#INPUT two numbers
#RETURN maximum of the two
#You cannot use Python's max() function
#You must use if, elif, else (or some combination)
def max2d(x,y):
    if x > y:
        return x
    else:
        return y


#INPUT 3 numbers
#RETURN maximum of the three
#You must use your max2D function
def max3d(x,y,z):
    return max2d(x,max2d(y,z))

#problem 8
#INPUT [name0,name1, votes] where votes is a non-empty list of 0,1
#RETURN a tuple (name, c, t) where name is the winner, c is the number of winning votes
#t is the total votes cast 
def decision(data):
    pass


#problem 9 
#INPUT three values: all have values or two have values and the remain has None
#OUTPUT for two values, return the computed None variable
#for three values return True or False using isclose(x,y,abs_tol = 0.001)
#remember to convert degrees to radians
def solve(theta, opposite, adjacent):
    pass


# problem 10
def future(A, r):
    A = A * 0.2
    no_ = 12
    time = 2
    payment = A * (r/no_) / ((1+ (r/no_)) ** (no_*time) - 1)
    return round(payment,2)


if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the unit testing Feel free to add print statements. 
    You should uncomment *after* you've completed the function
    """

    #problem 1 
    print(g(0))
    print(g(1))
    print(g(1.01))

    #problem 2
    print(f(1976))
    print(f(1977))
    print(f(1985))
    print(f(1988))
    print(f(2000))

    #problem 3
    print(h(0))
    print(h(1))
    print(h(1.5))
    print(h(2))
    print(h(3))

    #problem 4
    print(q((1,0,-1)))
    print(q((6,-1,-35)))
    print(q((1,-7,-7)))

    #problem 5
    # print(eq([14, "/",2, 7]))
    # print(eq([20, "*",19, 381]))
    # print(eq([20, "*",19, 380]))
    # print(eq([2,"**",3,8]))
    # print(eq([1.1,'-',1,.1])) #saw in class this doesn't work! (will return False)

    #problem 6
    print(covid('ABC'),covid('ACB'))
    print(covid('BAC'),covid('BCA'))
    print(covid('CAB'),covid('CBA'))

    #problem 7
    print(max3d(1,2,3))
    print(max3d(1,3,2))
    print(max3d(3,2,1))

    #problem 8
    #data0 = ['B','Z',[0,1,1,0,1,0,0]]
    #print(decision(data0))
    #data1 = ['B', 'Z',[1,0,1]]
    #print(decision(data1))
    #data2 = ['B', 'Z',[1,0,1,0,1,1,0,0]]
    #print(decision(data2))


    #problem 9
    # print(solve(5,None,105600))
    # print(solve(None,9238.9,105600))
    # print(solve(5,9238.8,None))
    # print(solve(5,9238.8,105600))
    # print(solve(5,9100,105600))

    #problem 10
    home_price, rate = 250000, 6/100
    t,n = 2,12                         #years, monthly
    payment = future(home_price,rate)
    print(f"{n} payments yearly for {t} years requires ${payment}")
    # #confirm this achieves 50000
    A = round(payment*((1 + rate/n)**(t*n)-1)/(rate/n),2)
    print(A)
