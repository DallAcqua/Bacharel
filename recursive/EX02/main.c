#include <stdio.h>

void sequencia (int n){
	if(n != 0){
		printf("%d ", n);
		sequencia(n - 2);
	}
}
int main() {
	int n;
	printf("Digite um numero: ");
	scanf("%d", &n);
	sequencia(n);
	return 0;
}
