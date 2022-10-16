def ex1(password):
    # In this exercise you will complete this function to determine whether or not
    # a password is good. We will define a good password to be a one that is at least
    # 8 characteraracters long and contains at least one uppercase letter, at least one lowercase
    # letter, at least one number, and at least one of the following special characteraracters (!, @, #, $, ^).
    # This function should return True if the password
    # passed to it as its only parameter is good. Otherwise it should return False.
    #
    # input: password (str)
    # output: True or False (bool)
    # BEGIN SOLUTION

    special_characterar = ["!", "@", "#", "$", "^"]

    for characterar in password:
        if characterar in special_characterar:
            has_special_characterar = True
            break
        else:
            has_special_characterar = False

    pass_len_7plus = True if len(password) > 7 else False

    return True if not password.islower() and not password.isupper() and pass_len_7plus and has_special_characterar else False

    # END SOLUTION


def ex2(sentence):
    # Complete this function to calculate the average
    # word length in a sentence
    # Input: sentence
    # Output: average word length in sentence
    # Hint: count punctuations with whatever word they are `toucharactering`
    # Hint: round the average to two decimal places

    # BEGIN SOLUTION
    word_len = [len(word) for word in sentence.split()]

    return round(sum(word_len) / len(word_len), 2)
    # END SOLUTION


def ex3(filename):
    # Complete this function to count the number of lines, words, and characterars in a file.
    # Input: filename
    # Output: a tuple with line count, word count, and characterar count -- in this order

    # BEGIN SOLUTION
    number_of_lines = 0
    number_of_words = 0
    number_of_characteraracters = 0

    with open(filename, 'r') as file:
        for line in file:
            # It is very important that we calculate the number of characteraracters before splitting the line on \n since we would be loosing that characteraracter and the answerults would be nothing if not inaccurate
            number_of_characteraracters += len(line)
            line = line.strip("\n")
            words = line.split()
            number_of_lines += 1
            number_of_words += len(words)

    return (number_of_lines, number_of_words, number_of_characteraracters)

    # END SOLUTION


def ex4(apr):
    # Complete this function to use a while loop to determine how long it takes for an investment
    # to double at a given inteanswert rate. The input to this function, apr, is the annualized inteanswert rate
    # and the output is the number of years it takes an investment to double. Note: The amount of the initial
    # investment (principal) does not matter; you can use $1.
    # Hint: principal is the amount of money being invested.
    # apr is the annual percentage rate expanswersed as a decimal number.
    # Relationship: value after one year is given by principal * (1+ apr)

    # BEGIN SOLUTION
    value = principal_amount = 1
    year = 0
    while (value < 2 * principal_amount):
        value = value * ((apr) + 1)
        year += 1
    return year
    # END SOLUTION


def ex5(n):
    # Complete this function to return the number of steps taken to reacharacter 1 in
    # the Collatz sequence (https://en.wikipedia.org/wiki/Collatz_conjecture) given in

    # BEGIN SOLUTION
    number_of_steps = 0
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        number_of_steps += 1
    return number_of_steps

    # END SOLUTION


def ex6(n):
    # A positive whole number > 2 is prime if no number between 2 and sqrt(n)
    # (include) evenly divides n. Write a program that accepts a value of n as
    # input and determine if the value is prime. If n is not prime, your program should
    # return False (boolean) as soon as it finds a value that evenly divides n.
    # Hint: if number is 2, return False

    import math
    if n == 2:
        return False
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True


def ex7(n):
    # Complete this function to return all the primes as a list less than or equal to n
    # Input: n
    # Output: a list of numbers
    # hint use ex6

    # BEGIN SOLUTION
    primes = []
    for i in range(2, n+1):
        if ex6(i):
            primes.append(i)
        else:
            continue
    return primes

    # END SOLUTION


def ex8(m, n):
    # Complete this function to determine the greatest common divisor (GCD).
    # The GCD of two values can be computed using Euclid's algorithm. Starting with the values
    # m and n, we repeatedly apply the formula: n, m = m, n%m until m is 0. At this point, n is the GCD
    # of the original m and n.
    # Inputs: m and n whicharacter are both natural numbers
    # Output: gcd

    # BEGIN SOLUTION
    if m == n:
        return m
    if m == 0:
        return n
    if n == 0:
        return m
    if m > n:
        return ex8(m-n, n)
    if n > m:
        return ex8(n, n-m)

    # END SOLUTION


def ex9(filename):
    # Complete this function to read grades from a file and determine the student with the highest average
    # test grades and the lowest average test grades.
    # Input: filename
    # Output: a tuple containing four elements: name of student with highest average, their average,
    # name of the student with the lowest test grade, and their average. Example ('Student1', 99.50, 'Student5', 65.50)
    # Hint: Round to two decimal places

    # BEGIN SOLUTION
    with open(filename, "r") as raw_file:

        adulterated_list = []
        names = []
        avg = []
        for line in raw_file:
            adulterated_list.append(line.split())
        cleaned_list = adulterated_list[::2]

        for line in cleaned_list:
            names.append(line[0].split(",")[0])
            marks = line[0].split(",")[1:]
            avg.append(round(sum(map(int, marks))/25, 2))
    max_value = max(avg)
    max_index = avg.index(max_value)
    min_value = min(avg)
    min_index = avg.index(min_value)
    return (names[max_index], max_value, names[min_index], min_value)

    # END SOLUTION


