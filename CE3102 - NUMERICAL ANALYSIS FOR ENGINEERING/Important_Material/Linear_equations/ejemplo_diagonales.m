%Ejemplo para obtener las diagonales de una matriz
%tridiagonal

A=[1  2 0  0;
   1 -5 3  0;
   0  1 6  3;
   0  0 1 -22];
   
%Forma 1: Sirve para cualquier lenguaje
a=[0]; %Diagonal de abajo
b=[]; %Diagonal principal
c=[]; %Diagonal de arriba

m=size(A,1);

%Almacenar valores de la primera fila
b=[b A(1,1)];
c=[c A(1,2)];

%Almacenar valores de las filas 2,3,...,m-1
for i=2:m-1
  a=[a A(i,i-1)];
  b=[b A(i,i)];
  c=[c A(i,i+1)];
end

%Almacenar valores de la fila m
a=[a A(m,m-1)];
b=[b A(m,m)];

c=[c 0];


%Forma 2: Solo sirve en Octave y Matlab
a=diag(A,-1)
a=[0 a];
b=diag(A)
c=diag(A,1)
c=[c 0];

