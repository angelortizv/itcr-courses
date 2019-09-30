/*-------------------------------------------------------------------------------

 @file prolog-basics-01.rkt
 @version 1.0
 @date 30/07/2019
 @author angelortizv
 @brief This file contains basic functions to learning Prolog
 
-------------------------------------------------------------------------------*/

% Name: First Element
% Execution Example: first([a,b,c],X) ; X = a
first([X|_],X).

% Name: Rest of a List
% Execution Example: rest([a,b,c],X) ; X = [b,c]
rest([_|X],X).

% Name: Lists Construction
% Execution Example: resconst(a, [b,c],X) ; X = [a,b,c]
cons(X,L,[X|L]).

% Name: list concatenation
% Execution Example: concat([a,b], [c,d,e],L) ; L =[a,b,c,d,e]
concat([],L,L).
concat([X|L1],L2,[X|L3]):-concat(L1,L2,L3).

% Name: Reverse List
% Execution Example: reverse([a,b,c],L) ; L =[c,b,a]
reverse(L1,L2):-reverse_aux(L1,L2,[]).
reverse_aux([],L2,L2).
reverse_aux([X|L1],L2,L3):-reverse_aux(L1,L2,[X|L3]).

% Name: Length of a list
% Execution Example: kength([a,b,c],X) ; X=3
length([],0).
length([_|L],N) :-
    length(L,N1),
    N is N1 + 1.

% Name: BNF Example -------------------------------------------------------------


% Descripción		:	Inicio de una Conversacion
% Nombre de Hecho	:	saludo([X])
% Parámetro			: 	palabra clave de saludo 	
% Uso				:	sintagma_saludo([B])
saludo([hola|S],S).
saludo([saludos|S],S).
saludo([disculpe|S],S).
saludo([buenos,dias|S],S).
saludo([buenas,tardes|S],S).
saludo([buenas,noches|S],S).

% Descripción		:	Fin de una Conversacion
% Nombre de Hecho	:	despedida([X])
% Parámetro			:	palabra clave de despedida
% Uso				:	sintagma_saludo([B])
despedida([gracias|S],S).
despedida([muchas,gracias|S],S).
despedida([adios|S],S).
despedida([hasta_luego|S],S).
despedida([chao|S],S).

% Descripción		:	Nombre del Programa
% Nombre de Hecho	:	nombre_programa([X])
% Parámetro			:	nombre del Sistema Experto
% Uso				:	sintagma_saludo([B])
nombre_programa([callCenterLog|S],S).
nombre_programa([log|S],S).
nombre_programa([callCenter|S],S).

% Palabras Clave para el BNF --------------------------------------------------------------------------------------------------------------

%  Descripción		:	Determinantes masculinos
% Nombre de Hecho	:	determinante_m(X)
% Parámetro			:	determinantes masculinos
% Uso				:	sintagma_nominal([A],[B])		
determinante_m([el|S],S).
determinante_m([lo|S],S).
determinante_m([los|S],S).
determinante_m([un|S],S).
determinante_m([unos|S],S).
determinante_m([este|S],S).
determinante_m([estos|S],S).
determinante_m([nuestro|S],S).
determinante_m([otro|S],S).
determinante_m([alguno|S],S).
determinante_m([algunos|S],S).
determinante_m([del|S],S).

% Descripción		:	Determinantes femeninos
% Nombre de Hecho	:	determinante_f([X])
% Parámetro			:	determinantes femeninos
% Uso				:	sintagma_nominal([A],[B])
determinante_f([la|S],S).
determinante_f([las|S],S).
determinante_f([una|S],S).
determinante_f([unas|S],S).
determinante_f([esta|S],S).
determinante_f([estas|S],S).
determinante_f([nuestra|S],S).
determinante_f([otra|S],S).
determinante_f([alguna|S],S).
determinante_f([algunas|S],S).
determinante_f([mala|S],S).

% Descripción		:	Determinantes neutros
% Nombre de Hecho	:	determinante_n([X])
% Parámetro			:	determinantes neutros
% Uso				:	sintagma_nominal([A],[B])
determinante_n([mi|S],S).
determinante_n([mis|S],S).
determinante_n([posibles|S],S).

% Descripción		:	Negaciones
% Nombre de Hecho	:	negacion([X])
% Parámetro			:	adverbios de negacion
% Uso				:	oracion([A],[B])
negacion([no|S],S).
negacion([nunca|S],S).

