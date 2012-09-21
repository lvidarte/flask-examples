import string
import random

key = ''.join(random.sample(string.printable, 24))
print repr(key)
