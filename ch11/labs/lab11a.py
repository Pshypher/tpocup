
################################################################################
## Demonstration program for class Date
################################################################################

import date

A = date.Date( 1, 1, 2014 )

print( A )              # 01/01/2014
print( A.to_iso() )     # 2014-01-01
print( A.to_mdy() )     # January 01, 2014
print( A.is_valid() )   # True
print()

B = date.Date( 12, 31, 2014 )

print( B )              # 12/31/2014
print( B.to_iso() )     # 2014-12-31
print( B.to_mdy() )     # December 31, 2014
print( B.is_valid() )   # True
print()

C = date.Date()

C.from_iso( "2014-07-04" )  

print( C )              # 07/04/2014
print( C.to_iso() )     # 2014-07-04
print( C.to_mdy() )     # July 04, 2014
print( C.is_valid() )   # True
print()

D = date.Date()

D.from_mdy( "March 15, 2015" )

print( D )              # 03/15/2015
print( D.to_iso() )     # 2015-03-15
print( D.to_mdy() )     # March 15, 2015
print( D.is_valid() )   # True
print()

E = date.Date()

print( E )              # 00/00/0000
print( E.to_iso() )     # 0000-00-00
print( E.to_mdy() )     # Invalid 0, 0000
print( E.is_valid() )   # False
print()

