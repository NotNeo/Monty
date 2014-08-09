def method_one():
    print "How old are you?",
    age = raw_input ()
    print "How tall are you?",
    height = raw_input ()
    print "How much do you weigh?",
    weight = raw_input ()

    print "So you're %r old, %r tall and %r heavy." % (age, height, weight)


def method_two():
    print "How old are you?",
    age = raw_input()
    print "How tall are you?",
    height = raw_input()
    print "How much do you weigh?",
    weight = raw_input()

    print "So you're " + age + " years old, " + height + " tall and " + weight + " lbs heavy."