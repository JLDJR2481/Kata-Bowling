class Puntuacion:
    strike = 10
    last_throw = 0
    null = 0

    def __init__(self, points):
        self.points = list(points)

    @staticmethod
    def specials_values(throws):
        total = 0
        for i in throws:
            if i.isdigit():
                total += int(i)
                Puntuacion.last_throw = int(i)

            elif i == 'X':
                total += Puntuacion.strike

            elif i == '-':
                Puntuacion.last_throw = int(Puntuacion.null)

            elif i == '/':
                total += (int(Puntuacion.strike) - int(Puntuacion.last_throw))

        return total

    def calcular_puntos(self):
        total_points = 0
        numbers_of_throws = 0
        numbers_of_throws_in_frame = 0
        frame = 0

        for i in self.points:
            if frame == 9:
                total_points += Puntuacion.specials_values(
                    self.points[numbers_of_throws:])
                return total_points
            elif i.isdigit():
                total_points += int(i)
                Puntuacion.last_throw = i
                if numbers_of_throws_in_frame > 0:
                    numbers_of_throws_in_frame = 0
                    frame += 1
                else:
                    numbers_of_throws_in_frame += 1
                numbers_of_throws += 1

            elif i == '-':
                Puntuacion.last_throw = 0
                if numbers_of_throws_in_frame > 0:
                    numbers_of_throws_in_frame = 0
                    frame += 1
                else:
                    numbers_of_throws_in_frame += 1
                numbers_of_throws += 1

            elif i == 'X':
                total_points += Puntuacion.specials_values(
                    self.points[numbers_of_throws: numbers_of_throws+3])
                numbers_of_throws += 1
                frame += 1

            elif i == '/':
                total_points += int(Puntuacion.specials_values(
                    self.points[numbers_of_throws: numbers_of_throws+2]))
                numbers_of_throws += 1
                numbers_of_throws_in_frame = 0
                frame += 1

        return total_points


if __name__ == "__main__":

    assert 60 == Puntuacion("12345123451234512345").calcular_puntos()

    assert 90 == Puntuacion("9-9-9-9-9-9-9-9-9-9-").calcular_puntos()

    assert 150 == Puntuacion("5/5/5/5/5/5/5/5/5/5/5").calcular_puntos()

    assert 300 == Puntuacion("XXXXXXXXXXXX").calcular_puntos()

    assert 182 == Puntuacion("9/X72X9/X7-X7/XXX").calcular_puntos()
