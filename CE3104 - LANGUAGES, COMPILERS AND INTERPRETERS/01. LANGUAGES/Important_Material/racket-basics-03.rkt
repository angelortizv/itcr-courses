#|-------------------------------------------------------------------------------

 @file racket-basics-03.rkt
 @version 1.0
 @date 31/07/2019
 @author angelortizv
 @brief This file contains basic functions to learning Scheme through DrRacket
 
-------------------------------------------------------------------------------|#

#lang racket

#|--SETS-----------------------------------------------------------------------|#

;Set Identification
(define (member? ele list1)
  (cond((null? list1)
        #f)
       ((equal? ele (car list1))
        #t)
       (else
        (member? ele (cdr list1)))))

(define (set? list1)
  (cond ((null? list1)
         #t)
        ((member? (car list1) (cdr list1))
        #f)
        (else
         (set? (cdr list1)))))

;Equality of Sets
(define (equal-set? conj1 conj2)
  (cond ((and (null? conj1) (null? conj2))
         #t)
        ((not (equal? (length conj1) (length conj2)))
         #f)
        (else
         (equal-set?-aux conj1 conj2))))

(define (equal-set?-aux conj1 conj2)
  (cond((null? conj1)
        #t)
       ((not (member? (car conj1) conj2))
        #f)
       (else
        (equal-set?-aux (cdr conj1) conj2))))


;Union of Sets
(define (union conj1 conj2)
  (cond ((null? conj1)
         conj2)
        ((null? conj2)
         conj1)
        ((member? (car conj1) conj2)
         (union (cdr conj1) conj2))
        (else
         (cons (car conj1)
               (union (cdr conj1) conj2)))))

;Intersection of Sets
(define (intersection conj1 conj2)
  (cond ((null? conj1)
         '())
        ((null? conj2)
         '())
        ((member? (car conj1) conj2)
         (cons (car conj1)
               (intersection (cdr conj1) conj2)))
        (else
         (intersection (cdr conj1) conj2))))
#|--SETS-----------------------------------------------------------------------|#

#|--VECTORS & MATRICES---------------------------------------------------------|#

;Vector equality
(define (equal-vec? vec1 vec2)
  (cond ((and (null? vec1) (null? vec2))
        #t)
  ((or (null? vec1) (null? vec2))
   #f)
  ((not (equal? (car vec1) (car vec2)))
   #f)
  (else
   (equal-vec? (cdr vec1) (cdr vec2)))))

;Sum of vectors
(define (vec-sum vec1 vec2)
  (cond( (and (null? vec1) (null? vec2))
         '())
       (else
        (cons (+ (car vec1)(car vec2))
              (vec-sum (cdr vec1) (cdr vec2))))))

;Vector Multiplication
(define (vec-mult vec1 vec2)
  (cond ((and (null? vec1) (null? vec2))
         0)
        (else
         (+ (* (car vec1) (car vec2))
            (vec-mult (cdr vec1) (cdr vec2))))))


;Matrix Transpose
(define (take-1f mat)
  (cond ((null? mat)
         '())
        (else
         (cons (car (car mat))
               (take-1f (cdr mat))))))

(define (delete-1f mat)
  (cond ((null? mat)
         '())
        (else
         (cons (cdr (car mat))
               (delete-1f (cdr mat))))))

(define (transpose mat)
  (cond ((null? (car mat))
        '())
        (else
         (cons (take-1f mat)
                     (transpose (delete-1f mat))))))


;Multiplication of a vector by a matrix
(define (mult-vec-mat vec mat)
  (mult-vec-mat-aux vec (transpose mat)))

(define (mult-vec-mat-aux vec mat)
  (cond ((null? mat)
         '())
        (else
         (cons (vec-mult vec (car mat))
               (mult-vec-mat-aux vec (cdr mat))))))

;Matrix Multiplication
(define (mat-mult mat1 mat2)
  (cond ((null? mat1)
         '())
        (else
         (cons (mult-vec-mat (car mat1) mat2)
               (mat-mult (cdr mat1) mat2)))))
        
#|--VECTORS & MATRICES---------------------------------------------------------|#

