# Simple Interest is p*r*t/100 where p is principal
# r is rate and t the time.

p = 10000
r = 12.5
t = 5
simple_interest = (p * r * t) / 100
print("The simple interest of ${} for a duration of {} years \
and interest rate equal to {:.1%} is {}".format(p,t,(r/100),simple_interest))
