%--------------------------------------------------------------------------------------------------------------------
%
% tallerlogico.rkt - archivo correspondiente al taller de Programación Lógica
%
% Este archivo es parte de las tareas cortas (talleres) correspondientes a un 10% de la nota
% en el curso de Lenguajes Compiladores e Intérpretes: Módulo Lenguajes. El mismo tiene como
% objetivo, reafirmar el conocimiento del paradigma de programación lógico.
%
% Versión de Archivo    :    0.1
% Autor                 :    Angelo Ortiz Vega, Github@angelortizv
% Última Modificación   :    11/09/2019 : 16:06
%
% -------------------------------------------------------------------------------------------------------------------

%Ejercicio 1: Defina los hechos correspondientes a: clara->jose->ana; tomas->jose->patricia->jaime; tomas->isabel
progenitor(clara, jose).
progenitor(tomas, jose).
progenitor(tomas, isabel).
progenitor(jose, ana).
progenitor(jose, patricia).
progenitor(patricia, jaime).

%Ejercicio 2: ¿Cómo preguntamos quienes son los abuelos de Jaime?
abuelo(X, Y):- progenitor(X,Z),progenitor(Z,Y).

%Ejercicio 3: ¿Cómo preguntamos quienes son los bisabuelos de Jaime?
bisabuela(X, Y):- progenitor(X,Z),progenitor(Z,A),progenitor(A,Y).

%Ejercicio 4: Defina los hechos para: el oro es valioso;ana es mujer;juan tiene oro;juan es el padre de maria;
             %juan presta el libro a maria;juan presta el lapiz a pedro;pedro presta el borrador a juan.
valioso(oro).
mujer(ana).
tiene(juan, oro).
padre(juan, maria).
prestamolibro(juan, maria). /*prestamo(libro, juan, maria)*/
prestamolapiz(juan, pedro). /*prestamo(lapiz, juan, pedro)*/
prestamoborrador(pedro, juan). /*prestamo(borrador, pedro, juan)*/

%Ejercicio 5: Teniendo los siguientes hechos: varon(albert);varon(edward);mujer(alice);mujer(victoria);padres(edward,victoria,albert)
                                             %padres(alice,victoria,albert).
                                             %Plantee la regla para hermana_de(X,Y).Es cierto si X es hermana de Y.
varon(albert).
varon(edward).
mujer(alice).
mujer(victoria).
padres(edward, victoria, albert). 
padres(alice, victoria, albert).
hermana_de(X,Y):- padres(X, Z, A), padres(Y,Z,A), mujer(X), X\=Y.

%Ejercicio 6: Plantee los hechos y deducciones para la función miembro
%Ejemplo de Ejecución: ?miembro(b,[a,b,c]) = true; ?miembro(b,[a,[b,c]]) = false; ?miembro([b,c],[a,[b,c]]) = true.
miembro(X, [X|_]).
miembro(X, [_|R]):- miembro(X,R).

%Ejercicio 7: Plantee los hechos y deducciones para la función inversa.
%Ejemplo de Ejecución: ?inversa([a,b,c],[c,b,a]) = true; ?inversa([a,b,c],X).
invertir(L1,L):-invertir(L1,[],L).
invertir([],L,L).
invertir([X|L1],L2,L3):-invertir(L1,[X|L2], L3).

invertir2([],Zs,Zs).
invertir2([X|Ls],Ys, Zs):-invertirAux(Xs, [X|Ys], Zs).

%Ejercicio 8: Cree las clausulas para longitud
%Ejemplo de Ejecución: ?Longitud([a,b,c,d,e],5) = true; ?Longitud([a,b,c,d,e],3) = False; ?Longitud([a,b,c,d,e],X) = 5.
longitud([],0).
longitud([X|L], N):-longitud(L,N1),
N is N1+1.

%Ejercicio 9: Defina 3 acontecimientos que se compongan de 2 elementos fecha(año) y evento.
             %Escriba las clausulas para que le pregunte al usuario una fecha y el sistema devuelva el evento asociado.
%Ejemplo de Ejecución: ?FechaEvento() -> Digite la fecha -> 2018 -> el 2018 se dio el mundial de rusia
fecha(2018,'el 2018 se dio el mundial de rusia').
fecha(2014,'el 2014 se dio el mundial de brasil').
fecha(2010,'el 2010 se dio el mundial de egipto').

FechaEvento():-
    writeln('Digite la fecha: '),
    read(X),
    fecha(X,Y),
    writeln(Y).