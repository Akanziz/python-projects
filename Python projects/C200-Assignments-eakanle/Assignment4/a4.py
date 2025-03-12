import math
#import matplotlib.pyplot as plt



###########################################################################
# Functions for Problem 1
###########################################################################
#INPUT dlst = [day, month, year]
#RETURN string corresponding to the day of the week (i.e. "Mon", "Sun", etc)
week = {1:"Mon", 2:"Tue", 3:"Wed", 4:"Thu", 5:"Fri", 6:"Sat", 7:"Sun"}
def a(dlst):
    d,m,y = dlst
    return (y - (14 - m)/12)

def b(dlst):
    x = a(dlst) + (a(dlst))/4 - (a(dlst))/100 + (a(dlst))/400
    return math.floor(x)

def c(dlst):
    d,m,y = dlst
    return (m + 12*(14-m)/12 - 2)

def day(dlst):
    d,m,y = dlst
    ans = (d + b(dlst) + (31 * (c(dlst))/12)) % 7
    
    if ans in week:
        return week[ans]
    else:
        return "Invalid day"

###########################################################################
# Functions for Problem 2
###########################################################################
#INPUT t = (a,b,c)
#RETURN return complex or real roots
def q(t):
    a, b, c = t
    determinant = b**2 - 4*a*c

    if determinant >= 0:
        r1 = round(((-b - math.sqrt(determinant)) / (2*a)), 2)
        r2 = round(((-b + math.sqrt(determinant)) / (2*a)), 2)
        return r1, r2
    elif determinant < 0:
        real_part = round((-b / (2 * a)),2)
        imag_part = round((math.sqrt(-determinant) / (2 * a)),2)
        root1 = complex(real_part, imag_part)
        root2 = complex(real_part, -imag_part)
        return root1, root2




###########################################################################
# Functions for Problem 3
###########################################################################
#INPUT a nested list of people encoded as 0's and 1's. v0 and v1 are the respective lists respresenting the people pairs.
# You'll be comparing the smallest degree of difference between each sublist representing each person.
# RETURN person pair with the smallest degree (smallest degree of difference between the person pair lists)
def inner_prod(v0,v1):
    inner_prod_result = 0
    
    for c in range(len(v0)):
        inner_prod_result = inner_prod_result + (v0[c]*v1[c])

    return inner_prod_result 

def mag(v):
    result = math.sqrt(inner_prod(v, v))
    return result

def angle(v0,v1):
    if mag(v0) == 0 or mag(v1) == 0:
        return 0.0
    
    argument = inner_prod(v0,v1) / (mag(v0) * mag(v1))
    argument = max(min(argument, 1), -1)

    angle_result = math.acos(argument)
    return round((angle_result * (180/math.pi)), 2)


def match(people):
    result = []
    for i in range(len(people)):
        j = 1
        while j + i < len(people):
            angle_result = angle(people[i], people[i + j])
            result_lst = [people[i], people[i + j], angle_result]
            result.append(result_lst)
            j += 1
    return result


def best_match(scores):
    if not scores:
        return None
    
    index = 0
    best_angle = scores[0][2]
    
    for i in range(1, len(scores)):
        if scores[i][2] < best_angle:
            index = i
            best_angle = scores[i][2]

    return scores[index]



###########################################################################
# Functions for Problem 4
###########################################################################
#INPUT tuple of quadratic (ax^2 + bx + c)
#RETURN tuple (m,n) cofficients for real solutions a(x+m)^2 + n = 0
#CONSTRAINT round to 2 places
def c_s(coefficients) :
    a,b,c = coefficients
    m = round((b / (2*a)) ,2)
    n = round((c - (b**2) / (4*a)) ,2)
    return (m, n)


#INPUT coefficients for quadratic ax^2 + bx + c 
#RETURN return real roots uses c_s
def q_(coefficients):
    m, n = c_s(coefficients)
    r1 = round((-m + math. sqrt (-n)) , 2)
    r2 = round((-m - math. sqrt (-n)) ,2)

    return (r2, r1)


####＃#######＃############################################################
# Functions for Problem 5
#＃#＃####＃###############################################################
# INPUT List os numbers
# RETURN Variots means
def mean(lst):
    avr = (sum(lst))/len(lst)
    return round (avr, 2)

def var(lst):
    total = 0
    for i in lst:
        total += (i - mean (lst))**2
    vr = 1/(len(lst))*total
    return round (vr,2)

def std(lst):
    sd = math.sqrt(var(lst))
    return round (sd,2)

def mean_centered(lst):
    new = []
    for i in lst:
        new += [i - mean(lst)]
    return new



###########################################################################
# Functions for Problem 6
###########################################################################
# INPUT supply and demand coefficients
# RETURN solution of quadratic equations
def equi(s,d):
    r = q((s[0]-d[0],s[1]-d[1],s[2]-d[2]))
    return r


###########################################################################
# Functions for Problem 7
###########################################################################
#INPUT parameters to LV model
#OUTPUT two lists history_rabbit, history_fox of populations
def rabbit_fox(br,dr,df,bf,rabbit,fox,time_limit):
    b = 0
    history_fox = []
    history_rabbit = []
    while b < time_limit:
        history_rabbit.append (rabbit)
        history_fox.append (fox)
        old_rab = rabbit
        rabbit = math. ceil(rabbit + (rabbit * br) - (rabbit * fox * dr) )
        fox = math.ceil(fox + (bf * dr * old_rab * fox) - (fox * df))
        b += 1

     
    return history_rabbit, history_fox

