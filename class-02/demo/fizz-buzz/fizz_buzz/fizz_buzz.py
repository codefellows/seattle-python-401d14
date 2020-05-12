def fizz_buzz(num):
    """
    Describe your function
    """

    # output = ''

    # if not num % 3:
    #     output = 'Fizz'

    # if not num % 5:
    #     output += 'Buzz'


    # return output or str(num)

    if not num % 15:
        return 'FizzBuzz'
    elif not num % 3:
        return 'Fizz'
    elif not num % 5:
        return 'Buzz'


    return str(num)
