"""Fixture project for T5a (docs/plans/P-0731-v2-extracao-modalidade.md ### T5a).

Pure Python — never imports PySide6. `dead_code.py` only reads class bases as AST
names (`^Q[A-Z]` textual match), it never executes the module it sweeps, so `QWidget`
below does not need to exist or be importable.
"""


class MyWidget(QWidget):
    """Qt-derived class (base matches ^Q[A-Z]) overriding a canonical virtual."""

    def paint(self, painter, option, index):
        """Framework-dispatched virtual (moc/C++) — no explicit `.paint()` caller
        anywhere in this fixture. Must NOT be flagged as dead code."""
        return None


def orphan_function():
    """Production symbol with no caller anywhere in this fixture.

    Exists so the test can distinguish "the override was correctly excused" from
    "the sweep found nothing at all" — this one MUST be flagged.
    """
    return None
