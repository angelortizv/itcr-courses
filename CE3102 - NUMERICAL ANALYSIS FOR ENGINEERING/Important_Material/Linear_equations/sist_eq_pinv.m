1;
function [xk,error,k]=sol_pinv(A,b,tol,iterMax)
  X=(1/norm(A,2)^2)*A'; %Valor inicial
  xk=X*b; %Aproximacion a la solucion del problema
  I=eye(size(A,1));
  for k=1:iterMax
    X=X*(2*I-A*X); %Actualizar iteracion de la pseudoinversa
    xk_n=X*b;  %Actualizar iteracion de la soluciè´—n
    error=norm(xk_n-xk)/norm(xk_n); %Error
    xk=xk_n;
    if error<tol
      break
    end    
  end
end