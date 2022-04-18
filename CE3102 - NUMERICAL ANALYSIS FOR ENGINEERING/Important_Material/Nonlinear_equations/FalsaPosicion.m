1;
%Ecuación cos(x)=x en [0.5,pi/4]
function [xk, k, error] = FalsaPosicion(f0, a, b, tol, iterMax)

a = 0.5;
b=pi/4;
%f1 = sym(f0);
%f = matlabFunction(f1);
f = @(x) cos(x)-x;
iterMax = 1000;
tol = 1e-6;

if f(a)*f(b)<0 %Paso 1
  %Paso 2
  x0=a;
  x1=b;
  
  xk=x1-(x1-x0)*f(x1)/(f(x1)-f(x0));
  for k=2:iterMax
    if f(a)*f(xk)<0 %[a,xk]
      xkp1=xk-(xk-a)*f(xk)/(f(xk)-f(b));
      b=xk;
    else %f(xk)*f(b)z0
      xkp1=xk-(xk-b)*f(xk)/(f(xk)-f(b));
      a=xk;
    end
    xk=xkp1;
    %Paso 3.3
    error = abs(f(xk));
    if error<tol
      break
    end
  end
else
    display("No cumple las condiciones")
end
