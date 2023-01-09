# Kata-Bowling

## Indice

- [**Bolos**](#bolos)
  - [**Distribución de los bolos**](#distribucion-de-los-bolos)
  - [**Puntuación**](#puntuacion)
    - [**Marcador**](#marcador)

## Bolos

Los bolos son un deporte el cual consiste en tirar unos objetivos llamados bolos, por turnos. Cada jugador tiene 2 tiros por cada frame, el cual le permitirá tirar el máximo de bolos posibles para que estos se sumen. Un ejemplo muy claro sería un frame en el cual se tiraron 2 bolos en el primer turno y 7 en el segundo. Este jugador no ha conseguido tumbar los 10 bolos, por lo cual no se le aplica ninguna bonificacion especial y se le sumaría 9.

Son un total de 10 frames, de los cuales 9 son de 2 tiradas; y el décimo de 3 tiradas siempre que el jugador haga pleno o semipleno. En caso contrario, el jugador solo tendrá 2 tiradas en el último frame.

### Distribucion de los bolos

![distribucion bolos](https://user-images.githubusercontent.com/115024410/211366984-099f043e-e17a-4cd0-bc36-5e625c1bb9bd.png)

### Puntuacion

En los bolos, se puntúan los bolos tumbados durante toda la partida de forma acumulativa. Normalmente, en el tablero de puntos se colocan números excepto en algunas ocasiones:

- Semipleno: Si el jugador no ha tumbado los 10 bolos en la primera tirada pero si tumba los bolos restantes en la segunda, esto se conoce como **semipleno** o **spare**. En el tablero sale representado con un / y no se coloca ninguna puntuación hasta que el jugador que haya conseguido el semipleno haga otra tirada. El semipleno puntúa 10 + los bolos tumbados en la siguiente tirada por el jugador. Por ejemplo, el jugador tiene acumulado 20 puntos, y consigue un semipleno (7 /). Despúes, el mismo consigue tumbar 8 bolos en su siguiente turno. La suma de puntuación sería 20 + (10+8) = 38

- Pleno: Si el jugador tumba los 10 bolos en la primera tirada del frame, se conoce como **pleno** o **strike**. En este caso, se representa en el tablero como una X en la primera casilla del frame, y no se puntúa de inmediato, ya que el jugador debe sumar la puntuación de este frame (10, al ser pleno) más los bolos tumbados en los siguientes 2 tiros. Si este mismo consigue otro pleno, debe tener en cuenta la acumulación del primer pleno conseguido y del segundo. En este caso, hay 2 ejemplos:

  1. Un jugador tiene una puntuación de 30 y realiza un pleno. Despues, realiza un semipleno (6 /). Aquí, el jugador debe sumar 30 + (10 + 10), ya que el semipleno son 2 tiradas. Es decir, que la puntuación del pleno sería 30 + 20 = 50. Además, el mismo debe dejar vacío el frame del semipleno ya que debe aplicar la regla del mismo.

  2. Un jugador va en buena racha y realiza 5 plenos consecutivos y en el 6º frame realiza 7 2. En este caso, el primer pleno sería 10 + 10 + 10 (1er pleno + 2º pleno + 3er pleno) y así hasta el cuarto, donde sumaría 10 + 10 + 7 (4º pleno, 5º pleno y primera tirada del 6º frame); y el quinto sumaría 10 + 7 + 2.
     En este caso, la puntuación total sería 30 + 30 + 30 + 27 + 19 = 136

- Split: El split es el terror de los jugadores. Simplemente trata de tener el mismo numero de bolos en ambos lados siempre que el bolo 1 ("el pico de la montaña") esté tumbado. En este caso, se suele dar un bonus por realizar el semipleno (desconozco que bonus tiene actualmente), y se marca con el numero de bolos tumbado en la primera tirada rodeado por un circulo rojo.

- Fallo: Se considera fallo una tirada la cual no tumba ningún bolo, ya sea por que se ha ido por los canales o por que la bola se va hasta el fondo sin tumbar ni un bolo. Aquí, en el frame se coloca un -, indicando una tirada fallida

- Falta: Se considera falta si el jugador pisa la linea o la atraviesa. En este caso se colocará directamente un 0 en el cuadro del frame

#### Marcador

![hoja de puntuacion](https://user-images.githubusercontent.com/115024410/211367033-3f7cfd07-3829-487a-a4b8-35f908ea1cd3.jpg)
