#include <stdio.h>
#include <stdlib.h>

void vitoria(void)
{
	printf("eits{RETIRADA}\n");
	exit(0);
}

void enviar_mensagem(char *msg)
{
	char buffer[32];
	sprintf(buffer, "A mensagem eh: \"%s\"", msg);
	printf("%s\n", buffer);
}

int main(void)
{
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);

	printf("O alvo: %p\n", (void *)vitoria);

	printf("Mensagem\n> ");
	char *msg = NULL;
	scanf("%ms", &msg);
	enviar_mensagem(msg);
}
