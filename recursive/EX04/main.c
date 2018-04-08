#include <stdio.h>

int fat(int i){
	if(i == 1){
		return 1;
	}else{
		return i * fat(i-1);
	}
}

int super(int i){
	if(i == 0){
		return 1;
	}else{
		return fat(i) * super(i - 1);
	}
}

int main() {
	int i;
	printf("Digite um numero: ");
	scanf("%d", &i);
	printf("O fatorial eh: %d", super(i));
	return 0;
}
