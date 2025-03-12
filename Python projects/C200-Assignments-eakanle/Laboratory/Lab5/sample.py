def find_error3(name1, name2, name3):
    
    greetings = "Hey: "+ name1 +" "+ name2 +" "+ name3
    return(greetings)



# Run the funciton to see how it behaves
print(find_error3("Clarence Ellis", "Dorothy Vaughan", "Lyndsey Scott")) # "Clarence Ellis", "Dorothy Vaughan", "Lyndsey Scott"



def find_error4():
    givenList = [456, 45, 6, 7, 8, 765, 89, 12, 43 , 1589 , 547 , 879] 
    newList = []

    for i in givenList:
        newList += [i+1]
    
    return(newList)


# Run the funciton to see how it behaves
print(find_error4())


def find_error5(list1, list2):
    
    my_sum  = 0
    for i in range(len(list1)):
        my_sum += int(list1[i]) + int(list2[i])
    return my_sum



# Run the funciton to see how it behaves
print(find_error5([34, 56, 78, 100], [100, 200, 500, "23"]))

def addFive (x):
	"""
	Adds 5 to each item in list x and returns a new list
	"""
	finalList = []
	for i in x:
		result = i + 5
		finalList = finalList + [result]
	return finalList
print(addFive([3, 1, 5]))


def parseDoc (mostCommon, letter):
	"""
	Given some list containing the most common words in a document and a 		given letter, return a new list containing the all of the words that start 	with a the given letter. You can assume that the first letter of each word 	is lower case. 
	"""
	letterList = []
	for word in mostCommon:
		if letter == word[0]:
			letterList += [word]
	return letterList
print(parseDoc(["hello", "apple", "dog", "habit", "health"], "h"))


def even (x):
	"""
	Counts how many even numbers in a list
	""" 
	count = 0
	for i in x:
		i=int(i)
		if i % 2 == 0:
			count += 1
	return count
print(even(['1','2','3','4','5']))


def stringPractice (word1, word2):
	"""
	Given two words of equal length, return whether the two words are the 	same.
	"""
	same = True
	for i in range (len(word1)):
		if word1[i] != word2[i]: 
			same = False
			return same
print(stringPractice('sentence', 'sequence'))



dic = {(0 ,1): " good " ,(1 ,0): " bad ", (1 ,1): " ugly " }
 
x = [1, 1]
 
for k , v in dic.items():

    if k == x :
        
        print(v)