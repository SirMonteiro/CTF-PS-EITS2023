#include <stdio.h>
#include <stdbool.h>

struct {
	char nome[32];
	bool permitido;
} usuario = {.nome = {0}, .permitido = false};

int main(void)
{
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);

	printf("Qual o seu nome?\n> ");
	scanf("%s", usuario.nome);

	if (usuario.permitido) {
		printf("Ola %s, aqui esta a sua flag: %s\n", usuario.nome, "eits{REMOVIDA}");
	}
	else {
		printf("Ola %s, voce nao tem permissao para ver a flag\n", usuario.nome);
	}
}
