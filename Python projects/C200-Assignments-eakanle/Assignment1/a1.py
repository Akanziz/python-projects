# We have added import math
# It's only needed once
import math

# Problem 1
#input radius r, height h
#return volume
def c(r,h):
    volume = (1/3)*math.pi*(r**2)*h
    return round(volume, 2)
   
    
# Problem 2
#input t days
#output oxygen content percent of its normal level
def f(t):
    numerator = t**2 + (10*t) + 100
    denominator = t**2 + (20*t) + 100
    value = 100*(numerator/denominator)
    return round(value, 2)


# Problem 3
#input t hours
#return percent watching tv
def P(t):
    a,b,c,d,e = 0.01354,0.49375,2.58333,3.8,31.60704
    return round(a*(t**4) - b*(t**3) + c*(t**2) + d*(t) + e, 2)


# problem 4
#input x percent
#return millions of dollars
def cost(x):
    cost_toxic = (0.5*x)/(100 - x)
    return round(cost_toxic, 2)


# Problem 5
#input dosage a mg and years t
#return child dosage mg
def D(t,a):
    chid_doseage = ((t+1)/(24))*a
    return round(chid_doseage, 2)


# Problem 6
#input number of susceptible, but healthy children
#output number of the infected children
# use math.ceil() before returning your final answer.
def I(S):
    infected_childern = 192 * math.log2(S/762) - S + 763
    return math.ceil(infected_childern)


# Problem 7
#input number of items 
#output total cost 
# q > 0
def C(q):
 a,b,c,d = 0.01,-0.6,13,1000
 return a*(q**3) + b*(q**2) + c*q + d

#input number of items
#output average cost
def A(q):
    return C(q)/q

# Problem 8
#input months t=0,...,11
#output items sold x 1000
def hh(t):
    n,d = 532,1 + 869*math.exp(-1.33*t)
    return math.floor(n/d)

# Problem 9
#input time seconds
#output feet
def height(t):
    height_of_stone = -16*(t**2) + 64*t + 80
    return round(height_of_stone, 2)

# Problem 10
#input t hours
#output percent treatment
def B(t):
    n,d = 0.44*(t**4) + 700,0.1*(t**4) + 7
    return round(n/d, 2)

# Problem 11
#input coefficients for quadratic and value
#output True if value is root, False otherwise
def quad(a,b,c,x):
    return not bool(a*(x**2) + b*(x) + c)


#input P principle, n times per year, t years, r rate
#output dollars
def R(P,r,n,t):
    x = (1 + r/n)**(n*t) - 1
    y = r/n
    return round(P*(x/y),2)

#input dimensions w,l,h for width, length, height of a 
# rectangular solid
#output total surface area
def S(w,l,h):
    return 2 * (w*l + w*h + l*h)



if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.
    """

    #problem 1
    #volume of cone
    print(c(2,5)) 
    print(c(3,7))

    #problem 2
    #oxygen content
    print(f(0))
    print(f(10))

    #problem 3
    #tv watching
    print(P(0))
    print(P(3))
    print(P(8))

    #problem 4
    #toxic waste
    print(cost(50))
    print(cost(70))
    print(cost(90))

    #problem 5
    # cowling's rule
    # print(D(4,500))
    
    #problem 6
    #flu outbreak
    # S = 100
    # print(I(100))
    # S = 300
    print(I(S)) 

    #problem 7
    # average cost
    # make your own inputs/outputs
    
    #problem 8
    print(hh(0))
    print(hh(5))
    print(hh(10))

    #problem 9
    print(height(5))
   
    #problem 10        
    #make your own inputs/outputs

    #problem 11
    #quadratic roots
    print(quad(2,5,-12,-4))
    print(quad(2,5,-12,3/2))
    print(quad(2,5,-12,1))

    # problem 12
    # Sinking Fund
    # P = 22000
    # n = 1
    # t = 7
    # r = 6/100
    print(R(P,r,n,t))
    # P = 500
    # n = 12
    # t = 20
    # r = 4/100
    print(R(P,r,n,t))
    # P = 1200
    # n = 4
    # t = 10
    # r = 8/100
    print(R(P,r,n,t))

    #problem 13
    #make your own inputs/outputs