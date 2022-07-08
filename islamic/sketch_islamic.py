from shapely.geometry import *
# from sympy as  import Point, Circle, Line, Ray
# import sympy as sympy
import vsketch


class IslamicSketch(vsketch.SketchClass):
    # Sketch parameters:
    # radius = vsketch.Param(2.0)

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("a4", landscape=False)
        vsk.scale("cm")


        # vsk.geometry(Polygon([[-1, -1], [-1, 1], [1, 1], [1, -1]]))

        # p1, p2, p3 = Point(0, 0), Point(5, 5), Point(6, 0)
        # origin = (0, 0)
        # originPoint = sympy.Point(origin)
        # p0 = sympy.Point(-1, -1)
        # c1 = Circle(origin, 1)
        # line = Line(p0, origin)
        # print(c1.intersection(line))
        
        origin = Point(0, 0)

        circle = origin.buffer(1)
        vsk.geometry(circle)
        vsk.stroke(2)
        diag_line = LineString([(0, 0), (-1, -1)])
        # vsk.geometry(diag_line)
        x = circle.intersection(diag_line)
        print(x)
        vsk.geometry(x)

        vsk.stroke(3)
        p1 = Point(0, -1).buffer(.1)
        p3 = Point(-1, 0).buffer(.1)
        p4 = origin.buffer(.1)
        x = Point(-0.7071067811865475, -0.7071067811865475).buffer(.01)
        vsk.geometry(x)

        
        vsk.geometry(p1)
        vsk.geometry(p3)
        vsk.geometry(p4)


    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    IslamicSketch.display()
