function [x,error,k]=biseccion(f1,a,b,tol,iterMax)
 
pkg load symbolic


f2=sym(f1); %Python -> Sympyfy (SymPy)
f=matlabFunction(f2); %Python -> Lambify (SymPy)
 
%f=@(x) exp(x)-2*x-10; %Definir f

if f(a)*f(b)<0    %Paso 1
  for k=1:iterMax
    x=(a+b)/2;      %Paso 2
    if f(a)*f(x)<0  %Paso 3
      b=x;
    else
      a=x;  
    end    
    error=abs(f(x));
    if error<tol  %Paso 4
      break
    end
  end  
else
  display('No cumple el teorema de Bolzano')
end
 
end
