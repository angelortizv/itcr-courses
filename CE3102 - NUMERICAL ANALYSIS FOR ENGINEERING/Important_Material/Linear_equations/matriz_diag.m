1;
function M=matriz_diag(n)
    M=zeros(n);
    M(1,1)=5; M(1,2)=1; % Primera fila
    M(n,n)=5; M(n,n-1)=1; %Ultima fila
    for i=2:n-1             % Restantes Filas
        M(i,i)=5;
        M(i,i-1)=1;
        M(i,i+1)=1;
    end
end