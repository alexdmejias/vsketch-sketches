import vsketch
import numpy as np
from random import uniform

def randVector(m):
    return [uniform(-m , m), uniform(-m , m)]


class CirclesSketch(vsketch.SketchClass):
    # Sketch parameters:
    circles_qty = vsketch.Param(20)
    r = vsketch.Param(10)
    inc = vsketch.Param(4)

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("a3", landscape=False, center=True)
        vsk.scale("mm")

        maxX = 0
        minX = 0
        maxY = 0
        minY = 0

        for i in range(self.circles_qty):
            # circle(  0, 0, r + (i * inc))
            vsk.circle(0, 0, self.r + (i * self.inc), mode="radius")

            # const {x, y} = p5.Vector.random2D().mult(inc / 2)
            # x, y = 5 * (np.random.rand(2)) - 2.5
            x, y = randVector(self.inc / 2)

            # translate(x, y)
            vsk.translate(x, y)
            print(x)
            # maxX = x > maxX ? x : maxX
            maxX = x if x > maxX else maxX
            # minX = x < minX ? x : minX
            minX = x if x < minX else minX

            # maxY = y > maxY ? y : maxY
            maxY = y if y > maxY else maxY
            # minY = y < minY ? y : minY
            minY = y if y < minY else minY

        print(f"vsk minX: {minX} maxX: {maxX}, minY: {minY} maxY: {maxY}")
        print("p5  minX: -9.99485041800317  maxX: 9.999151175532372, minY: -9.53499678839993  maxY: 9.99014779715518 (sample)")
        print("\n")


    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    CirclesSketch.display()