% Descripción		:	sustantivos masculinos
% Nombre de Hecho	:	sustantivo_m([X])
% Parámetro			:	sustantivos masculinos
% Uso				:	sintagma_nominal([A],[B])
sustantivo_m([internet|S],S).
sustantivo_m([celular|S],S).
sustantivo_m([televisor|S],S).
sustantivo_m([archivos|S],S).
sustantivo_m([papel|S],S).
sustantivo_m([problema|S],S).

% Descripción		:	sustantivos femeninos
% Nombre de Hecho	:	sustantivo_f([X])
% Parámetro			:	sustantivos femeninos
% Uso				:	sintagma_nominal([A],[B])
sustantivo_f([computadora|S],S).
sustantivo_f([impresora|S],S).
sustantivo_f([imagen|S],S).
sustantivo_f([referencia,para|S],S).
sustantivo_f([causas|S],S).

% Descripción		:	
% Nombre de Hecho	:	inicio causa_ref([X])
% Parámetro			:	
% Uso				:	
inicio_cr([posibles,causas,del,problema|S],S).
inicio_cr([algunas,referencias,para,el,problema|S],S).

% Descripción		:	Verbos
% Nombre de Hecho	:	verbo([X])
% Parámetro			:	verbos utilizables
% Uso				:	sintagma_verbal([A],[B])
verbo([sirve|S],S).
verbo([me,sirve|S],S).
verbo([funciona|S],S).
verbo([funcione|S],S).
verbo([se,descompuso|S],S).
verbo([se,rompio|S],S).
verbo([enciende|S],S).
verbo([se,enciende|S],S).
verbo([me,enciende|S],S).
verbo([se,conecta|S],S).
verbo([suena|S],S).
verbo([se,ve|S],S).
verbo([ocupo|S],S).
verbo([cambiar|S],S).
verbo([editar|S],S).
verbo([remover|S],S).
verbo([se,sobrecalienta|S],S).
verbo([se,le,atasca|S],S).
verbo([muestra|S],S).
verbo([esta,lento|S],S).
verbo([tiene|S],S).
verbo([tiene,conexion|S],S).
verbo([imprime|S],S).



% Descripción		:	recibe una lista de palabras y una lista vacía y verifica si es una oración gramaticalmente correcta según la estructura establecida
% Nombre de Regla	:	oracion([A],[B])
% Parámetro			:	lista para revisar y lista vacía
% Uso				:	se utiliza para validar oraciones
oracion(A,B):-
	sintagma_nominal(A,C),
	sintagma_verbal(C,B).
oracion(A,B):-
	sintagma_nominal(A,C),
	negacion(C,D),
	sintagma_verbal(D,B).
oracion(A,B):-
	inicio_cr(A,C),
	sintagma_nominal(C,D),
	sintagma_verbal(D,B).
oracion(A,B):-
	inicio_cr(A,C),
	sintagma_nominal(C,D),
	negacion(D,E),
	sintagma_verbal(E,B).

% Descripción		:	recibe una lista de palabras y una lista vacía; elimina el primer sintagma nominal encontrado y devuelve el resto de las palabras
% Nombre de Regla	:	sintagma_nominal([A],[B])
% Parámetro			:	lista a revisar y lista vacía
% Uso				:	se utiliza para encontrar el primer sintagma nominal en una lista de palabras
sintagma_nominal(A,B):-
	determinante_m(A,C),
	sustantivo_m(C,B).
sintagma_nominal(A,B):-
	determinante_f(A,C),
	sustantivo_f(C,B).
sintagma_nominal(A,B):-
	determinante_n(A,C),
	sustantivo_f(C,B).
sintagma_nominal(A,B):-
	determinante_n(A,C),
	sustantivo_m(C,B).

% Descripción		:	recibe una lista de palabras y una lista vacía; elimina el primer sintagma verbal encontrado y devuelve el resto de las palabras
% Nombre de Regla	:	sintagma_verbal([A],[B])
% Parámetro			:	lista a revisar y lista vacía
% Uso				:	se utiliza para encontrar el primer sintagma verbal en una lista de palabras
sintagma_verbal(A,B):-
	verbo(A,B).
sintagma_verbal(A,B):-
	verbo(A,C),
	sintagma_nominal(C,B).

% Descripción		:	recibe una lista de palabras y una lista vacía y verifica si estas palabras componen un saludo al programa (Ej. “hola log”)
% Nombre de Regla	:	sintagma_saludo([B])
% Parámetro			:	lista a revisar y lista vacía
% Uso				:	se utiliza para encontrar el primer sintagma saludo en una lista de palabras
sintagma_saludo(B):-
	input_to_list(L),
	saludo(L,C),
	nombre_programa(C,B),!.
sintagma_saludo(B):-
	sintagma_saludo([]).