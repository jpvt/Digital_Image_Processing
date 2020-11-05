# Digital_Image_Processing

1º trabalho prático PDI

Desenvolva um sistema para abrir, exibir, manipular e salvar imagens RGB com 24 bits/pixel (8 bits/componente/pixel). O sistema deve ter a seguinte funcionalidade:

1.	Conversão RGB-YIQ-RGB (cuidado com os limites de R, G e B na volta!)
2.	Negativo 

3.	Correlação m x n. Testar com filtros Média e Sobel
4.	Compare a aplicação do filtro média 25x25 com a aplicação do filtro média 25x1 seguido pela aplicação do filtro média 1x25, em termos de tempo de processamento e resultado final
5.	Filtro mediana m x n
6.	Reproduza o exemplo em https://la.mathworks.com/help/images/ref/normxcorr2.html?lang=en com as imagens baboon.png e babooneye.png, mas aplicando a correlação normalizada banda a banda e tomando como resultado a média das três correlações em cada ponto. Você pode utilizar toda a funcionalidade da linguagem de programação de sua escolha, incluindo bibliotecas avançadas.  
7.	Reproduza o item 6 utilizando a função correlação desenvolvida no item 3.
