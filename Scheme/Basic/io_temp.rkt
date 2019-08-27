#lang scheme
(define factorial  ;returns a list
  (lambda (x) 
    (if (= x 1) 
        (cons 1 '()) 
        (let 
            ([temp (factorial (- x 1))]) 
          (cons (* x (first temp)) temp))))) 

(display (factorial 20)) ;print


;simple input
(define input (open-input-file "bin\\test.txt"))
(read input)
(close-input-port input)

;simple file write
(define output (open-output-file "bin\\test.txt")) ;creats a new file
(write (factorial 20) output)
(close-output-port output)