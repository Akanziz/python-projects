import math

#Problem 1

#INPUT n0 start colony size, m growth rate, t time
#RETURN final colony size
def N(n_0, m, t):
    ans = n_0 * math.exp(m*t)
    return ans

#INPUT t days
#RETURN number of teeth
def N_t(t):
    ans = 71.8*math.exp(-8.96*math.exp(-0.0685*t))
    return math.cell(ans)


#INPUT pressures Pi, Pf 
#RETURN work joules
def W(P_i, P_f):
    R = 8.314
    T = 300
    work = R * T * math.log(P_i / P_f)
    return math.cell(work)


#INPUT V miles per hour, A area, C_l lift coefficient
#RETURN lbs 
def L(V,A,C_l):
    k = 0.0033
    lift = k*(V**2)*A*C_l
    return math.ceil(lift)


###########################################################################
# Functions for Problem 2
###########################################################################
#INPUT coef = (a,b,c)
#RETURN tuple ('up'|'down', (vertex, y-value of vertex))
###########################################################################
def q(coef):
    a,b,c = coef
    discriminant = b**2 - 4*a*c
    if a > 0:
        vertex = 'up'
    else:
        vertex = 'down'
    x_vertex = -b / (2 * a)
    y_vertex = a * x_vertex**2 + b * x_vertex + c
    return (vertex,(round(x_vertex,2), round(y_vertex, 2)))




###########################################################################
# Functions for Problem 3
###########################################################################
#INPUT object x and list lst
#RETURN True if object occurs in the list
#CONSTRAINT You cannot use 'x in y' -- must use bounded looping
def m(x,lst):
    for value in lst:
        if x == value :
            return True
    return False

#INPUT receipt= [[x0,y0],[x1,y1],...,[xn,yn]]
# x is item, y is cost
# tax_rate is the tax on taxable items
# no_tax is a list of items not taxable
#RETURN total amount owed (round values to 2 nearest decimal places)
def amt(reciept, tax_rate, no_tax):
    # [[x0,y0],[x1,y1],.. .,[xn,yn]] = reciept

    
    total = 0
    for x in reciept:

            if x[0] in no_tax:
                total += x[1]
            else:
                total += x[1]*(1+tax_rate)
    return round(total,2)


###########################################################################
# Functions for Problem 4
###########################################################################
#INPUT p0 = (x0,y0) p1 = (x1,y1)
#RETURN dictionary y = mx + b
def make_line(p0,p1):
    x0,y0,x1,y1 = *p0,*p1
    m = round((y1 - y0)/(x1 - x0),2)
    b = round(y0 - (m*x0),2)
    return {'m':m, 'b':b}

#INPUT two lines as dictionary
#RETURN a point (x,y) of intersection or "same line", "parallel lines" 
#rounded to two places
def intersection(l0,l1): 
    if l0['m'] == l1['m']:
        if l0['b'] == l1['b']:
            return "same line"
        else:
            return "parallel lines"
    else:
        x = (l1 ['b'] - l0['b']) / (l0['m'] - l1['m'])
        y = l0['m'] * x + l0['b']
        return round(x, 2), round(y, 2)


###########################################################################
# Functions for Problem 5
###########################################################################
#INPUT List of numbers
#RETURN Various means or error message

def arithmetic_mean(nlst):
    total = 0
    counter = len(nlst)
    for i in nlst:
        total += i
        mean = total/counter
    return mean


def geo_mean(nlst):
    total = 0
    n = len(nlst)
    for i in nlst:
        if nlst == []:
            return "Data Error: 0 values"
    return round((10**(total/n)),2)

def har_mean(nlst):
    if len(nlst) == 0:
            return "Data Error: 0 values"
    
    if 0 in nlst:
        return "data Error: 0 in data"
    
    total = sum(1/ num for num in nlst)
    return round(len(nlst) / total, 2)



def RMS_mean(nlst):
    sum = 0
    n = len(nlst)
    for i in  nlst:
        if nlst == []:
            return "data error: 0 values"
        else:
            sum += i**2
    return round(((sum/n)**(1/2)),2)


###########################################################################
# Function for Problem 6
###########################################################################
#INPUT x object, list of objects, integer y
#RETURN true if x occurs at least y times, false otherwise
def occur_at_least(x,y,lst):
    count = 0
    for i in lst:
        if i == x:
            count += 1
        if count >= y:
            return True
        else:
            return False



###########################################################################
# Functions for Problem 7
###########################################################################
#input two objects x,y and list
#returns True if x occurs strictly more than y in lst, False otherwise
def occurs_more(x,y,lst):
        count = 0
        sum = 0
        for i in lst:
            if i == x:
                count += 1
            elif i ==y:
                sum += 1
            else:
                continue
        if count > sum or lst == []:
            return True 
        else:
            return False 
