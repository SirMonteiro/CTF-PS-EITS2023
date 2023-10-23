# WEB - findRobots

## Descrição do desafio

Essa não, não lembro onde deixei meus robos...

## Descrição da solução

O desafio consiste em procurar a flag escondida dentro de um diretório não indexável em uma página web.

Para fazer o desafio, primeiro entra-se na página web disponibilizada, e olhando o código fonte é possível ir navegando até uma página dentro de /segredo/norobots/maybehere.html, que é possível observar que o .css é importado dentro de uma pasta com nome sugestivo, findme, que tentando ir em /segredo/norobots/findme/robots.txt, é possível encontrar uma página denominada secret.html, e finalmente entrando nessa página, é possível encontrar a flag: EiTS{N3v3r_W4nn4_S33_Y0u_4g41n}
