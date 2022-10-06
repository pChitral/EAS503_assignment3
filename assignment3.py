def ex1(password):
    # In this exercise you will complete this function to determine whether or not
    # a password is good. We will define a good password to be a one that is at least
    # 8 characters long and contains at least one uppercase letter, at least one lowercase
    # letter, at least one number, and at least one of the following special characters (!, @, #, $, ^).
    # This function should return True if the password
    # passed to it as its only parameter is good. Otherwise it should return False.
    #
    # input: password (str)
    # output: True or False (bool)
    # BEGIN SOLUTION

    special_char = ["!", "@", "#", "$", "^"]

    for char in password:
        if char in special_char:
            has_special_char = True
            break
        else:
            has_special_char = False

    if len(password) > 7:
        pass_len_7plus = True
    else:
        pass_len_7plus = False

    if not password.islower() and not password.isupper() and pass_len_7plus and has_special_char:
        return True
    else:
        return False

    # END SOLUTION


def ex2(sentence):
    # Complete this function to calculate the average
    # word length in a sentence
    # Input: sentence
    # Output: average word length in sentence
    # Hint: count punctuations with whatever word they are `touching`
    # Hint: round the average to two decimal places

    # BEGIN SOLUTION
    word_len = []

    list_of_words = sentence.split()
    for word in list_of_words:
        word_len.append(len(word))

    average_word_len = round(sum(word_len) / len(word_len), 2)
    return average_word_len
    # END SOLUTION


def ex3(filename):
    # Complete this function to count the number of lines, words, and chars in a file.
    # Input: filename
    # Output: a tuple with line count, word count, and char count -- in this order

    # BEGIN SOLUTION
    with open(filename, "r") as raw_file:
        entire_file = raw_file.read()

    list_of_lines = entire_file.split(".")

    """ 
    Splitting on "." will give us an empty string in the last which indeed would be counted as a line. 
    Thus, to get rid of that empty string we rewrite our list without considering that empty string.
    """
    list_of_lines = list_of_lines[:len(list_of_lines)-1]
    number_of_lines = len(list_of_lines)  # part 1 of the question done

    # Before doing anything, lets strip out the spaces and get rid of the unnecessary characters, which may skew the results.
    for i in range(len(list_of_lines)):
        list_of_lines[i] = list_of_lines[i].replace("\n", "").strip()

    # Here we'll count the total number of words in a line using a for loop
    number_of_words = 0

    # Lets calulate the list of list of words first
    list_of_list_of_words = []

    for line in list_of_lines:
        list_of_list_of_words.append(line.split(" "))

    # Now we'll calculate the total number of words
    number_of_words = 0
    for line in list_of_list_of_words:
        number_of_words += len(line)

    number_of_characters = 0

    for list_of_wordss in list_of_list_of_words:
        for word in list_of_wordss:
            number_of_characters += len(word)

    final_answer_tuple = (
        number_of_lines, number_of_words, number_of_characters)

    return final_answer_tuple
    # END SOLUTION


def ex4(apr):
    # Complete this function to use a while loop to determine how long it takes for an investment
    # to double at a given interest rate. The input to this function, apr, is the annualized interest rate
    # and the output is the number of years it takes an investment to double. Note: The amount of the initial
    # investment (principal) does not matter; you can use $1.
    # Hint: principal is the amount of money being invested.
    # apr is the annual percentage rate expressed as a decimal number.
    # Relationship: value after one year is given by principal * (1+ apr)

    # BEGIN SOLUTION
    value = principal_amount = 1
    year = 0
    while (value < 2 * principal_amount):
        value = value * ((apr) + 1)
        year = year + 1
    return year
    # END SOLUTION


def ex5(n):
    # Complete this function to return the number of steps taken to reach 1 in
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

    # BEGIN SOLUTION
    pass
    # END SOLUTION


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
    # Inputs: m and n which are both natural numbers
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
    with open("ex9_data.txt", "r") as raw_file:
        entire_file = raw_file.read()

    list_of_student_names_and_marks = entire_file.split("\n")
    list_of_student_names_and_marks = list_of_student_names_and_marks[::2]
    maal = []
    for i in range(len(list_of_student_names_and_marks)):
        maal.append(list_of_student_names_and_marks[i].split(","))
    dicto = {}
    list_of_dicts = []
    for i in range(len(maal)-1):
        dicto["name"] = (maal[i][0])
        dicto["marks"] = [eval(i) for i in (maal[i][1:])]
        list_of_dicts.append(dicto)

    # END SOLUTION
