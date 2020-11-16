## O que é um coeficiente de correlação?
Estatisticamente, a correlação entre duas variáveis é uma medida de similaridade entre essas. O coeficiente de correlação que utilizamos nessa demonstração é o coeficiente de correlação linear de Pearson, que entre as variáveis **a** e **b** é dado por:

$$
r = \frac{(a - \mu_{a} )}{\left | a - \mu_{a}  \right |} \times \frac{(b - \mu_{b} )}{\left | b - \mu_{b}  \right |}
$$

Sendo **r** o coeficiente de correlação linear de Pearson.


## O que é uma correlação normalizada?

A correlação normalizada é feita com o objetivo de detecar os pontos de uma imagem(ou sinal) que são mais semelhantes aos pontos de uma determinada máscara. Ao passar uma outra imagem como máscara, é possível detectar que pontos da imagem original que são mais parecidos (ou correlacionados) com essa.

Logo, a correlação normalizada entre um sinal **s** e uma máscara **h**, é equivalente ao sinal **g**, em que cada amostra é o coeficiente de correlação linear de Pearson entre **s** e **h** em cada posição da máscara em relação ao sinal.