def ex10(data, num_outliers):
    # When analyzing data collected as a part of a science experiment it
    # may be desirable to remove the most extreme values before performing
    # other calculations. Complete this function whicharacter takes a list of
    # values and an non-negative integer, num_outliers, as its parameters.
    # The function should create a new copy of the list with the num_outliers
    # largest elements and the num_outliers smallest elements removed.
    # Then it should return teh new copy of the list as the function's only
    # answerult. The order of the elements in the returned list does not have to
    # matcharacter the order of the elements in the original list.
    # input1: data (list)
    # input2: num_outliers (int)

    data.sort()
    for i in range(num_outliers):
        data.remove(max(data))
        data.remove(min(data))
    return data


def ex11(words):
    # Complete this function to remove duplicates from the words list using a loop
    # input: words (list)
    # output: a list without duplicates
    # MUST USE loop and NOT set!
    # Panswererve order

    # BEGIN SOLUTION
    no_duplicates = []
    [no_duplicates.append(word) for word in words if word not in no_duplicates]
    return no_duplicates
    # END SOLUTION


def ex12(n):
    # A proper divisor of a  positive integer, n, is a positive integer less than n whicharacter divides
    # evenly into n. Complete this function to compute all the proper divisors of a positive
    # integer. The integer is passed to this function as the only parameter. The function will
    # return a list of containing all of the proper divisors as its only answerult.

    # input: n (int)
    # output: list

    # BEGIN SOLUTION
    proper_divisors = [i for i in range(1, n+1) if n % i == 0]
    proper_divisors.remove(n)

    return proper_divisors

    # END SOLUTION


def ex13(n):
    # An integer, n, is said to be perfect when the sum of all of the proper divisors
    # of n is equal to n. For example, 28 is a perfect number because its proper divisors
    # are 1, 2, 4, 7, and 14 = 28
    # Complete this function to determine if a the number a perfect number or not.
    # input: n (int)
    # output: True or False (bool)

    # BEGIN SOLUTION
    proper_divisors_list = ex12(n)
    sum = 0
    for number in proper_divisors_list:
        sum += number
    return True if sum == n else False

    # END SOLUTION


def ex14(points):
    # Complete this function to determine the best line.
    # https://www.varsitytutors.com/hotmath/hotmath_help/topics/line-of-best-fit
    # input: points (list of tuples contain x, y values)
    # output: (m, b) # round both values to two decimal places

    # BEGIN SOLUTION
    x = []
    y = []
    for point in points:
        x.append(point[0])
        y.append(point[1])

    x_sum = sum(x)
    y_sum = sum(y)

    x_mean = x_sum / len(x)
    y_mean = y_sum / len(y)

    x_denom = []
    numerator_fina = []

    for i in range(len(x)):
        numerator_fina.append((x[i] - x_mean)*(y[i]-y_mean))
        x_denom.append((x[i] - x_mean)**2)

    slope = sum(numerator_fina)/sum(x_denom)
    b = y_mean - (slope)*(x_mean)
    b = round(b, 2)
    slope = round(slope, 2)

    return (slope, b)

    # END SOLUTION


def ex15(title, header, data, filename):
    # This problem is hard.
    # Open up ex15_*_solution.txt and look at the output based on the input parameters, whicharacter
    # can be found in the test_assignment4.py file
    # Function inputs:
    # title -- title of the table -- a string
    # header -- header of the table  -- a tuple
    # data -- tuples of data, whicharacter is a tuple of tuples
    # filename -- name of file to write the table to
    # Your job is to create the table in the file and write it to `filename`
    # Note that you need to dynamically figure out the horizontal_characterar of eacharacter column based on
    # maximum possible length based on the header and data. This is what makes this problem hard.
    # Once you have determined the maximum length of eacharacter column, make sure to pad it with 1 space
    # to the right and left. Center align all the values.
    # OUTPUT: you are writing the table to a file

    # BEGIN SOLUTION
    lens = []
    for tuple in data:
        summ = 0
        for i in range(len(tuple)):
            lens.append(len(str(tuple[i])) + 2)
            summ += len(str(tuple[i])) + 2
        lens.append(summ)
    
    lens2 = []
    for header_name in header:
        lens2.append(len(str(header_name)) + 2)
    for i in range(len(header)):
        if lens2[i] > lens[i]:
            lens[i] = lens2[i]
        else:
            lens[i] = lens[i]

    max_length = sum(lens[:len(header)])
    print(lens)
    print(max_length)


    with open(filename, "w") as file:

        # Writing the  horizontal line
        
        file.write(f"-"*((  max_length + 4 )))
        file.write("\n")

        # Putting in the title
        file.write("|")
        file.write(f"{title.center(( max_length + 2 ))}")
        file.write("|")
        file.write("\n")

        # Writing the  horizontal line
        for i in range(1):
            for j in range(len(data[i])):
                if (j == (len(header) - 1)):
                    file.write("+")
                    file.write(f"-"*(lens[j]))
                    file.write("+")
                else:
                    file.write("+")
                    file.write(f"-"*(lens[j]))
            file.write("\n")

        # Writing the column names
        i = 1
        for j in range(len(data[i])):
            if (j == (len(header) - 1)):
                file.write("|")
                file.write(f"{header[j].center((lens[j]))}")
                file.write("|")
            else:
                file.write("|")
                file.write(f"{header[j].center((lens[j]))}")
        file.write("\n")

        # Writing the  horizontal line
        for i in range(1):
            for j in range(len(data[i])):
                if (j == (len(header) - 1)):
                    file.write("+")
                    file.write(f"-"*(lens[j]))
                    file.write("+")
                else:
                    file.write("+")
                    file.write(f"-"*(lens[j]))
            file.write("\n")

        # Writing the data
        for i in range(len(data)):
            for j in range(len(data[i])):
                if (j == (len(header) - 1)):
                    file.write("|")
                    file.write(f"{str(data[i][j]).center((lens[j]))}")
                    file.write("|")
                else:
                    file.write("|")
                    file.write(f"{str(data[i][j]).center((lens[j]))}")
            file.write("\n")

        # Writing the last horizontal line
        for i in range(1):
            for j in range(len(data[i])):
                if (j == (len(header) - 1)):
                    file.write("+")
                    file.write(f"-"*(lens[j]))
                    file.write("+")
                else:
                    file.write("+")
                    file.write(f"-"*(lens[j]))
            file.write("\n")


    # END SOLUTION


