import math

########################
# PROBLEM 1
########################

#recursive functions
# Implement as per the directions in the PDF
def p(n):
    if n == 0:
        return 10000
    else:
        return (p(n-1)) + (0.02*p(n-1))
    

def c(n):
    if n == 1:
        return 9
    else:
        return (9 * c(n - 1)) + (10**(n - 1)) - c(n - 1)

def d(n):
    if n == 0:
        return 1
    else:
        return (3 * d(n-1)) + 1

def f(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (f(n - 1)) + (f(n - 2))
    
def e(n):
    if n == 1:
        return 12
    else:
        return (-5) * e(n - 1)


def c_2(n, k):
    if k == 0 or n == k:
        return 1 
    else:
        return c_2(n-1, k-1) + c_2(n-1, k)


def M(c,i):
    if c == 0:
        return 1
    elif c < 0 or f(i) > 10:
        return 0
    return M(c - f(c), i + 1) + M(c, i + 1)

  


########################
# PROBLEM 2
########################

# INPUT: a list of numbers
# OUTPUT: a list containing the start of interval, end of interval and maximal sum
def msi(x):
    tmp = x[0]
    start, end = 0, 1

    for a in range (len(x)):
        for b in range (len(x)):
            max = sum(x[a:b + 1 + a])
            if max > tmp:
                tmp = max
                start = a
                end = a + b + 1
    
    return [start, end, tmp]

########################
# PROBLEM 3
########################
# INPUT: list of cheese (0s or 1s)
# OUPUT: List with 0s moved to the front of the list and 1s at the back (see PDF for sample output)

def move(x):
    lo,hi = 0,len(x)-1
    
    while lo < hi:
        if x[lo] == 1 and x[hi] == 0:
            x[lo], x[hi] = x[hi], x[lo]
        if x[lo]== 0:
            lo += 1
        if x[hi] == 1:
            hi -= 1
    
    return x


########################
# PROBLEM 4
########################

#INPUT list of immutable objects
#RETURN probability distribution as a list
def makeProbability(xlst):
    d = {}
    for value in xlst:
        b = value
        if b in d.keys():
            d[b] += 1 
        else:
            d[b] = 1
    new_list = []
    for b in d.keys():
        new_list.append(d[b] / len(xlst))
    return (new_list)

#INPUT probability distribution
#RETURN non-negative number entropy
def entropy(xlst):
    entry = makeProbability(xlst)
    output = 0
 
 
    for b in entry:
        output += b * math.log2(b)
 
    output = -output
    return (round(output, 2))   



########################
# PROBLEM 5
########################

#INPUT list of 0s 1s
#OUTPUT longest sequential run of 1s
def L(x):
    if len(x) == 0:
        return 0
    if len(x) == 1:
        return x[0]
    main_cnt = 0
    point1, point2 = 0, 0
    while point1 < len(x):
        if x[point1] == 1:
            point2 = point1 + 1
            cnt = 1
            while (point2 < len(x)) and x [point2] == 1:
                cnt += 1
                point2 += 1 
            if cnt > main_cnt:
                main_cnt = cnt
            point1 += 1 
        else:
            point1 += 1
    return main_cnt   


########################
# PROBLEM 6
########################
#INPUT non-negative integer
#OUTPUT True if divisible by 9, False otherwise

def div_9(x):
    tmp = []
    xString = str(x)
    for i in xString:
        tmp.append(int(i))
    
    for digit in tmp:
        my_sum = sum(tmp)
    
    tmp2 = []
    num = str (my_sum)
    for n in num:
        tmp2.append(int(n))

    for m in tmp2:
        sum1 = sum(tmp2)
        if sum1 == 9:
            return True 
        elif sum1 == 0:
            return True 
        else:
            return False
        


########################
# PROBLEM 7
########################
#INPUT string base 17 A:10, B:11,..., F:15, G:16
#OUTPUT decimal 
def secdec_dec(n):
    rubric = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
              'a':10,'b':11,'c':12,'d':13,'e':14,'f':15,'g':16}
 
    count = len(str(n))
    final_lst = []
    for a in str(n).lower():
        final_lst.append(rubric[a] * (17**(count-1)))
        count -= 1
    return sum(final_lst)



########################
# PROBLEM 8
########################

# INPUT: integers x and y 
# OUPUT: Ouptut of recursive functions d() and e() as shown in the PDF
def d_1(x,y):
    if x == 1:
        return 1
    elif x == 0:
        return y 
    else:
        return d_1(max(x,y) % min(x,y), min(x,y))

