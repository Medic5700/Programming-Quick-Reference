{-
Author: Medic5700

This is an example of generating a factorial using recursion.
-}

factorial 0 = 1
factorial n = n * factorial ( n-1 )

main = print (map factorial [0..10])
