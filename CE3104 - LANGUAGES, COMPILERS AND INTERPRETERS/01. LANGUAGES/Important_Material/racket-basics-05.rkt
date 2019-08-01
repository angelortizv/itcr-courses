#|-------------------------------------------------------------------------------

 @file racket-basics-05.rkt
 @version 1.0
 @date 31/07/2019
 @author angelortizv
 @brief This file contains basic functions to learning Scheme through DrRacket
 
-------------------------------------------------------------------------------|#

#lang racket

;Computational representation for the graph
(define gg '((i (a b))
             (a (i c d))
             (b (i c d))
             (c (a b x))
             (d (a b f))
             (x (c))
             (f (d))
             ))

;There is route
(define (solution? end route)
  (equal? end (car route)))

;Neighbors
(define (neighbors ele graph)
  (let ((result (assoc ele graph)))
    (cond ((equal? result #f)
           #f)
          (else
           (cadr result)))))

;Find routes by depth first
(define (member? ele list1)
  (cond((null? list1)
        #f)
       ((equal? ele (car list1))
        #t)
       (else
        (member? ele (cdr list1)))))

(define (extend route graph)
  (apply append(map(lambda(x)
                     (cond ((member? x route) '())
                           (else (list (cons x route)))))
                   (neighbors (car route) graph))))

(define (depth start end graph)
  (depth-aux (list (list start)) end graph))

(define (depth-aux routes end graph)
  (cond ((null? routes)
         '())
        ((solution? end (car routes))
         (reverse (car routes)))
        (else
         (depth-aux (append (extend (car routes) graph)
                            (cdr routes))
                    end
                    graph))))

;Find routes by width first
(define (width-all start end graph)
  (width-all-aux (list (list start)) end graph '()))

(define (width-all-aux routes end graph total)
  (cond ((null? routes)
         (map reverse total))
        ((solution? end (car routes))
         (width-all-aux (cdr routes)
                        end
                        graph
                        (cons (car routes) total)))
        (else
         (width-all-aux (append
                         (cdr routes)
                         (extend (car routes) graph))
                        end
                        graph
                        total))))