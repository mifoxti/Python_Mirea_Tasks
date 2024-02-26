import random
import string

max_size = 10
result = ''.join(random.choices(string.ascii_letters + string.digits, k=max_size))
