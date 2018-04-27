#timeutilchecker.py
"""
>>> import timeutil
>>> timeutil.validate("149 p.m.")
False
>>> timeutil.validate("100:49 p.m.")
False
>>> timeutil.validate("01:49 p.m.")
False
>>> timeutil.validate("1:49 pm")
False
>>> timeutil.validate("1:490 p.m.")
False
>>> timeutil.validate("1:49 p.m.")
True

"""
import doctest
doctest.testmod(verbose=True)
