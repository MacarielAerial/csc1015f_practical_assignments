#testnumberutil.py
"""
>>> import numberutil
>>> numberutil.aswords(0)
'zero'
>>> numberutil.aswords(20)
'twenty'
>>> numberutil.aswords(30)
'thirty'
>>> numberutil.aswords(21)
'twenty one'
>>> numberutil.aswords(900)
'nine hundred'
>>> numberutil.aswords(920)
'nine hundred and twenty'
>>> numberutil.aswords(930)
'nine hundred and thirty'
>>> numberutil.aswords(921)
'nine hundred and twenty one'

"""
import doctest
doctest.testmod(verbose=True)

