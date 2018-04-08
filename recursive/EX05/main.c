#include <stdio.h>

int padovan(int n)
{
    if (n <= 3) {
    	return 1;
    }
	return padovan(n - 2) + padovan(n - 3);
}

int main(){
    int n;
    printf("Digite um numero: ");
    scanf("%d", &n);
    printf("O valor eh: %d", padovan(n));
    return 0;
}
