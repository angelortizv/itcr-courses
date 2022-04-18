1;
function [x, error, k] = NewtonRaphson(f0, x, tol, iterMax)
  
pkg load symbolic

f1 = sym(f0);

f = matlabFunction(f1);
fp = matlabFunction(diff(f1));

for k = 0:iterMax
  if isequal(fp(x), 0)
    display("No cumple las condciones para aplicar el teorema de Newton-Raphson");
    break
  else
    error = abs(f(x));
    if error < tol
      break
    else
      x = x - f(x)/fp(x);
    end
  end
end