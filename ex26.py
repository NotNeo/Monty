import ex25 as ex25
# See line 95 for explanation of above import

def break_words(line):
    """This function will break up words for us."""
    line = line.split(" ")
    return line
# Part of the problem is that line = line.split(" ") was written as, stuff.split() - stuff was not defined
# Changed 'words' to 'line' too relieve shadowing warning (more than one function or method using the same parameter)
# See line 85 for next set of changes



def sort_words(words):
    """Sorts the words."""
    return sorted(words)


def first_word(words):
    """Prints the first word after popping it off."""
    word = words[0]
    print word


def last_word(word):
    """Prints the last word after popping it off."""
    word = words[-1]
    print word

#-----------------------------------------------------------------------------------------------------------------------
def sort_sentence(x):                                               # These functions were defined using the same param
    """Takes in a full sentence and returns the sorted words."""    # as their arg (sentence) - remember, you want
    words = break_words(x)                                          # parameter values that are universal and don't
    return sort_words(words)                                        # cross with global vars or args - changed to
                                                                    # x, y, & z - other names would be ideal but in this
                                                                    # case, it'll do just to demonstrate the difference.
def first_and_last(y):
    """Prints the first and last words of the sentence."""
    words = break_words(y)
    first_word(words)
    last_word(words)


def first_and_last_sorted(z):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(z)
    print first_word(words)
    print last_word(words)
#-----------------------------------------------------------------------------------------------------------------------

# This works fine now.
print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\t The lovely world 
with logic so firmly planted cannot discern \n the needs of love 
nor comprehend passion from intuition 
and requires an explantion
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"


five = 10 - 2 + 3 - 6 # math was wrong on this line
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
jelly_beans, jars, crates = secret_formula(start_point)  # beans was not defined. Changed to reflect 'jelly_beans'

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (jelly_beans, jars, crates)

start_point /= 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)


# Start of problems... Traceback indicates issue with line 89 and line 3
sentence = "All good\tthings come to those who wait."


words = break_words(sentence)

# Can't reference an external class, module, function, variable, or file without import
sorted_words = ex25.sort_words(words)


first_word(words)
last_word(words)

# Sorted_words is assigned the return value of ex25.sort_words() - which returns an object, you can't sort an object,
# so you have to convert it to a string - str(sorted_words) - converts sorted_words's type value (object) to str (string)
first_word(str(sorted_words))
isinstance(sorted_words, str)

# Same as line 104
last_word(str(sorted_words))
sorted_words = sort_sentence(sentence)

print sorted_words
print first_and_last(sentence)
print first_and_last_sorted(sentence)
