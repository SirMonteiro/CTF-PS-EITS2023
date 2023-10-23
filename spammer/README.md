# binexp - spammer

## Descrição do desafio

As vezes força bruta é a melhor opção...

## Descrição da solução

O desafio consiste em explorar um buffer overflow básico para sobrescrever a variável booleana com um valor diferente de zero

Para a resolução, como sugere o nome, basta enviar um spam de caracteres que seja pelo menos um pouco maior que o tamanho do buffer, assim, o valor da variável booleana será sobrescrito e o programa irá imprimir a flag.

Para isso, basta executar o seguinte comando:

```bash
echo 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' | nc <endereço> <porta>
```

Assim, a flag encontrada:
eits{gr1t4nd0_qu3_53_r3s0lv3}
