# -*- coding: utf-8 -*-
#
#  Copyright 2011 Sybren A. Stüvel <sybren@stuvel.eu>
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

'''Common functionality shared by several modules.'''


import math

def bit_size(number):
    '''Returns the number of bits required to hold a specific long number.

    >>> bit_size(1023)
    10
    >>> bit_size(1024)
    10
    >>> bit_size(1025)
    11

    '''

    if number < 0:
        raise ValueError('Only nonnegative numbers possible: %s' % number)

    if number == 0:
        return 1
    
    return int(math.ceil(math.log(number, 2)))

def byte_size(number):
    """Returns the number of bytes required to hold a specific long number.
    
    The number of bytes is rounded up.
    """

    return int(math.ceil(bit_size(number) / 8.0))
