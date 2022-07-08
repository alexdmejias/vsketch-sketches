import vsketch
from shapely.geometry import LineString


def advance_direction(curr):
    return 0 if curr == 3 else curr

class SquaresSketch(vsketch.SketchClass):
    # Sketch parameters:
    # radius = vsketch.Param(2.0)
    starting_direction = 2
    current_direction = 0
    length = 5
    padding = 10

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("a4", landscape=False)
        vsk.scale("cm")

        points = []

        for i in range(5):
            x = 0
            y = 0

            if self.current_direction == 0:
                y = -self.length * i
            if self.current_direction == 1:
                x = -self.length * i
            if self.current_direction == 2:
                y = -self.length * i
            else :
                x = -self.length * i

            points.append((x, y))

            self.length += self.padding
            advance_direction(self.current_direction)

        vsk.geometry(LineString(points))
        # implement your sketch here
        # vsk.circle(0, 0, self.radius, mode="radius")

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    SquaresSketch.display()
