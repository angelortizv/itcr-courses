/*
 tallerimperativo.rkt - archivo correspondiente al taller de Programación Imperativa

 Este archivo es parte de las tareas cortas (talleres) correspondientes a un 5% de la nota
 en el curso de Lenguajes Compiladores e Intérpretes: Módulo Lenguajes. El mismo tiene como
 objetivo, reafirmar el conocimiento del paradigma de programación imperativo.

 Versión de Archivo    :    0.1
 Autor                 :    Angelo Ortiz Vega, Github@angelortizv
 Última Modificación   :    19/09/2019 : 23:30
 */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <assert.h>

//Ejercicio 1: Haga una función que imprima los equivalentes en millas del siguiente rango de kilómetros [1-10]
void km_miles(){
    for(int km = 1; km <= 10; km++){
        float millas = km*(0.621);
        printf("* %d km - %.3f millas\n",km,millas);
    }
}

//Ejercicio 2: Haga un programa que imprima el equivalente de los grados centígrados en Farenheit, debe recibir un valor de entrada.
void celsius_farenheit(int celsius){
    float farenheit = ((celsius*9)/5) + 32; 
    printf("* %d °C - %.2f °F\n",celsius,farenheit);
}

//Ejercicio 3: Escriba una función recursiva para calcular la cantidad de digitos de un número.
int digs(int num){
    return digs_aux(num,0);
}

int digs_aux(int num, int digs){
    if(num == 0){
        return digs;
    }
    int n = num/10;
    digs++;
    digs_aux(n,digs);
}

//Ejercicio 4: Escriba una función recusiva para calcular la cantidad de digitos pares de un número.
int pairs(int num){
    return pairs_aux(num,0);
}

int pairs_aux(int num, int digs){
    if(num == 0){
        return digs;
    } else{
        if((num%10)%2 == 0){
            digs++;
        }
    } 
    int n = num/10;
    pairs_aux(n,digs);
}

//Ejercicio 5: Escriba la siguiente función: int strcmp(char *s, char *p)
//Ejercicio 6: La función compara el largo del string s con el de p y devuelve un valor <0 si s<p; 0 si s==p; >0 si s>p
int stringLength(char *str){
    int i = 0;
    while (str[i] != '\0'){
        i++;	
    }
    return i;
}

int strcmp(char *s, char *p){
    if (stringLength(s) < stringLength(p))
        return -1;
    if (stringLength(s) > stringLength(p))
        return 1;
    if (stringLength(s) == stringLength(p))
        return 0;
}

//Ejercicio 7: Escriba la siguiente función: void strcat(char *dest, char *src) La función pega al final del string dest el valor del string src
char* strcat(char *dest, char *src){
    int i = 0, j = 0;
    char *res = (char*) malloc(sizeof(dest) + sizeof(src) + 1);
    while (dest[i] != '\0') {
        res[i] = dest[i];
        i++;
    }
    while (src[j] != '\0'){
        res[i] = src[j];
        i++;
        j++;
    }
    res[i] = '\0';
    return res;
}

//Ejercicio 8: Escriba un programa que imprima una lista de todas las palabras de un documento y para cada palabra una lista de los números en línea en los que aparece
//Ejercicio 9: Escriba un programa que imprima las distintas palabras de su entrada, ordenadas en forma descendente de acuerdo con su frecuencia de ocurrencia. Precede a cada palabra por su conteo.
