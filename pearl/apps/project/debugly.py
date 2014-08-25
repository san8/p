
'''


def debugger(func):
    """
    Decorator to print the name, start, end of a function.
    """
    def wrapper(*args, **kwrgs):
        print func.__name__
        print "started"
        func(*args, **args)
        print "completed"
    return wrapper

    
'''
