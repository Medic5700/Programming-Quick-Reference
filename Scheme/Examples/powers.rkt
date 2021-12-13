#lang racket

;;  Author: Medic5700
;;
;;  A simple program that displays the powers of 2.
;;  An example with a focus on string formatting.

(map 
 (lambda (x) (printf "2^~a\t=\t~a\n" x (expt 2 x)))
 '(0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20))
;note: displayed '<#void>' means the print returned nothing (If I understand it right)