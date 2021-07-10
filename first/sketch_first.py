import vsketch

class FirstSketch(vsketch.SketchClass):
    totalNumSegments = vsketch.Param(100, ) # the total number of segments in the image
    numSegments = vsketch.Param(4) # number of segments pere full rotation
    radius = vsketch.Param(10) # start radius of the circle
    radiusInc = vsketch.Param(2) # how much the radius grows per segment

    def draw(self, vsk: vsketch.SketchClass) -> None:
        vsk.size("a4", landscape=False)
        vsk.scale("mm")

        radius = self.radius
        start = 0
        degreesPerSegment = 360 / self.numSegments

        for _ in range(self.totalNumSegments):
            end = start + degreesPerSegment
            vsk.arc(0, 0, radius, radius, start, end, degrees=True)
            # vsk.rect(10, 10, 5, 8)
            start = end
            radius += self.radiusInc

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        self.vpype("linemerge linesimplify reloop linesort")

if __name__ == "__main__":
    # vsk = FirstSketch()
    # vsk.draw()
    # vsk.finalize()
    # vsk.display()
    FirstSketch.display()