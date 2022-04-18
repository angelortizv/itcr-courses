function L=fact_cholesky(A)
  m=size(A,1);
  L=zeros(m,m);
  
  %Columna 1 de L  
  L(1,1)=sqrt(A(1,1));
  for i=2:m
    L(i,1)=(1/L(1,1))*A(i,1);
  end
  
  %Columnas j=2,...,m  
  for j=2:m
    %Valor de la Diagonal
    sumAux1=0;
    for k=1:j-1
      sumAux1+=L(j,k)^2;
    end
    L(j,j)=sqrt(A(j,j)-sumAux1);
    %Valor debajo de la Diagonal
    for i=j+1:m
      sumAux2=0;
      for k=1:j-1
        sumAux2+=L(i,k)*L(j,k);
      end      
      L(i,j)=(1/L(j,j))*(A(i,j)-sumAux2);
    end
  end
end
