#lang scheme

;function decliration
(define fib (lambda (x) (if (<= x 0) 0 (if (= x 1) 1 (+ (fib (- x 1)) (fib (- x 2)))))))

;display formatting
(map 
 (lambda (x) (printf "fib(~a)\t= ~a~n" x (fib x)))
 '(0 1 2 3 4 5 6 7 8 9 10))
;note: displayed '<#void>' means the print returned nothing (If I understand it right)