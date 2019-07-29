#|-------------------------------------------------------------------------------

 @file rackets-basics-02.rkt
 @version 1.0
 @date 28/07/2019
 @author angelortizv
 @brief This file contains basic functions to learning Scheme through DrRacket
 
-------------------------------------------------------------------------------|#

#lang racket


#|
;;Basic Operations on lists
   () -> null list
   (car '(s0 ... sN)) -> returns the first item
   (cdr '(s0 ... sN)) -> returns all items except the first
   (cons s0 '(s1 s2 sN)) -> Insert an item at the beginning
   (list s0 ... sN) -> Produce a list with the parameters entered

;;List Evaluators
   (list? '())
   (equal? arg1 arg2)
   (null? arg1)

|#

;Greatest common divisor
(define (gcd a b)
  (cond((zero? b)
        a)
       (else
        (gcd b (remainder a b)))))

;Make a number rational
(define (make-rat a b)
  (let((maxcd(gcd a b))
       )
    (list(/ a maxcd)
         (/ b maxcd))))

;List Member
(define (member? ele list1)
  (cond((null? list1)
        #f)
       ((equal? ele (car list1))
        #t)
       (else
        (member? ele (cdr list1)))))

;Length of a list
(define (length list1)
  (cond ((null? list1)
         0)
        (else
         (+ 1 ( length (cdr list1))))))

;Extract the nth element
(define (element index list1)
  (cond ((null? list1)
         #f)
        ((equal? index 1)
         (car list1))
        (else
         (element (- index 1)(cdr list1)))))

;Extract the last item
(define (last list1)
  (cond((null? list1)
        #f)
       ((null? (cdr list1))
        (car list1))
       (else
        (last (cdr list1)))))

;Remove pair numbers
(define (pairs list1)
  (cond((null? list1)
        '())
       ((even? (car list1))
        (cons (car list1)
              (pairs (cdr list1))))
       (else
        (pairs (cdr list1)))))

;Paste two lists
(define (paste list1 list2)
  (cond ((null? list1)
         list2)
        ((null? list2)
         list1)
        (else
         (cons (car list1)
               (paste (cdr list1)
                      list2)))))

;Invert a list
(define (invert list1)
  (cond ((null? list1)
         '())
        (else
         (append (invert (cdr list1))
                 (list (car list1))))))
 
;Find the highest in a list
(define (highest list1)
  (cond ((null? list1)
         #f)
        (else
         (highest-aux (car list1) (cdr list1)))))

(define (highest-aux ele list1)
  (cond ((null? list1)
         ele)
        ((< ele (car list1))
         (highest-aux (car list1) (cdr list1)))
        (else
         (highest-aux ele (cdr list1)))))

;Find the smallest in a list
(define (smallest list1)
  (cond ((null? list1)
         #f)
        (else
         (smallest-aux (car list1) (cdr list1)))))

(define (smallest-aux ele list1)
  (cond ((null? list1)
         ele)
        ((< (car list1) ele)
         (smallest-aux (car list1) (cdr list1)))
        (else
         (smallest-aux ele (cdr list1)))))

;Remove an item from a list
(define (remove-ele ele list1)
  (cond((null? list1)
        '())
       ((equal? ele (car list1))
        (cdr list1))
       (else
        (cons (car list1)
              (remove-ele ele (cdr list1))))))

;Sort a list
(define (sort list1)
  (cond ((null? list1)
         '())
        (else
         (cons (smallest list1)
               (sort(remove-ele
                     (smallest list1)
                     list1))))))

;Sort a list by insertion
(define (insert-sorted-list ele list1)
  (cond((null? list1)
        (list ele))
       ((> ele (car list1))
        (cons (car list1)
              (insert-sorted-list ele
                                  (cdr list1))))
       (else
        (cons ele list1))))

(define (insertion-sort list1)
  (cond((null? list1)
        '())
       (else
        (insertion-sort-aux list1 '()))))

(define (insertion-sort-aux list1 result)
  (cond((null? list1)
        result)
       (else
        (insertion-sort-aux
         (cdr list1)
         (insert-sorted-list (car list1)
         result)))))

;Sort a list by successive partitions
(define (pivot list1)
  (cond ((null? list1)
         #f)
        (else
         (pivot-aux (car list1) (cdr list1) '() '() ))))

(define (pivot-aux point list1 smallest greatest)
  (cond( (null? list1)
        (list1 smallest greatest))
  ((<= (car list1) point)
   (pivot-aux point
              (cdr list1)
              (cons (car list1) smallest)
              greatest))
  (else
   (pivot-aux point
              (cdr list1)
              smallest
              (cons (car list1) greatest)))))

(define (quick-sort list1)
  (cond((null? list1)
        '())
       (else
        ((let*
            ((point (car list1))
             (smallest-greatest (pivot list1))
             (smallest (car smallest-greatest))
             (greatest (cadr smallest-greatest))
             )
          (append(quick-sort smallest)
                 (list point)
                 (quick-sort greatest)))))))