def e_1(x,y):
    if d_1(x,y) == 1:
        return (x * y)
    else:
        c = d_1(x,y)
        
        return c * e_1(x // c, y // c)



########################
# PROBLEM 9
########################
# INPUT: a list of integers
# OUTPUT: As shown by the recursive function in the PDF
def m(lst):
    if len(lst) < 2:
        return []
    elif len(lst) == 2:
        return [[lst[0] + lst[1]]]
    else:
        bee = [lst[i] + lst[i + 1] for i in range(len(lst) - 1)]
        return m(bee) + [bee]

########################
# PROBLEM 10
########################

# INPUT: list of candies
# Total empty space
# Please don't be confused by the fact that PDF shows the function accepting only one argument i.e. 'c' but here 
# we have two arguments i.e. 'c' and 'space', it will still work if you call package() with just one argument - package([3,3,3]) 
# because we have fixed space = 9, so Python will take that value as default even if you don't pass 'space' 
# explicitly in the test case (default value of space is 9).
def package(candies, space=9):
    if candies == []:
        return space
    c = candies[0]
    if candies[0] <= space:
        return package(candies[1:],space - c)
    else:
        return package(candies, space + 9)


########################
# PROBLEM 11
########################

def encode(msg,shift):
    pass

def decode(msg,shift):
    pass




if __name__ == "__main__":


    # Problem 1
    # p(0) = 10000
    # p(1) = 10200.0
    # p(2) = 10404.0
    # p(3) = 10612.08
    # p(4) = 10824.3216
    for i in range(5):
        print(p(i))
 
    
    for i in range(2,6):
        print(c(i))
    print(c(1))
    # c(2) = 82
    # c(3) = 756
    # c(4) = 7048
    # c(5) = 66384    

    for i in range(5):
        print(d(i))
    # d(0) = 1
    # d(1) = 4
    # d(2) = 13
    # d(3) = 40
    # d(4) = 121
    
    for i in range(6):
        print(f(i))
    # f(0) = 1
    # f(1) = 1
    # f(2) = 2
    # f(3) = 3
    # f(4) = 5
    # f(5) = 8

    for i in range(1,6):
        print(e(i))
    # e(1) = 12
    # e(2) = -60
    # e(3) = 300
    # e(4) = -1500
    # e(5) = 7500

    for i in range(5):
        for j in range(5):
            print(M(i,j), " ", end="")
    # M((0, 0)) = 1
    # M((0, 1)) = 1
    # M((0, 2)) = 1
    # M((0, 3)) = 1
    # M((0, 4)) = 1
    # M((1, 0)) = 6
    # M((1, 1)) = 5
    # M((1, 2)) = 4
    # M((1, 3)) = 3
    # M((1, 4)) = 2
    # M((2, 0)) = 6
    # M((2, 1)) = 5
    # M((2, 2)) = 4
    # M((2, 3)) = 3
    # M((2, 4)) = 2
    # M((3, 0)) = 6
    # M((3, 1)) = 5
    # M((3, 2)) = 4
    # M((3, 3)) = 3
    # M((3, 4)) = 2
    # M((4, 0)) = 0
    # M((4, 1)) = 0
    # M((4, 2)) = 0
    # M((4, 3)) = 0
    # M((4, 4)) = 0    

    for i in range(2,6):
        print(c_2(5,i))
    # c_2(5,2) = 10
    # c_2(5,3) = 10
    # c_2(5,4) = 5
    # c_2(5,5) = 1

    # problem 2
    # x2 = [7, -9, 5, 10, -9, 6, 9, 3, 3, 9]
    # print(msi(x2))

    #problem 3
    # data3 = [[1,0],[0,1,0,1,0,1,0],[1,1,1,1,0,0,0,0],[0,1,0,1,1], [1,1,0,1],[0,0,1,0,1,1],[1,0,0,0,1,1,1]]
    # for d in data3:
    #     print(f"{d} => {move(d)}")
    

    # #Problem 4
    # data1 = [["a", "b", "a", "c", "c", "a"],[1],[1,2,3,4]]
    # # 1.46, -0.0, 2.0; 0 is minimal, log(n) is maximal
    # for d in data1:
    #     print(entropy(d)) 
 
    # # #Problem  5
    # data2 = [[0],[1],[1,1,0,1,1,1],[0,1,1,0],[0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    # for d in data2:
    #     print(L(d))

    # # #Problem 6
    # data3 = [99,0,18273645,22,27]
    # for d in data3:
    #     print(div_9(d), not bool(d % 9))

    # # # Problem 7
    # data4 = ["G2","100","10","GA3","G","E2"]
    # for d in data4:
    #     print(secdec_dec(d), int(d,17))
    
       
    # # problem 8
    # data = [[15,25],[6,7],[1,1],[1,2],[0,4],[210,2310]]
    # for i in data:
    #     print(e(*i))

    #problem 9
    # x = [[1,2,3,4,5],[1],[3,4],[5,10,22],[1,2,3,4,5,6]]
    # for i in x:
    #     print(m(i))

    #problem 10
    # candies = [[3,3,3],[3,1,2,2,1],[1,2,2,2,3],[3,2,2,3,1,3]]
    # for c in candies:
    #     print(package(c))
    
    #problem 11

    # data = ["abc xyz","the cat", "i love ctwohundred"]
    # for i,j in enumerate(data,start=2):
    #     print(f"original msg {j}")
    #     print(f"encoded  msg {encode(j,i)}")
    #     print(f"decoded  msg {decode(encode(j,i),i)}")

    # secret_msg = encode("the quick brown fox jumps over the lazy dog", 24)
    # print(secret_msg)
    # print(decode(secret_msg,24))
    print()