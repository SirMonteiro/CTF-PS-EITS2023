# binexp - login quebrado

## Descrição do desafio

Opa... Opa... Parece que não tenho permissão

## Descrição da solução

O desafio consiste em explorar um buffer overflow de forma a substituir o ID de usuário para assim mostrar a primeira string do array mensagens

Para isso, é necessário encher o buffer com 32 caracteres da tabela ASCII mais um número 1, que no caso desse código resulta em 0 e retorna a flag, assim, basta montar o payload com 32 caracteres como o "a", e um "1" interpretado de um hexadecimal para um caractere, com o seguinte comando:

```bash
echo -e 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x01' | nc <endereço> <porta>
```

Assim, a flag encontrada:
eits{l0g4d0_c0m_5uc3550}
