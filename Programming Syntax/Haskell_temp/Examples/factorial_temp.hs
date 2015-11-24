factorial 0 = 1
factorial n = n * factorial ( n-1 )

temp = map factorial [0..10]
temp2 n = [ factorial(x) | x <- [0..n]]
