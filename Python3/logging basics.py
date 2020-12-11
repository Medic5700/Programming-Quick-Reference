'''
https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
'''

'''
Included for reference from https://docs.python.org/3/howto/logging.html#logging-basic-tutorial

Level       When it’s used
DEBUG       Detailed information, typically of interest only when diagnosing problems.
INFO        Confirmation that things are working as expected.
WARNING     An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
ERROR       Due to a more serious problem, the software has not been able to perform some function.
CRITICAL    A serious error, indicating that the program itself may be unable to continue running.
'''

import logging

#default logging level is 'WARNING'
logging.info('Test 1 - info') #will not show up
logging.warning('Test 1 - warning')

print("=========================================================================")

#the different functions
logging.info('Test 2 - info') #Report events that occur during normal operation of a program (e.g. for status monitoring or fault investigation)
logging.warning('Test 2 - warning') #if there is nothing the client application can do about the situation, but the event should still be noted
#warnings.warn() #should be used from insided a module if needed
logging.error('Test 2 - error') #Report suppression of an error without raising an exception 
logging.critical('Test 2 - critical') #Report suppression of an error without raising an exception 
try:
    temp = 1/0
except:
    logging.exception('Test 2 - exception') #this should only be used inside a try/except, because it will include the error info automatically

print("=========================================================================")
