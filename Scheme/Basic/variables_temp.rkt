#lang scheme
;there are no variables in scheme per-se, instead, anything that looks like a variable just copy and pasts part of the exicution tree...

;Datatypes
;numbers = int,rational,real,complex; 5 is a int is a rational is a real is a complex
;symbols
;pairs = '(1 . 2)
;lists

;define binds a name to a value
(define var-pair '(1 . 2)) ;a way of making a pair, each pair contains two sections, a 'car' and a 'cdr'
(car var-pair) ;the first part of the pair
(cdr var-pair) ;the second part of the pair

(define var-list1 '(1 2 3 4 5)) ;'(1 2 3) a way of making a list, the other way is the next line
(define var-list2 (cons 1 (cons 2 (cons 3 (cons 4 (cons 5 '())))))) ;cons takes two arguments, and puts them together in a pair (this line creates a kind of linked list)

;accessing lists
(first var-list1)
(second var-list1)
(third var-list1)
(rest var-list1) ;returns a list minus the first element
(length var-list1)
(reverse var-list1)
(append var-list1 var-list2)
(empty? '())

;let allows the creation of a kind of local variable... (kind of... not really...)
(let ([a (+ 2 5)] ;binds a and b to their expesion
      [b 10]) ;variables evaluated in parrallel, they can't see each other
      (+ a b a a a a a a a a))
(let* ([a (+ 2 5)] ;variables evaluated in sequence, the next can see the previous
      [b (+ a 2)]) 
      (+ a b a a a a a a a a))
(letrec ([my-even? ;variables evaluated in undefined order, variables can see each other recursivly
          (lambda (x)
            (if (= x 0)
                #t
                (my-odd? (- x 1))))]
         [my-odd?
          (lambda (x)
            (if (= x 0)
                #f
                (my-even? (- x 1))))])
  (my-even? 5))