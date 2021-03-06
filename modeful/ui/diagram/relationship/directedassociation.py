from kivy.graphics import Color, Line

from modeful.ui.diagram.relationship import Trigonometry
from modeful.ui.diagram.relationship.association import Association


class DirectedAssociation(Association):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        with self.canvas.before:
            Color(0, 0, 0, .5)
            self._arrowhead_line = Line(points=[], width=1)

    def redraw(self, x1, y1, x2, y2):
        super().redraw(x1, y1, x2, y2)

        points = Trigonometry.get_arrowhead_points(x1, y1, x2, y2, size=20)
        self._arrowhead_line.points = points
