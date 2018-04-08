#include <stdio.h>

int fat(int i){
	if(i <= 1){
		return 1;
	}else{
		return i * fat(i-2);
	}
}

int main() {
	int i;
	printf("Digite um numero: ");
	scanf("%d", &i);
	printf("O fatorial eh: %d", fat(i));
	return 0;
}
