import vsketch

class TwoSketch(vsketch.SketchClass):
    def draw(self, vsk: vsketch.SketchClass) -> None:
        vsk.size("a4", landscape=False)
        vsk.scale("cm")

        # for j in range(22):
        #     with vsk.pushMatrix():
        #         for i in range(12):
        #             with vsk.pushMatrix():
        #                 vsk.rotate(0.03 * vsk.random(-j, j))
        #                 vsk.translate(
        #                     0.01 * vsk.randomGaussian() * j,
        #                     0.01 * vsk.randomGaussian() * j,
        #                 )
        #                 vsk.rect(0, 0, 1, 1)
        #             vsk.translate(1, 0)
        #     vsk.translate(0, 1)
        vsk.line(0, 0, 10, 20)
        vsk.rect(10, 10, 5, 8)
        vsk.circle(2, 2, radius=3)
        vsk.triangle(0, 0, 1, 1, 0, 1)

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")

if __name__ == "__main__":
    TwoSketch.display()