from src.puntuacion import Puntuacion


def test_puntos():
    assert 60 == Puntuacion("12345123451234512345").calcular_puntos()

    assert 90 == Puntuacion("9-9-9-9-9-9-9-9-9-9-").calcular_puntos()

    assert 150 == Puntuacion("5/5/5/5/5/5/5/5/5/5/5").calcular_puntos()

    assert 300 == Puntuacion("XXXXXXXXXXXX").calcular_puntos()

    assert 149 == Puntuacion("72X134/X727-9/7/XXX").calcular_puntos()

    assert 182 == Puntuacion("9/X72X9/X7-X7/XXX").calcular_puntos()

    assert 97 == Puntuacion("8-2181X4/814271427/-").calcular_puntos()

    assert 167 == Puntuacion("8145368/-/5/XXX8/7").calcular_puntos()

    assert 186 == Puntuacion("813/XXXXX638/11").calcular_puntos()

    assert 299 == Puntuacion("XXXXXXXXXXX9").calcular_puntos()

    assert 0 == Puntuacion("--------------------").calcular_puntos()
