
# if user will enter not a number, but a letter, words, strings, etc for (enter) variable - error is inevitable
# using error processing operators to prevent an error from occurring
# also using while loop to repeat the loop until the user enters a suitable value

while True:
    try:                  # the section of code in which an error can occur is written in the block (try)
        enter = float(input("Enter a number: "))
        print(100/enter)
        break
    except ValueError:    # for the (except) operator need to clarify the type of error so that it intercepts it
        print("You enter not a number!")  # and after interception will reproduce the prepared code preventing the error
    except ZeroDivisionError:             # another possible error in this loop , so using except operator again
        print("Can't divide by zero!")
    else:                # operator (else) works only when there were not any errors in the (try) block
        print("Wow, You did great and and enter the correct value with the first attempt!")
    finally:             # the code written in finally operator works always (code is always executed)
        print("Will be working always!!")  # even if there was an error in (try) block ,
# even if there was an error in (try) block , the code from (finally) operator will be always executed

print("the program continues to work")


# context manager ( with , as)
# allows to work with resources that require closure in case of an error safely (saves data processed before the error)
# but can not do anything with error itself
with open("/Users/air/Desktop/ErrorTest.txt", "a") as r:   # (with) function (open) (as) variable r
    r.write("something" + "\n")                         # same as r = open("/Users/air/Desktop/ErrorTest.txt", "a")
#    10/0                             # random error
    r.write("something23")

print("continue to work")

