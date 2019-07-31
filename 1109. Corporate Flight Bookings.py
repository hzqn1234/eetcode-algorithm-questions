## O(n)    
class Solution:
    def corpFlightBookings(self, bookings, n):
        res = [0] * (n + 1) 
        for start, end, seats in bookings:
            res[start-1] += seats
            res[end] -= seats
        s = 0
        for index, i in enumerate(res):
            res[index] += s
            s += i
        return res[:-1]

## Too Slow (Brute Force)
class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        # booking_final = [[0]*n for i in range(len(bookings))]
        booking_final2 = [0]*n
        for start,end,seat in bookings:
            for flight in range(start-1,end):
                booking_final2[flight]=booking_final2[flight]+seat            
        return booking_final2

## Too Slow
from operator import add
class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        # booking_final = [[0]*n for i in range(len(bookings))]
        booking_final2 = [0]*n
        for i in range(len(bookings)):
            booking = bookings[i]
            temp=[0]*(booking[0]-1)+[booking[2]]*(booking[1]-booking[0]+1)+[0]*(n-booking[1])
            booking_final2 = list( map(add, booking_final2, temp ))
        return booking_final2



## Too Slow
from operator import add
class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        # booking_final = [[0]*n for i in range(len(bookings))]
        booking_final2 = [0]*n
        for i in range(len(bookings)):
            booking = bookings[i]
            temp=[0]*(booking[0]-1)+[booking[2]]*(booking[1]-booking[0]+1)+[0]*(n-booking[1])
            booking_final2 = list( map(add, booking_final2, temp ))
        return booking_final2



## Memory Exceeded
from operator import add
class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        booking_final = [[0]*n for i in range(len(bookings))]
        booking_final2 = [0]*n
        for i in range(len(bookings)):
            booking = bookings[i]
            booking_final[i]=[0]*(booking[0]-1)+[booking[2]]*(booking[1]-booking[0]+1)+[0]*(n-booking[1])
        for i in range(len(bookings)):
            booking_final2 = list( map(add, booking_final2, booking_final[i] ))
        return booking_final2

## Too Slow
class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        booking_final = [0]*n
        for booking in bookings:
            for flight in range(booking[0],booking[1]+1):
                booking_final[flight-1]=booking_final[flight-1]+booking[2]
        return booking_final