ex9("ex9_data.txt")


def ex10(data, num_outliers):
    # When analyzing data collected as a part of a science experiment it
    # may be desirable to remove the most extreme values before performing
    # other calculations. Complete this function which takes a list of
    # values and an non-negative integer, num_outliers, as its parameters.
    # The function should create a new copy of the list with the num_outliers
    # largest elements and the num_outliers smallest elements removed.
    # Then it should return teh new copy of the list as the function's only
    # result. The order of the elements in the returned list does not have to
    # match the order of the elements in the original list.
    # input1: data (list)
    # input2: num_outliers (int)
    data.sort()
    for i in range(num_outliers):
        data.remove(max(data))
        data.remove(min(data))
    return data

    # output: list

    # BEGIN SOLUTION
    pass
    # END SOLUTION


def ex11(words):
    # Complete this function to remove duplicates from the words list using a loop
    # input: words (list)
    # output: a list without duplicates
    # MUST USE loop and NOT set!
    # Preserve order

    # BEGIN SOLUTION
    no_duplicates = []
    [no_duplicates.append(word) for word in words if word not in no_duplicates]
    return no_duplicates
    # END SOLUTION


def ex12(n):
    # A proper divisor of a  positive integer, n, is a positive integer less than n which divides
    # evenly into n. Complete this function to compute all the proper divisors of a positive
    # integer. The integer is passed to this function as the only parameter. The function will
    # return a list of containing all of the proper divisors as its only result.

    # input: n (int)
    # output: list

    # BEGIN SOLUTION
    proper_divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            proper_divisors.append(i)
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
    if sum == n:
        return True
    else:
        return False
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



    # END SOLUTION


def ex15(title, header, data, filename):
    # This problem is hard.
    # Open up ex15_*_solution.txt and look at the output based on the input parameters, which
    # can be found in the test_assignment4.py file
    # Function inputs:
    # title -- title of the table -- a string
    # header -- header of the table  -- a tuple
    # data -- rows of data, which is a tuple of tuples
    # filename -- name of file to write the table to
    # Your job is to create the table in the file and write it to `filename`
    # Note that you need to dynamically figure out the width of each column based on
    # maximum possible length based on the header and data. This is what makes this problem hard.
    # Once you have determined the maximum length of each column, make sure to pad it with 1 space
    # to the right and left. Center align all the values.
    # OUTPUT: you are writing the table to a file

    # BEGIN SOLUTION
    pass
    # END SOLUTION


def ex16(lst):
    # Complete this function to use list comprehension to return all values from `lst`
    # that are a multiple of 3 or 4. Just complete the list comprehension below.
    # input: `lst` of numbers
    # output: a list of numbers

    # BEGIN SOLUTION
    # complete the following line!
    # return [for ele in lst] #complete this line!
    pass  # remove this line
    # END SOLUTION


def ex17(lst):
    # Complete this function to use list comprehension to multiple all numbers
    # in the list by 3 if it is even or 5 if its odd
    # input: `lst` of numbers
    # output: a list of numbers

    # BEGIN SOLUTION
    # complete the following line!
    # return [for ele in lst] #complete this line!
    pass  # remove this line
    # END SOLUTION


def ex18(input_dict, test_value):
    # Complete this function to find all the keys in a dictionary that map to the input value.
    # input1: input_dict (dict)
    # input2: test_value
    # output: list of keys

    # BEGIN SOLUTION
    pass
    # END SOLUTION


def ex19(filename):
    """
    In this problem you will read data from a file and perform a simple mathematical operation on each data point. 
    Each line is supposed to contain a floating point number.
    But what you will observe is that some lines might have erroneous entries. 
    You need to ignore those lines (Hint: Use Exception handling).

    The idea is to implement a function which reads in a file and computes the median 
    of the numbers and returns the output. You may use the inbuilt function sort when computing the median.

    DO NOT USE ANY INBUILT OR OTHER FUNCTION TO DIRECTLY COMPUTE MEDIAN

    The files
    """
    # BEGIN SOLUTION
    pass
    # END SOLUTION


def simulateProblem():
    """
    See instructions in exercise_19_instructions.html file
    """
    # BEGIN SOLUTION
    pass
    # END SOLUTION


def ex20():
    """
    The function calls the simulateProblem() 10000 times to figure out 
    the empirical (observed) probability of gaining more money when switching 
    and gaining more money when sticking to the original choice.
    Return the probability of win due to sticking and win due to switching
    """
    # BEGIN SOLUTION
    pass
    # END SOLUTION