lst =  [2,2,3,1,2,1,1,2]
print (occurs_more (1 ,2 , lst ) )
print (occurs_more (2 ,3 , lst ) )
print (occurs_more (2 ,3 ,[]) )


#input two objects x, y and list
#return if the number of times x,y occur in list are equal, then return the list
#if x occurs more than y, then remove the occurrences from the left side until
#their counts are equal, then return the list
#if y occurs more than x, the same procedure
def equal_remove(x,y,lst):
    tmp = lst
    def cnt_occurs(x, lst):
        count = 0
        for i in lst:
            if i == x:
                count += 1
        return count
    
    x_c,y_c = cnt_occurs(x,lst), cnt_occurs(y,lst)

    def re_k(x,cnt, lst):
        result = lst[:]
        for i in range(cnt):
            result.remove(x)
        return result
    

    if x_c < y_c:
        tmp = re_k(y,y_c-x_c,tmp)
    elif x_c > y_c:
        tmp = re_k(x,x_c - y_c, tmp)

    return tmp
    

###########################################################################
# Functions for Problem 8
###########################################################################
#INPUT list of numbers
#RETURN True if geometric series, False otherwise
def is_geo(xlst):
    if  len(xlst) <=2:
        return 0
    for i in range(len(xlst)-1):
        ratio = xlst[1] / xlst[0]
        if xlst[i] * ratio == xlst[i+1]:
            continue
        else:
            return 0
        
    return 1

###########################################################################
# Functions for Problem 9
###########################################################################
#INPUT pair of points in 2D
#RETURN distance round to two decimal places
def net_displacement(p0,p1):
        x0,y0,x1,y1 = *p0, *p1
        displacement = ((x0-x1)**2+(y0-y1)**2)**(1,2)
        return round(displacement,2)

#INPUT starting position (x,y) and list of one step directions w,e,s,n that move the positon
#of x,y
#RETURN a tuple final destination, distance, distance from start
def track(start_pos, movement):
    pass



###########################################################################
# Functions for Problem 10
###########################################################################
#INPUT pair of tuples from tracking
#RETURN distance betweem two ending places 
def final_distance(m0,m1):
   x



###########################################################################
# Functions for Problem 11
###########################################################################
#INPUT conference and game
#RETURN the dictionary conference after changing wins,losses, percentages of teams (there are no ties)
def update(conference, game):
    pass



###########################################################################
# Functions for Problem 12
###########################################################################
#INPUT amt and list of donations
#RETURN tuple: amt, donations left, the amount of the goal left
def go_fund_me(amt, donations):
    pass



###########################################################################
# Functions for Problem 13
###########################################################################
#INPUT credit score cr and list of potential clients [[n0,cd0],[n1,cd1],...,[nm,cdm]] where n is name, cd is unweighted dictionary of credit values
#RETURN list of people and their score that is strictly greater than cr; if nobody qualifies, then return empty list
def loan(cr, lst):
    pass



#Problem 14
#INPUT current temperature T(t) of fish (T_t, environment T_e, temperature of fish and lst of what dogs were doing hours ago]
#OUTPUT The time (in hours) that elapsed after the murder reported as a float
#you must determine k from problem and formula from description
def time(T_t, T_e, T_0):
    #k = ??? #you have to determine this
    pass




