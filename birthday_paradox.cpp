#include <bits/stdc++.h>
#define DAYS 365

/*  How many people must be there in a room to make the probability 100%
    that 2 people in the room have same birthday?
    Answer: 367 (since there are 366 possible birthdays, including February 29).

    Input:  2 0.7
    Output: 30 */

/*  Number of people with the same birthday */
int count_people(int n, double p) {
    if(p == 1.0) return DAYS + n;
    return ceil(sqrt(n*DAYS*log(1/(1-p))));
}

/*  Reverse method to find the probability according to the number of people. */
double find_prob(int k) {
    double prob = 1.0;
    for(int i = 1; i <= k; i++)
        prob = prob * ((double) (DAYS - i + 1) / DAYS);
    return 1.0 - prob;
}

int main() {
    /*  n = how many people with the same birthday
        p = probability */
    int n, qtd;
    double p;

    scanf("%d %lf", &n, &p);

    qtd = count_people(n, p);

    printf("%d\n", qtd);
    printf("%.2lf\n", find_prob(qtd));
    return 0;
}
