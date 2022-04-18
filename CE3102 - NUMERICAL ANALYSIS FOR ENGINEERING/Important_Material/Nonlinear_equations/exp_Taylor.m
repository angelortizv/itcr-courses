function y=exp_Taylor(a,tol)
  
    suma=0;
        iterMax=1000;
  for n=0:iterMax
    sumak=suma+a^n/factorial(n);
    e_rel=abs(sumak-suma)/abs(sumak);
    suma=sumak;
    if e_rel<tol
      y=sumak;
      break
    end
  end

end
