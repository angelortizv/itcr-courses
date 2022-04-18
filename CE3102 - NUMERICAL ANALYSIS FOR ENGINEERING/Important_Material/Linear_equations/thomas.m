1;
function thomas()
  m = 100;
  matriz_diag;
  A = matriz_diag(m); b=[-12 -14*ones(1,m-2) -12]';
  n = length(A);
  xn = [0*ones(1,m-2)];
  xn = rec(A,b,1,n,xn,0,0)
end

function xn = rec(A,b,i,n,xn,p,q)
  if i == n
    qi = (b(i)-q*A(i,i-1))/(A(i,i)-p*A(i,i-1));
    xi = qi;
    xn(i) = xi;
  elseif i == 1
    pi = A(i,i+1)/A(i,i);
    qi = b(i)/A(i,i);
    xn = rec(A,b,i+1,n,xn,pi,qi);
    xn(i) = qi - pi*xn(i+1);
  else
    pi = A(i,i+1)/(A(i,i)-p*A(i,i-1));
    qi = (b(i)-q*A(i,i-1))/(A(i,i)-p*A(i,i-1));
    xn = rec(A,b,i+1,n,xn,pi,qi);
    xn(i) = qi - pi*xn(i+1);
  end
end