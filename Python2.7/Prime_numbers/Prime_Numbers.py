
def is_prime_func(number):
    '''
        Takes in a Number and determines if it is a Prime Number
        
        Args: A Number
        
        Returns: True or False
    '''
    is_prime = True
    # make sure n is a positive integer
    n = abs(int(number))
    # 0 and 1 are not primes
    if n < 2:
        is_prime = False
    #############################
    # 2 is the only even prime number
    elif n == 2: 
        is_prime = True
    # all other even numbers are not primes
    elif n % 2 == 0: 
        is_prime = False
    else:
        # range starts with 3 and only needs to go up the squareroot of n
        # for all odd numbers
        for x in range(3, int(n**0.5)+1, 2):
            if n % x == 0:
                is_prime = False
    return is_prime



def find_1000_prime():
    '''
        Finds what the 1000th Prime number is
        
        Args: None
        
        Returns: The 1000th Prime Number
    '''
    current_number = 2
    count = 0
    while True:
        is_prime = is_prime_func(current_number)
        if is_prime:
            count += 1
        if count == 1000:
            return current_number
        else:
            current_number +=1


def find_primes(end_number):
    '''
        Finds all Prime numbers up to and including an End Number.
        
        Args: A User Entered Number to End our Loop
        
        Returns: A List of Prime Numbers
    '''
    primes = []
    for n in range(2,end_number+1):
        is_prime = is_prime_func(n)
        if is_prime:
            primes.append(n)

    return primes


def main():
    print 'Prime Numbers'
    print '='*40
    print ""

    thous_prime = find_1000_prime()

    if thous_prime:
            print ""
            print 'The 1000th Prime Number is:', int(thous_prime)

    else:
            print "Sorry, Error Occured"



if __name__ == '__main__':
    main()

