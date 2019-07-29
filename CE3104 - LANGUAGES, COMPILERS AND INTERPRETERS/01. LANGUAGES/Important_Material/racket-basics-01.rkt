#|-------------------------------------------------------------------------------

 @file rackets-basics-01.rkt
 @version 1.0
 @date 28/07/2019
 @author angelortizv
 @brief This file contains basic functions to learning Scheme through DrRacket
 
-------------------------------------------------------------------------------|#

#lang racket

#|
;;Elementary numerical operations
   (+ arg1 ... argN)
   (- arg1 ... argN)
   (* arg1 ... argN)
   (/ arg1 ... argN)

;;Additional numerical operations
   (abs arg1)
   (min arg1 ... argN)
   (max arg1 ... argN)
   (truncate arg1)
   (round arg1)
   (quotient arg1 arg2) "/"
   (remainder arg1 arg2) "%"
   (expt arg arg2)
   (sqrt arg1)

;;Numeric Predicates
   (= arg1 ... argN)
   (equal? arg1 arg2)
   (< arg1 ... argN)
   (<= arg1 ... argN)
   (> arg1 ... argN)
   (>= arg1 ... argN)
   (zero? arg1)
   (positive? arg1)
   (negative? arg1)
   (even? arg1) "pair=#t-impair=#f"   
   (odd? arg1) "pair=#f - impair=#t"
   (number? arg1)
   (integer? arg1)
   (real? arg1)
   
;;Logical Predicates
   (and arg1 ... argN)
   (or arg1 ... argN)
   (not arg1)

;;Other Functions
   (quote arg1) = 'arg1
|#

;Successor Function
(define (suc n)
  (+ n 1))

;Predeccesor Function
(define (pred n)
  (- n 1))

;Square a number
(define (square x)
  (* x x))

;Raise a number to a power
(define (expt b n)
  (if (= n 0)
      1
      (* b (expt b (- n 1)))))

;Sum 0 to n
(define (sum-until n)
  (cond ((zero? n)
         0)
        (else
         (+ n (sum-until (- n 1))))))

;Sum of Squares
(define (sum-squares n)
  (cond ((zero? n)
        0)
  (else
   (+ (* n n) (sum-squares (- n 1))))))

;Sum of Quotients
(define (sum-quotients n)
  (cond((zero? n)
        0)
       (else
        (+ (/ 1 (* n (+ 1 n)))
           (sum-quotients (- n 1))))))

;Sum of an interval
(define (sum-interval start end)
  (cond ((equal? start end)
         end)
        (else
         (+ start
            (sum-interval(+ 1 start) end)))))

;Factorial Function
(define (factorial n)
  (if (= n 1)
      1
      (* n (factorial (- n 1)))))

;Fibonacci’s Numbers
(define (fib n)
  (cond ((equal? n 0)
         1)
        ((equal? n 1)
        1)
        (else
         (+ (fib (- n 1))
            (fib (- n 2))))))

;Prime Numbers
(define (divisible? n div)
  (zero? (remainder n div)))

(define (prime n)
  (cond ((equal? n 1)
         #t)
        (else
         (prime?-aux n 2))))

(define (prime?-aux n div)
  (cond ((equal? n div)
         #t)
        ((divisible? n div)
         #f)
        (else
         (prime?-aux n (+ div 1)))))
