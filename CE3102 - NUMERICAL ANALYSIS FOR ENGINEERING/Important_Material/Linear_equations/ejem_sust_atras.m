function ejem_sust_atras()
  clc; clear; 
  A=[1 1 -1 3;0 -1 -1 -5;0 0 3 13;0 0 0 -13];
  b=[4 -7 13 -13].';
  x=sust_atras(A,b)
end

function x=sust_atras(A,b)
  m=length(b);
  x=zeros(m,1);
  for i=m:-1:1
    aux=0;
    for j=i+1:m
      aux+=A(i,j)*x(j);
    end
    x(i)=(1/A(i,i))*(b(i)-aux);
  end
end

