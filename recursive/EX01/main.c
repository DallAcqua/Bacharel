#include <stdio.h>

void sequencia (int n){
	if(n != 0){
		sequencia(n - 2);
		printf("%d ", n);
	}
}
int main() {
	int n;
	printf("Digite um numero: ");
	scanf("%d", &n);
	sequencia(n);
	return 0;
}
