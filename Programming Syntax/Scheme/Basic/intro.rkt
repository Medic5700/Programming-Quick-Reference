#lang scheme
;scheme is a function based language. 
;Every operation can be thought of as placed in a tree.
;The compiler optimizes code to be run in parallel... so code can't be thought of as running in a sequence (there are some operations that breaks this assumption, like output)

;the ";" is the comment character
;the "\" still applies as an escape character in strings
;the "'" is kind of an escape character for the language, means to interprite something litteraly
(display '(1 2 3)) ;IE: the "'(1 2 3)" means to interprite it NOT as an operation to perform on "2" and "3", but as the list "1,2,3"

;there doesn't seem to be an easy way to handle argument handling from main, the wispers from google is that there is a confuded way though

;There isn't really the concept of loops in scheme (or variables), only recursion

(display "Hello World") ;prints a single argument out
(printf "\n~a ~a" "Hello" "World") ;works more like printf from C

;true and false
(display #t) ;#f
(display '()) ;null