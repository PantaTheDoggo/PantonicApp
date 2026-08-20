"""Fixture project for T5b (docs/plans/P-0731-v2-extracao-modalidade.md ### T5b) — TR
counterpart of `qt_project/widget.py`: identical class shape, but this project has NO
`.claude/framework-virtuals.txt`. Proves the exception is never granted without an
explicit project declaration.
"""


class MyWidget(QWidget):
    """Same shape as the declared fixture (`qt_project/widget.py`) — no declaration
    here means no exception is granted for the override below."""

    def paint(self, painter, option, index):
        """Would be excused as a framework-dispatched virtual if this project
        declared `QWidget`/`paint` in `.claude/framework-virtuals.txt`, the way
        `qt_project/` does. Without that declaration this is just a plain method
        with no explicit `.paint()` caller anywhere in this fixture — MUST be
        flagged as dead code."""
        return None
