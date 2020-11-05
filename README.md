# Digital_Image_Processing

## API - OpenDIP


1. Converter: Classe responsável pelas conversões disponíveis na API, para essa primeira versão ela terá os seguintes métodos: 1. RGB2YIQ; 2. YIQ2RGB; 3. visualize_image(só a imagem após conversão); 4. visualize_all_process(visualizar imagem antes e depois).

2. Filter: Classe responsável pelos filtros disponíveis na API, terá os seguintes métodos: 1. apply_sobel_filter; 2. apply_median_filter; 3. apply_box_linear_filter; 4. apply_negative; 4. visualize_image(só a imagem após conversão); 5. visualize_all_process(visualizar imagem antes e depois).

3. Correlator: Classe responsável por fazer correlação e convolução, terá os seguintes métodos: 1. apply_correlation; 2. apply_norm_correlation


## Especificação do trabalho


Desenvolva um sistema para abrir, exibir, manipular e salvar imagens RGB com 24 bits/pixel
(8 bits/componente/pixel). O sistema deve ter a seguinte funcionalidade:
1. Conversão RGB-YIQ-RGB (cuidado com os limites de R, G e B na volta!)
2. Negativo
3. Correlação m x n. Testar com filtros Média e Sobel
4. Compare a aplicação do filtro média 25x25 com a aplicação do filtro média 25x1
seguido pela aplicação do filtro média 1x25, em termos de tempo de processamento
e resultado final
5. Filtro mediana m x n
6. Reproduza o exemplo em
https://la.mathworks.com/help/images/ref/normxcorr2.html?lang=en com as
imagens baboon.png e babooneye.png, mas aplicando a correlação normalizada
banda a banda e tomando como resultado a média das três correlações em cada
ponto. Você pode utilizar toda a funcionalidade da linguagem de programação de
sua escolha, incluindo bibliotecas avançadas.
7. Reproduza o item 6 utilizando a função correlação desenvolvida no item 3.
O sistema deve ser desenvolvido em uma linguagem de programação de sua escolha. Não
use bibliotecas ou funções especiais de processamento de imagens imagem baboon.png e
babooneye.png, exceto no item 6, em que o uso de funções avançadas é livre. Para o item 2, duas
formas de aplicação devem ser testadas: em RGB (banda a banda) e na banda Y, com
posterior conversão para RGB.
Observações:
1. O trabalho pode ser feito em grupo, com até cinco componentes.
2. Para integralização das notas, o trabalho deve ser apresentado na data e horário
marcados, juntamente com um relatório, contendo pelo menos as seguintes
seções: introdução (contextualização e apresentação do tema, fundamentação
teórica, objetivos), materiais e métodos (descrição das atividades desenvolvidas e
das ferramentas e conhecimentos utilizados) resultados, discussão (problemas e
dificuldades encontradas, comentários críticos sobre os resultados) e conclusão.
Cada componente do grupo deve estar familiarizado com o trabalho desenvolvido
pelos demais componentes do seu grupo, e todos devem comparecer à
apresentação dos trabalhos.

