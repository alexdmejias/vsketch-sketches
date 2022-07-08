import vsketch
import random


class Lines01Sketch(vsketch.SketchClass):
    # Sketch parameters:
    line_length = vsketch.Param(2)
    padding_hor = vsketch.Param(2)
    padding_ver = vsketch.Param(2)
    cols = vsketch.Param(10)
    rows = vsketch.Param(10)
    max_num_of_ver_paddings = vsketch.Param(3)

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("a4", landscape=False, center=True)
        vsk.scale("mm")

        for i in range(0, self.cols):
            prev_y = 0
            for _ in range(0, self.rows):
                if (_ != 0):
                    r = random.randint(1, self.max_num_of_ver_paddings)
                    rs = prev_y + (self.padding_ver * r)
                else:
                    rs = 0

                vsk.line(
                    (i * self.line_length) + self.padding_hor,
                    -rs,
                    ((i + 1) * self.line_length),
                    -rs
                )
                prev_y = rs

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    Lines01Sketch.display()
