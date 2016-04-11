# SOLUTIONS!

################################################################
# PART ONE


# 1. Write a function that does not take any arguments and
#    prints "Hello World".
def greeting():
    """ Print 'Hello World' """

    print "Hello World"


# 2. Write a function that takes a name as a string and
#    prints "Hi" followed by the name.
def name_greeting(name):
    """ Print 'Hi' followed by the input name """

    print "Hi", name


# 3. Write a function that takes two integers and multiplies
#    them together. Print the result.
def multiply_nums(num1, num2):
    """ Multiply the first input number by the second input number """
    total = num1 * num2

    print total


# 4. Write a function that takes a string and an integer and
#    prints the string that many times
def string_multiply(string, n):
    """ Print the input string as many times as the input number given """

    times = string * n

    print times


# 5. Write a function that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If integer is 0 print "Zero".
def higher_than_lower_than(num):
    """ Print 'Higher than 0' if input number is greater than 0,
    Print 'Lower than 0' if input number is less than 0,
    Print 'Zero' if input number is 0
    """
    if num > 0:
        print "Higher than 0"
    elif num < 0:
        print "Lower than 0"
    elif num == 0:
        print "Zero"


# 6. Write a function that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.

def divisible_num(num):
    """ Return a boolean if the input number is evenly divisible by 3 """

    while True:
        if num % 3 == 0:
            return True
        else:
            return False


# 7. Write a function that takes a sentence as one string and
#    returns the number of spaces.



# 8. Write a function that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.

def calculate_meal_total(price, tip=15):
    """ Return total amount of input price and input tip.
    If no tip given default to 15% """

    tip_total = float(price) * (float(tip) / 100)
    total_price = tip_total + price

    return round(total_price, 2)


# 9. Write a function that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#	 should be returned in a list.
#
# 	Then, write code that shows the calling of this function
# 	on a number and unpack what is returned into two
# 	variables --- sign and parity (whether it's positive
# 	or negative). Print sign and parity.


################################################################
# PART TWO


# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).
#
#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviaton, and the
#    default tax amount as parameters.
#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item including tax.

# 2. Turn the block of code from the directions into a function.
#	 Take a name and a job title as parameters, making it so the
# 	 job title defaults to "Engineer" if a job title is not passed in.
#	 Return the person's title and name.
def job_title(name, title='Engineer'):
    """ Print input name and input title as a string.
    Default title to 'Engineer' """

    print title + ' ' + name


# 3. Given a receiver's name, receiver's job title, and sender's name, print the following letter:      
#       Dear JOB_TITLE RECEIVER_NAME, I think you are amazing! Sincerely,
#       SENDER_NAME. 
#    Use the function from #2 to construct the full title for the letter's greeting.

# 4. Turn the block of code from the directions into a function. This
#    function will take a number and append it to *numbers*. It doesn't
#    need to return anything.
