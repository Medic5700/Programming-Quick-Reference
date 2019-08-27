#lang scheme

;function decliration
(define factorial (lambda (x) (if (= x 0) 1 (* x (factorial (- x 1))))))

;display formatting
(map 
 (lambda (x) (printf "~a!\t= ~a~n" x (factorial x)))
 '(0 1 2 3 4 5 6 7 8 9 10))
;note: displayed '<#void>' means the print returned nothing (If I understand it right)