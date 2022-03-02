''
from unittest import TestResult

'''
Tester
'''


from methods import account

user1 = account("Naiane", 1000)
user2 = account("Jonas",10000)

test_transfer = user1.transfer(500,user2)
print(test_transfer)