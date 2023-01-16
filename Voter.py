class Voter(object):
    # __init__ is a special method called whenever you try to make
    # an instance of a class. As you heard, it initializes the object.
    # Here, we'll initialize some of the data.
    def __init__(self):
        # Let's add some data to the [instance of the] class.
        self.position = (100, 100)
        self.velocity = (0, 0)

    # We can also add our own functions. When our ball bounces,
    # its vertical velocity will be negated. (no gravity here!)
    def bounce(self):
        self.velocity = (self.velocity[0], -self.velocity[1])

   


