#lang scheme

(define var-list '(0 1 2 3 4 5 6 7 8 9))

(map (lambda (x) (+ x 1)) var-list) ;applies a function that takes n-inputs to n-lists of inputs
(map (lambda (x y) (+ x y)) var-list var-list)

(apply max var-list) ;takes a list of input, and puts it through an operation that can handle n args //IE: returns a single element output

;fold, applies an operation that takes EXACTLY two arguments, and applies it recursivle
(foldl (lambda (x y) (+ x y)) 42  var-list) ;IE: (function (function (function ... (function 42 0) 1) 2) 3) 4)...
(foldr (lambda (x y) (+ x y)) 42  var-list) ;IE: (function 0 (function 1 (function 2 (... (function 9 42)))))))))))...
