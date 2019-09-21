#lang scheme

; =      - equal
; <      - less then
; <=     - less then or equal to
; >      - greater then
; >=     - greater then or equal to
; eq?    - identical
; eqv?   - operationally equivalent
; equal? - same structure and contents
; not    - not
; and    - and
; or     - or

; empty? - is the list/arg empty?


(map (lambda (x)
       (if (= x 0)
           '(0,0)
           '(0,1)))
       '(0 1 2 3 4 5 6 7 8 9))

(map (lambda (x)
       (cond [(= x 0) '(1,0)]
             [(= x 1) '(1,1)]
             [else '(1,2)]))
       '(0 1 2 3 4 5 6 7 8 9))