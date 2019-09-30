#|-------------------------------------------------------------------------------------------------------------------

 tallerfuncional.rkt - archivo correspondiente al taller de Programación Funcional

 Este archivo es parte de las tareas cortas (talleres) correspondientes a un 10% de la nota
 en el curso de Lenguajes Compiladores e Intérpretes: Módulo Lenguajes. El mismo tiene como
 objetivo, reafirmar el conocimiento del paradigma de programación funcional.

 Versión de Archivo    :    0.1
 Autor                 :    Angelo Ortiz Vega, Github@angelortizv
 Última Modificación   :    12/09/2019 : 22:50

-------------------------------------------------------------------------------------------------------------------|#

#lang racket

;;Ejercicio 1: Programe la función factorial
;;Ejemplo de ejecución: 0! = 1; n! = n(n-1)!
(define (fact n)
  (cond ((zero? n)
         1)
        (else
         (* n (fact (- n 1))))))

;;Ejercicio 2: Programe la función fibonacci
;;Ejemplo de ejecución: fib(0) = 1; fib(1) = 1; fib(n) = fib(n-1) + fin(n-2)
(define (fib n)
  (cond ((equal? n 0)
         1)
        ((equal? n 1)
         1)
        (else
         (+ (fib(- n 1)) (fib(- n 2))))))

;;Ejercicio 3: Programe la función miembro
;;Ejemplo de ejecución: (miembro 'a '(a b c)) = #t; (miembro 'a '(b c d)) = #f
(define (miembro ele list1)
  (cond ((null? list1)
         #f)
        ((equal? ele 1)
         (car list1))
        (else
         (miembro ele (cdr list1)))))

;;Ejercicio 4: Programe la función eliminar
;;Ejemplo de ejecución: (eliminar 'a '(a b c)) = '(b c); (eliminar 'a (b c d)) = '(b c d)
(define (eliminar ele list1)
  (cond ((null? list1)
         '())
        ((equal? ele (car list1))
         (cdr list1))
        (else
         (cons (car list1)
               (eliminar ele (cdr list1))))))

;;Ejercicio 5: Programe la función quicksort
;;Ejemplo de ejecución: (quicksort '(3 2 1)) = (1 2 3); (quicksort '(2 3 4 1 1 2 5))
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

(define (quicksort list1)
  (cond((null? list1)
        '())
       (else
        ((let*
            ((point (car list1))
             (smallest-greatest (pivot list1))
             (smallest (car smallest-greatest))
             (greatest (cadr smallest-greatest))
             )
          (append(quicksort smallest)
                 (list point)
                 (quicksort greatest)))))))

;;Ejercicio 6: Programe una función que reciba de parámetro una lista de símbolos que representen los
               ;atributos de un automóvil y una lista de símbolos con los valores de estos atributos. La función
               ;retornará una lista que contenga pares, cada par contendrá indicando su atributo y su valor.
;;Ejemplo de Ejecución: (automóvil '(Hatchback Susuki Forza1 Rojo si Manual) '(Tipo Marca Modelo Calor AC Trasmisión)) =
                       ;((Tipo Hatchback) (Marca Susuki) (Modelo Forza1) (color Rojo) (AC si) (Transmisión Manual)) 
(define (automovil listaatributos listasimbolos)
  (cond
    [(or(null?  listaatributos)(null? listasimbolos))
     '()]
    [else
     (append  (list(list (car listasimbolos) (car listaatributos))) (automovil  (cdr listaatributos)(cdr listasimbolos)))]
    )
  )

;;Ejercicio 7: Programe la función eliminar de un árbol binario

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

;Remove elements from a tree
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


;;Ejercicio 8: Programe la función encuntrar las rutas anchura primero
;;Ejemplo de ejecución: (widthFirst 'src 'dest 'graph)

;Reverse Sublist in a list
(define (reverseSublists list1)
  (reverseSublistsAux list1 '()))

(define (reverseSublistsAux list1 result)
  (cond ((null? list1)
         (reverse result))
        (else
         (reverseSublistsAux (cdr list1)
                               (cons (reverse (car list1))
                                     result)))))

;Function that creates new paths
(define (extend path graph)
  (extendAux (getNeighbors (car path) graph) '() path))

(define (extendAux neighbors result path)
  (cond ((null? neighbors)
         result)
        ((memberList? (car neighbors) path) (extendAux (cdr neighbors) result path))
        (else
         (extendAux (cdr neighbors)
                     (append result (list (list* (car neighbors) path)))
                     path))))

;Search function by width first
(define (widthFirst src dest graph)
  (cond ((equal? src dest)
         (list src))
        (else
         (widthFirstAux (list (list src)) dest graph '()))))

(define (widthFirstAux paths end graph result)
  (cond ((null? paths)
         (reverseSublists result))
        ((equal? end (caar paths))
         (widthFirstAux (cdr paths)
                         end
                         graph
                         (cons (car paths) result)))
        (else
         (widthFirstAux (append (extend (car paths) graph)
                                 (cdr paths))
                         end
                         graph
                         result)
         )))