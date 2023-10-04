import re

my_pattern = r"[A-Z][\w\s,']*today[\w'\s,]*[\.?]*"
my_regex = re.compile(my_pattern)
