#include <stdio.h>
#include <math.h>

/*  Se você lançar uma moeda M vezes, quantas sequências de N caras você pode esperar?
    Resposta: M*(1/2^N).
    Só há 2 formas para 1 jogada: cara ou coroa. Portanto, 1/2^N.*/

int main() {
    int m, n, seq;
    scanf("%d %d", &m, &n);

    seq = (int) round(m*(1.0/pow(2, n)));
    printf("%d\n", seq);
    return 0;
}
