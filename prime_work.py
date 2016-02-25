def NP(function, num):
    '''Parent function to access prime and primelist'''
    #Reads the primes text file
    with open('list_of_primes_doc.txt', 'r') as list_of_primes:
            #Converts the data to a list
            primes = eval(list_of_primes.read())
    
    def prime(num):
        #Weeds out non-integers from the test
        if round(float(num)) != float(num): 
            return "Requires an integer value."
        #Weeds out 1 from the test.
        if num == 1: 
            return "1 isn't prime."
        if num in primes:
            return True
        temp = 0
        #Divides the number by every natural number less than it
        while primes[temp] < num / 2:
            remainder = num % primes[temp]
            #If the number ever divides evenly, it returns False
            if remainder == 0:
                return False
            temp += 1
            #Adds to the list if it reaches the end and hasn't found an answer yet
            if temp >= len(primes):
                primelist(temp)
        #Otherwise, the number must be prime, so it returns true
        return True

    #Generates a certain number of primes up to an index
    def primelist(index): 
        
        #Starts by checking the last prime in the list
        check = primes[len(primes) - 1] + 1
        #Goes until it reaches the index
        while len(primes) < index + 1:
            if prime(check):
                primes.append(check)
            check += 1
    #Runs the prime function if specified
    if function == 'prime':
        if(prime(num)):
            return True
        else:
            return False
    #Runs the primelist function if specified
    if function == 'primelist':
        primelist(num)
        #Rewrites the new prime list to the text document
        with open('list_of_primes_doc.txt', 'w') as list_of_primes:
            list_of_primes.write(str(primes))
        print('This is a list of primes up to index-' + str(num))
        return primes[:(num + 1)]
        
        
    
