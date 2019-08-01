#|-------------------------------------------------------------------------------

 @file racket-basics-04.rkt
 @version 1.0
 @date 31/07/2019
 @author angelortizv
 @brief This file contains basic functions to learning Scheme through DrRacket
 
-------------------------------------------------------------------------------|#

#lang racket

;Tree Builder
(define (tree root left right)
  (cond((and (null? left) (null? right))
        root)
       (else
        (list root left right))))

(define (atom? x)
  (not (list? x)))

;Tree's Root
(define (root tree1)
  (cond( (atom? tree1)
        tree1)
  (else
   (car tree1))))

;Tree's Left Child
(define (left-child tree1)
  (cond ((atom? tree1)
         '())
        (else
         (cadr tree1))))

;Tree's Right Child
(define (right-child tree1)
  (cond ((atom? tree1)
         '())
        (else
         (caddr tree1))))

;Leaf Evaluator
(define (leaf? node)
  (cond((null? node)
        #f)
       ((atom? node)
        #t)
       ((and (null? (left-child node))
             (null? (right-child node)))
       #t)
  (else
   #f)))

;Find an item in a tree
(define (node? ele tree1)
  (cond ((null? tree1)
         #f)
        ((equal? ele (root tree1))
         #t)
        ((node? ele (left-child tree1))
         #t)
        ((node? ele (right-child tree1))
         #t)
        (else
         #f)))

#|--Tidy Binary Trees-----------------------------|#

;Locate an item
(define (locate ele tree1)
  (cond ((null? tree1)
         #f)
        ((equal? ele (root tree1))
         tree1)
        ((< ele (root tree1))
         (locate ele (left-child tree1)))
        ((> ele (root tree1))
         (locate ele (right-child tree1)))))

;Insert elements
(define (insert ele tree1)
  (cond ((null? tree1)
         (tree ele '() '()))
        ((<= ele (root tree1))
         (tree (root tree1)
               (insert ele (left-child tree1))
               (right-child tree1)))
        ((> ele (root tree1))
         (tree (root tree1)
               (left-child tree1)
               (insert ele (right-child tree1))))))

;Remove elements
(define (major tree1)
  (cond ((null? tree1)
         #f)
        ((null? (right-child tree1))
         (root tree1))
        (else
         (major (right-child tree1)))))

(define (remove ele tree1)
  (cond ((null? tree1)
         '())
        ;node search starts
        ((< ele (root tree1))
         (tree (root tree1)
               (remove ele (left-child tree1))
               (right-child tree1)))
        ((> ele (root tree1))
         (tree (root tree1)
               (left-child tree1)
               (remove ele (right-child tree1))))
        ;node has no children
        ((and (null? (left-child tree1))
              (null? (right-child tree1)))
         '())
        ;node has no left child
        ((null? (left-child tree))
         (right-child tree1))
        ;node has no right child
        ((null? (right-child tree1))
        (left-child tree1))
  (else
   (tree (major (left-child tree1))
         (remove (major (left-child tree1))
                 (left-child tree1))
         (right-child tree1)))))

