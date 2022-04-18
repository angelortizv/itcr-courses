1;
function [xk,k,error]=sol_jacobi(A,b,x0,iterMax,tol)
  xk=x0;
  %P1:
  d=diag(A); %Vector diagonal
  D=diag(d); %Matriz diagonal
  %P2: 
  LmU=A-D;
  %P3:
  d_in=1./d; %Vector con inverso multiplicativo de d
  D_in=diag(d_in); %La inversa de D
  %P4:
  z=D_in*b;
  M=-D_in*LmU;
  %P5
  for k=1:iterMax
    %P5.1
    xk=M*xk+z;
    %P5.2
    error=norm(A*xk-b);
    %P5.3
    if error<tol
      break
    end
  end
end