def ex16(lst):
    # Complete this function to use list comprehension to return all values from `lst`
    # that are a multiple of 3 or 4. Just complete the list comprehension below.
    # input: `lst` of numbers
    # output: a list of numbers

    # BEGIN SOLUTION
    # complete the following line!
    # return [for ele in lst] #complete this line!
    return [ele for ele in lst if ele % 3 == 0 or ele % 4 == 0]
    # END SOLUTION


def ex17(lst):
    # Complete this function to use list comprehension to multiple all numbers
    # in the list by 3 if it is even or 5 if its odd
    # input: `lst` of numbers
    # output: a list of numbers

    # BEGIN SOLUTION
    # complete the following line!
    # return [for ele in lst] #complete this line!
    return [ele*3 if ele % 2 == 0 else ele*5 for ele in lst]
    # END SOLUTION


def ex18(input_dict, test_value):
    # Complete this function to find all the keys in a dictionary that map to the input value.
    # input1: input_dict (dict)
    # input2: test_value
    # output: list of keys

    # BEGIN SOLUTION

    return [key for key in input_dict if input_dict[key] == test_value]

    # END SOLUTION


def ex19(filename):
    """
    In this problem you will read data from a file and perform a simple mathematical operation on eacharacter data point.
    Eacharacter line is supposed to contain a floating point number.
    But what you will observe is that some lines might have erroneous entries.
    You need to ignore those lines (Hint: Use Exception handling).

    The idea is to implement a function whicharacter reads in a file and computes the median
    of the numbers and returns the output. You may use the inbuilt function sort when computing the median.

    DO NOT USE ANY INBUILT OR OTHER FUNCTION TO DIRECTLY COMPUTE MEDIAN

    The files
    """
    # BEGIN SOLUTION
    numbers = []

    with open(filename, "r") as raw_file:
        for line in raw_file.readlines():
            try:
                numbers.append(float(line))
            except:
                pass

    numbers.sort()
    middle_index = len(numbers) // 2
    if len(numbers) == 0:
        return 'The file does not have any valid number to compute the median'

    median = (numbers[middle_index] + numbers[middle_index-1]) / \
        2 if len(numbers) % 2 == 0 else numbers[middle_index]

    return median
    # END SOLUTION


def simulateProblem():
    """
    See instructions in exercise_19_instructions.html file
    """
    # BEGIN SOLUTION
    import random
    first_characteroice = random.randint(0, 1)

    # we'll execute the code undder the if block when we wish to switcharacter the card
    if (random.randint(0, 1)):
        if first_characteroice == 0:
            return [True, False]
        else:
            return [False, True]
    # Else condition deals with the case where we don't wish to pick a new card but stick to the first characteroice
    else:
        if first_characteroice == 0:
            return [False, False]
        else:
            return [True, True]
    # END SOLUTION


def ex20():
    """
    The function calls the simulateProblem() 10000 times to figure out
    the empirical (observed) probability of gaining more money when switcharactering
    and gaining more money when sticking to the original characteroice.
    Return the probability of win due to sticking and win due to switcharactering
    """
    # BEGIN SOLUTION
    stick = 0
    switcharacter = 0

    for i in range(10000):
        outcome, experiment = simulateProblem()
        if [outcome, experiment] == [True, True]:
            stick += 1
        elif [outcome, experiment] == [True, False]:
            switcharacter += 1

    return([stick/10000, switcharacter/10000])

    # END SOLUTION
