1;
function [x1, k, error] = MetodoSecante(f0, x0, x1, tol, iterMax)
  
pkg load symbolic

f1 = sym(f0);
f = matlabFunction(f1);

arr = [];

for k = 0:iterMax
  if isequal(f(x1)-f(x0), 0)
    display("No cumple las condciones para aplicar el teorema de Newton-Raphson");
    break
  else
    error = abs(f(x1));
    arr(k + 1) = error;
    if error < tol
      break
    else
      xtemp = x0;
      x0 = x1;
      x1 = x1 - ((x1-xtemp)*f(x1))/(f(x1)-f(xtemp));
    end
  end
plot(arr, 0:k)
grid on;
xlabel("Error");
ylabel("Iteraciones");
title("Grafica Iteraciones vs Error");
end