1;
function [L,U] = sol_LU(A)
  m = length(A);
  U = A;
  L = eye(m);
  for k = 1:m-1
    for j = k+1:m
      L(j,k)=U(j,k)/U(k,k);
      U(j,k:m) = U(j,k:m)-L(j,k)*U(k,k:m);
    end
  end
end