###########################################################################
# Functions for Problem 8
###########################################################################
# INPUT container, sample size n
# OUTPUT random selection of size n in any order
# CONSTRAINT uses random 
# This is with replacement
def sub_strings(str,cnt):
    for i in range(len(str)):
        for j in range(i + 1, len(str) + 1):
            sub_string = str[i:j]
            if sub_string in cnt:
                cnt[sub_string] += 1
            else:
                cnt[sub_string] =1
    return cnt
    



###########################################################################
# Functions for Problem 9
###########################################################################
#INPUT values for annuity
#OUTPUT deposit amount needed
def deposit(S,i,n) :
    monthly_deposit = round(((S * i) / ((1 + i)**n - 1)),2)
    return monthly_deposit  


#INPUT sinking fund values except deposit
#OUTPUT a list of period, deposit, interest, accrued total fund
def sinking_fund(final_amt, r, m, y):
    result = []
    n = m * y
    i = r / m

    R = deposit(final_amt, i, n)

    b = 0
    total = 0

    while b < n:
        interest = round((((i)*(total))),2)
        total = total + R + interest
        loop_result = [b, R, interest, round(total, 2)]
        result.append(loop_result)
        b +=1
    
    return result


###########################################################################
# Functions for Problem 10
###########################################################################
#INPUT list of numbers
#OUTPUT Boolean if geometric series
def is_geometric_sequence(lst):
    if len(lst) < 3:
        return False
    else:
        for i in range(len (lst)-1):
            ratio = lst [1] / lst [0]
            if lst[i] * ratio == lst[i+1]:
                continue
            else:
                return False
        return True



###########################################################################
# Functions for Problem 11
###########################################################################
#INPUT portfolio of stock price, shares, market
#OUTPUT current total value
def value(portfolio, market):  
    port_value = 0
    mkt_value = 0

    for stock, (buy_price, shares) in portfolio['stock'].items():
        port_value += buy_price * shares 
        mkt_value += market[stock] * shares
    return round((mkt_value - port_value) / port_value * 100, 0)

portfolios = {'A':{'stock':{'X':(41.45,45),'y':(22.20,1000)}},
    'B':{'stock':{'x':(33.45,15),'y':(12.20,400)}}}
market = {'x':43.00, 'y':22.50}




if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.

    You **do not** have to put anything here
    """

    #problem 1
    print(day([14,2,2000]))
    print(day([14,2,1963]))
    print(day([14,2,1972]))

    #problem 2
    print(q((3,4,2)))
    print(q((1,3,-4)))
    print(q((1,-2,-4)))

    #problem 3
    people0 = [[0,1,1],[1,0,0],[1,1,1]]
    print(match(people0))
    print(best_match(match(people0)))

    people1 = [[0,1,1,0,0,0,1],
               [1,1,0,1,1,1,0],
               [1,0,1,1,0,1,1],
               [1,0,0,1,1,0,0],
               [1,1,1,0,0,1,0]]
    print(best_match(match(people1)))
    #output is ([1, 1, 0, 1, 1, 1, 0], [1, 0, 0, 1, 1, 0, 0], 39.23)

    v0,v1 = (2,3,-1), (1,-3,5)
    print(angle(v0,v1)) #122.83

    v0,v1 = (3,4,-1),(2,-1,1)
    print(angle(v0,v1)) #85.41

    v0,v1 = (5,-1,1),(1,1,-1)
    print(angle(v0,v1)) #70.53


    #problem 4 pairs should be identical
    print(q((1,-4,-8)), q_((1,-4,-8)))
    print(q((1,3,-4)),q_((1,3,-4)))
   
    
    #problem 5
    lst = [1,3,3,2,9,10]

    print(mean(lst))
    print(var(lst))
    print(std(lst))
    print(mean(mean_centered(lst)))

    #problem 6
    s = (-.025,-.5,60)
    d = (0.02,.6,20)
    print(equi(s,d))
    
    s = (5,7,-350)
    d = (4,-8,1000)

    print(equi(s,d))

    #problem 7
    br = 0.03
    dr = 0.0004
    df = 0.25
    bf = 0.11
    rabbit = 3000  #initial population size
    fox = 200  #initial population size
    time_limit = 2000
    history_rabbit, history_fox = rabbit_fox(br,dr,df,bf,rabbit,fox, time_limit)

    # #uncomment to see time, rabbit, fox populations
    for j in range(0,2000,200):
        print(j, history_rabbit[j], history_fox[j])


    # plt.plot(list(range(0,time_limit)),history_rabbit)
    # plt.plot(list(range(0,time_limit)),history_fox)
    # plt.xlabel("Time")
    # plt.ylabel("Population Size")
    # plt.legend(["Rabbit","Fox"])
    # plt.title("Lotka-Volterra Model for Rabbit & Fox")
    # plt.show()

    
    #problem 8
    data = ["abcabc","ccccc",""]
    for d in data:
        cnt = {}
        sub_strings(d,cnt)
        print(cnt)

    #problem 9
    S = 30000
    m = 4
    r = 10/100
    y = 2
    for i in sinking_fund(S,r,m,y):
        print(i)


    #problem 10
    data = [[1,2,4,6],[2,4,8,16],[10,30,90,270,810,2430]]
    for d in data:
        print(is_geometric_sequence(d))


    #problem 11
    portfolios =  {'A':{'stock':{'x':(41.45,45),'y':(22.20,1000)}},
    'B':{'stock':{'x':(33.45,15),'y':(12.20,400)}}}
    market = {'x':43.00, 'y':22.50}


    for name, portfolio in portfolios.items():
        print(f"{name} {value(portfolio,market)}")
