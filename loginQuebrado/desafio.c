#include <stdio.h>

struct {
	char nome[32];
	int id;
} usuario = {.nome = {0}, .id = 2};

char *mensagens[] = {
	"eits{}",
	"voce nao tem permissao de leitura"
};

int main(void)
{
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);

	printf("Qual o seu nome?\n> ");
	scanf("%s", usuario.nome);

	printf("Ola, %s\n", usuario.nome);

	if (usuario.id <= 0 || usuario.id > (int) sizeof(mensagens)) {
		printf("Usuario inexistente\n");
	}
	else {
		printf("Mensagem: %s\n", mensagens[usuario.id - 1]);
	}
}
