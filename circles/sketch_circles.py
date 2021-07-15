import vsketch
import numpy as np
from random import random

def randVector():
    return [random(), random()]


class CirclesSketch(vsketch.SketchClass):
    # Sketch parameters:
    circles_qty = vsketch.Param(20)
    radius = vsketch.Param(10)
    radius_inc = vsketch.Param(4)

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("a4", landscape=False, center=True)
        vsk.scale("mm")

        for i in range(self.circles_qty):
            vsk.circle(0, 0, self.radius + (i * self.radius_inc), mode="radius")
            x, y = np.random.rand(2) * 10
            print(f"{x} - {y}")
            vsk.translate(x, y)

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    CirclesSketch.display()
