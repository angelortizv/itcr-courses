function ejem_sust_atras()
  clc; clear; 
  A=[2 -6 12 16;1 -2 6 6;-1 3 -3 -7;0 4 3 -6];
  b=[70 26 -30 -26].';
  x=elim_gauss_sust_atras(A,b)
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

function [Ar,br]=triang_sup(A,b)
  
end

function x=elim_gauss_sust_atras(A,b)
  
end


%Implementar sust_adelante