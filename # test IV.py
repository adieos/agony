# exceptions
try:
    presiden = int(input("Joko: "))
    wapresiden = int(input("Widodo: "))
    negara = presiden/wapresiden
except ZeroDivisionError:
    print("Hey! You cannot divide by zero!")
except ValueError:
    print("Please, only use numbers!")
except Exception as ex: # type(exception).__name__ to see the exception name !
    print("Unknown error occured.")
    print("Details: ")
    print("Error type: {0}".format(type(ex).__name__))
    print(ex)
else: # executed IF no exception is raised
    print(negara)
finally: # executed regardless of error's presence
    print("I will always present :-)")

