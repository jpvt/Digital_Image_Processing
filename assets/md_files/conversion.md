## O que é uma imagem digital?

Uma imagem digital é composta de pixels, cada um com quantidades finitas e discretas de representação numérica para sua intensidade. A imagem digital contém um número fixo de linhas e colunas de pixels, normalmente armazenados na memória do computador como uma imagem raster, uma matriz bidimensional de pequenos inteiros, cada um representando uma cor associada a um pixel específico.

## O que é o espaço RGB?

O espaço RGB foi desenvolvido com propósito de reproduzir as cores em dispositivos eletrônicos como telas de monitores. Nesse cada pixel consiste em três canais, cada um representando uma cor (R para vermelho, G para verde e B para azul). Normalmente, 8 bits são reservados para cada componente (canal), o que se diferencia em 256 níveis de intensidade diferentes para cada cor, resultando em aproximadamente 16 milhões de cores reproduzidas no total.

## O que é o espaço YIQ?

O espaço YIQ também é utilizado para reproduzir cores. O sistema YIQ é mais utilizado pelo sistema de TV em cores NTSC, adotado principalmente na América do Norte e Central e no Japão. I e Q representam a crominância e Y a luminância. O espaço utiliza uma combinação linear das diferenças entre os valores RGB. Podendo ser calculado da seguinte forma:

$$
R, G, B, Y  \in [0, 1], I  \in [-0.5957, 0.5957], Q \in [-0.5226, 0.5226]
$$


$$
\begin{bmatrix}
Y\\ 
I\\ 
Q
\end{bmatrix} = \begin{bmatrix}

0.299 & 0.587  & 0.114\\ 
0.596 & -0.274 & -0.322\\ 
0.211 & -0.523 & 0.312
\end{bmatrix}

\cdot

\begin{bmatrix}
R\\ 
G\\ 
B
\end{bmatrix}
$$

Sendo assim, é possível representar o espaço RGB, como uma combinação linear entre os valores YIQ:

$$
\begin{bmatrix}
R\\ 
G\\ 
B
\end{bmatrix} = \begin{bmatrix}

1.0 & 0.956  & 0.621\\ 
1.0 & -0.272 & -0.647\\ 
1.0 & -1.106 & 1.703
\end{bmatrix}

\cdot

\begin{bmatrix}
Y\\ 
I\\ 
Q
\end{bmatrix}
$$

Logo, observa-se que com essas combinações é possível representar uma imagem RGB como YIQ e uma imagem YIQ como RGB. Então a partir disso podemos fazer os conversores RGB-YIQ e YIQ-RGB apenas calculando essas fórmulas. Veja o exemplo em código utilizando o pacote Numpy:

* RGB - YIQ
```py

# Matriz YIQ
matrix_yiq = np.array([[0.299, 0.587, 0.114],
                       [0.596, -0.274, -0.322],
                       [0.211, -0.523, 0.312]
                      ])

# Na Matriz YIQ é possível observar que os vetores não estão representados
# como deveriam, visto que matematicamente cada vetor é representado pela
# coluna e não pela linha. Portanto será necessário transpor a matriz.

# arr_img == Array que representa a imagem

yiq_image = np.dot(arr_img, matrix_yiq.T)

# E simples assim temos nossa imagem YIQ

```

* YIQ - RGB
```py
# Matriz YIQ
matrix_rgb = np.array([
                        [1.0, 0.956, 0.621],
                        [1.0, -0.272, -0.647],
                        [1.0, -1.106, 1.703]
                      ])

# Na Matriz RGB é possível observar que os vetores não estão representados
# como deveriam, visto que matematicamente cada vetor é representado pela
# coluna e não pela linha. Portanto será necessário transpor a matriz.

# arr_img == Array que representa a imagem

rgb_image = np.dot(arr_img, matrix_yiq.T)

# E simples assim temos nossa imagem RGB de volta
```