if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.

    You **do not** have to put anything here
    """
    #problem 1
    print(N(500,100,4)) 
    print(N_t(1000))
    print(W(10,1))
    # print(L(33.8,512,0.515))

    #problem 2
    print(q((-2.6,7.6,-10)))
    print(q((1,-10.2,26.01)))

    #problem 3
    receipt = [[1,1.45],[3,10.00],[2,1.45],[5,2.00]]
    tax_rate,no_tax = 7/100, [33,5,2]
    print(amt(receipt,tax_rate, no_tax))
    print(amt(receipt,10/100,[]))

    #problem 4
    p0 = (32,32)
    p1 = (29,5)
    p2 = (15,10)
    p3 = (49,25)
    p4 = (15,30)
    p5 = (50,15)
 
    l0,l1 = make_line(p0,p1),make_line(p2,p3)
    print(intersection(l0,l1))
    l0 = make_line(p4,p5)
    print(intersection(l0,l1))
    
    p6,p7,p8 = (0,0),(1,1),(2,2)
    p9,p10 = (0,1),(1,2)
    print(intersection(make_line(p6,p7),make_line(p7,p8))) # same line
    print(intersection(make_line(p6,p7),make_line(p9,p10))) # parallel lines

    #problem 5
    print(arithmetic_mean([1,2,3]))
    print(geo_mean([2,4,8]))
    print(har_mean([1,2,3]))
    print(RMS_mean([1,3,4,5,7]))

    #problem 6
    # data6 = [[1,[1,2,1,2,1,1],4], [1,[1,2,1,2,1,1],3],
    #     [1,(1,2,1,2,1,0),4], ]

    # for d in data6:
    #     print(occur_at_least(*d))

    #problem 7
    # lst = [2,2,3,1,2,1,1,2]
    # print(occurs_more(1,2,lst))
    # print(occurs_more(2,3,lst))
    # print(occurs_more(2,3,[]))
 

    # print(equal_remove(1,2,lst))
    # print(equal_remove(1,3,lst))
    # print(equal_remove(2,3,lst))
    # print(occurs_more(2,3,(equal_remove(2,3,lst))))

    # #problem 8
    # xlst = [1/2,1/4,1/8,1/16,1/32]
    # print(is_geo(xlst))
    # xlst = [1,-3,9,-27]
    # print(is_geo(xlst))
    # xlst = [625,125,25]
    # print(is_geo(xlst))
    # xlst = [1/2,1/4,1/8,1/16,1/31]
    # print(is_geo(xlst))
    # xlst = [1,-3,9,-26]
    # print(is_geo(xlst))
    # xlst = [625,125,24]
    # print(is_geo(xlst))
    # print(is_geo([1/2,1/4]))

    # #problem 9
    # data_m9 = [[(0,0), list(10*'n' + 15*'e' + 10*'s'+15*'w')],
    #       [(0,0), list(3*'n' + 4*'e')],
    #       [(1,2), list(3*'s' + 4*'w')]]

    # for d in data_m9:
    #     print(track(*d))

    #problem 10
    # data_m10 = [[(0,0), list(10*'n' + 15*'e' + 10*'s'+15*'w')],
    #       [(0,0), list(3*'n' + 4*'e')],
    #       [(1,2), list(3*'s' + 4*'w')]]

    # print(final_distance(track(*data_m10[1]),track(*(data_m10[2]))))

    # #problem 11
    # big_10_women = {'IU':{'W':12,'L':1,'PCT':.923, 'Home':(13,0)},
    #             'PU':{'W':6,'L':6,'PCT':.500, 'Home':(8,4)}, 
    #             'IOWA':{'W':11,'L':1,'PCT':.917, 'Home':(11,1)},
    #             'NW':{'W':1,'L':11,'PCT':.083,'Home':(6,6)}}
    
    # print(big_10_women['IU'],big_10_women['IOWA'])
    # update(big_10_women,{'IU':87,'IOWA':78})
    # print(big_10_women['IU'],big_10_women['IOWA'])
    
    # update(big_10_women, {'IU':8,'IOWA':7})
    # print(big_10_women)
    
    # update(big_10_women, {'PU':87,'NW':91})
    # print(big_10_women)
    
    # update(big_10_women, {'IOWA':89,'PU':75})
    # print(big_10_women)
    

    # #problem 12
    # data12 = [[100,[10,15,20,30,29,13,15,40]],
    #     [100,[]],
    #     [100,[30,4]]]

    # for d in data12:
    #     print(go_fund_me(*d))
    # print(go_fund_me(50, [45,47,78]))

    #Problem 13
    # data = [['x',{'P':600, 'L':700,'A': 500, 'N': 170, 'C': 250}],
    #     ['y',{'P':550, 'L':720,'A': 500, 'N': 230, 'C': 250}],
    #     ['b',{'P':560, 'L':710,'A': 500, 'N': 221, 'C': 250}],
    #     ['c',{'P':800, 'L':700,'A': 200, 'N': 100, 'C': 150}],
    #     ['a',{'P':800, 'L':800,'A': 600, 'N': 250, 'C': 150}],
    #     ['z',{'P':800, 'L':800,'A': 500, 'N': 250, 'C': 150}]]
    # print(loan(550,data))

    #problem 14
    #initial scene of the crime data
   
    # no_alibis = {"Ursala":[3,4],"Shilah":[2,2.5],"Kaiser":[1,2]}
    # T_t = 81
    # T_e = 65
    # T_0 = 85
    # time_discovered = 4 #PM Dr. D's living room
    # suspects = []

    # time_of_murder = time_discovered - time(T_t, T_e, T_0)
    # for name,times in no_alibis.items():
    #     start,end = times
    #     if start <= time_of_murder <= end:
    #         suspects.append(name)

    # print(f"The suspect(s) {suspects}")