def base_converter(num, second_base=2, first_base=10):
    '''Converts an integer from one base (2-10) to another base(2-10).
(int, int, int) -> int'''
    def ten_to_another(num, second_base):
        '''Converts an integer from base 10 to another base (2-10).'''
        temp = num
        times_divided = 0
        
        #Calculates the number of digits needed in the product through division.
        while temp >= 1:
            temp = temp / second_base
            #The number of times the number needs to be divided by the base to get to <1 is the number of digits.
            times_divided += 1
            
        temp = num
        comparison = second_base ** (times_divided-1)
        final_answer = ''
        #Goes over each digit needed for the result.
        for d in range(times_divided):
            increment = 0
            #Uses subtraction to find the value of the digit.
            while temp >= comparison:
                temp = temp - comparison
                increment += 1
            comparison /= second_base
            #Adds the value to a string for the final answer.
            final_answer = final_answer + str(increment)
        #Returns the final answer by converting the former string into an integer.
        return int(final_answer)
    
    def another_to_ten(num, first_base):
        '''Converts an integer from one base (2-10) to base 10.'''
        #Divides the number into digits
        divided = list(str(num))
        #Calculates the value of the far left digit in the number.
        powers = first_base ** (len(divided) - 1)
        final_answer = 0
        #Goes over each digit in the given number.
        for d in divided:
            #Adds the digit multiplied by its value to the final answer.
            final_answer += (int(d) * powers)
            #Changes the value for the next right digit.
            powers /= first_base
        #Returns the sum of all the digits with their respective weights.
        return final_answer
    #Converts to ten before converting to the desired base to utilize the ten_to_another function.
    if(first_base != 10):
        return ten_to_another(another_to_ten(num, first_base), second_base)
    #Converts straight from ten to another base if that is all that is necessary.
    else:
        return ten_to_another(num, second_base)
