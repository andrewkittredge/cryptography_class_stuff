'''
Created on Dec 12, 2011

@author: Brent Hepburn
'''
import math

def ascii_to_int(message):
    result = 0
    for i in range(len(message)):
        result = result + ord(message[len(message) - i - 1])*10**(i*3)
    return result
    
def int_to_ascii(value):
    result = ""
    val = str(value)
    for i in range(int(math.ceil(float(len(val)) / float(3)))):
        end = len(val) - (i * 3);
        start = end - 3;
        if start < 0:
            start = 0
        result = chr(int(val[start:end])) + result
    return result

import unittest
class TestAscciToInt(unittest.TestCase):
    def test_int_to_ascii(self):
        s = 'Now is the time for something something'
        message_int = ascii_to_int(s)
        self.assertTrue(int(message_int))
        self.assertEqual(int_to_ascii(message_int), s)
        
        message = 'hello world'
        i = ascii_to_int(message)
        self.assertEqual(i, 10965)
        self.assertEqual(message, int_to_ascii(i))

if __name__ == '__main__':
    unittest.main()