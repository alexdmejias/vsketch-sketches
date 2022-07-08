import vsketch


class HalfCirclesSketch(vsketch.SketchClass):
    # Sketch parameters:
    # radius = vsketch.Param(2.0)

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("a3", landscape=False)
        vsk.scale("cm")

        # implement your sketch here
        vsk.arc(0, 0, 30, 30, 0, 180, degrees=True)

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    HalfCirclesSketch.display()
