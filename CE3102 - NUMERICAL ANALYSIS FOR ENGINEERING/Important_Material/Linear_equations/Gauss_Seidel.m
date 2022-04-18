1;
function [xk, k, error]=Gauss_Seidel(A, b, x0, tol, iterMax)
  [L D U] = desc_LDU(A);
  y = sust_adelante(L+D,b);
  xk = x0;
  for k = 1:iterMax
    z = sust_adelante(L+D,U*xk);
    xk = -z+y;
    error=norm(A*xk-b);
    if error<tol
      break
    end
  end
end

%Implementar sust_adelante
function x=sust_adelante(A,b)
  m=length(b);
  x=zeros(m,1);
  x(1)=(1/A(1,1))*(b(1));
  for i=2:m
    aux=0;
    for j=1:i-1
      aux+=A(i,j)*x(j);
    end
    x(i)=(1/A(i,i))*(b(i)-aux);
  end
end

function [L D U]=desc_LDU(A)
  m = size(A);
  L = zeros(m,m);
  D = zeros(m,m);
  U = zeros(m,m);
  diag = 1;
  for k = 1:m
    for j = 1:m
      if j == diag && k == diag
        D(k,j) = A(k,j);
        diag += 1;
      elseif j < diag
        L(k,j) = A(k,j);
      else
        U(k,j) = A(k,j);
      end
    end
  end
end


##function [L D U]=desc_LDU(A)
##  m = size(A);
##  L = zeros(m,m);
##  D = zeros(m,m);
##  U = zeros(m,m);
##  for k = 1:m
##    if k == 1
##      D(k,k) = A(k,k);
##      U(k:m,k) = A(k:m,k);
##    elseif k == m
##      L(1:k,k) = A(1:k,k);
##      D(k,k) = A(k,k);
##    else
##      L(1:k,k) = A(1:k,k);
##      D(k,k) = A(k,k);
##      U(k:m,k) = A(k:m,k);
##    end
##  end
##end


