{-
Author: Medic5700

This is an example of generating the fibonacci sequence using recursion.
-}

fib 0 = 0
fib 1 = 1
fib n = fib (n-1) + fib (n-2)

main = print (map fib [0 .. 10])
