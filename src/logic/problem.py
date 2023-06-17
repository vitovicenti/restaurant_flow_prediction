# Problem.py - Representations Logics
# AIFCA Python3 code Version 0.9.4 Documentation at http://aipython.org
# Download the zip file and read aipython.pdf for documentation

# Artificial Intelligence: Foundations of Computational Agents http://artint.info
# Copyright David L Poole and Alan K Mackworth 2017-2022.
# This work is licensed under a Creative Commons
# Attribution-NonCommercial-ShareAlike 4.0 International License.
# See: http://creativecommons.org/licenses/by-nc-sa/4.0/deed.en

class Clause(object):
    """A definite clause"""

    def __init__(self, head, body=[]):
        """clause with atom head and lost of atoms body"""
        self.head = head
        self.body = body

    def __str__(self):
        """returns the string representation of a clause.
        """
        if self.body:
            return self.head + " <- " + " & ".join(self.body) + "."
        else:
            return self.head + "."


class Askable(object):
    """An askable atom"""

    def __init__(self, atom):
        """clause with atom head and lost of atoms body"""
        self.atom = atom

    def __str__(self):
        """returns the string representation of a clause."""
        return "askable " + self.atom + "."


def yes(ans):
    """returns true if the answer is yes in some form"""
    return ans.lower() in ['yes', 'yes.', 'oui', 'oui.', 'y', 'y.']  # bilingual


from display import Displayable


class KB(Displayable):
    """A knowledge base consists of a set of clauses.
    This also creates a dictionary to give fast access to the clauses with an atom in head.
    """

    def __init__(self, statements=[]):
        self.statements = statements
        self.clauses = [c for c in statements if isinstance(c, Clause)]
        self.askables = [c.atom for c in statements if isinstance(c, Askable)]
        self.atom_to_clauses = {}  # dictionary giving clauses with atom as head
        for c in self.clauses:
            if c.head in self.atom_to_clauses:
                self.atom_to_clauses[c.head].add(c)
            else:
                self.atom_to_clauses[c.head] = {c}

    def clauses_for_atom(self, a):
        """returns set of clauses with atom a as the head"""
        if a in self.atom_to_clauses:
            return self.atom_to_clauses[a]
        else:
            return set()

    def __str__(self):
        """returns a string representation of this knowledge base.
        """
        return '\n'.join([str(c) for c in self.statements])


general_occupation = KB([

    Askable('Event'),
    Askable('Weekend'),
    Askable('Holiday'),
    Askable('Turistic_season'),
    Askable('Working_day'),

    Clause('Open'),

    Clause('occupation_100', ['High_season', 'Weekend', 'Event', 'Open']),
    Clause('occupation_80', ['High_season', 'Weekend', 'Open']),
    Clause('occupation_60', ['High_season', 'Event', 'Open']),
    Clause('occupation_40', ['Event', 'Open']),
    Clause('occupation_20', ['Working_day', 'Open']),

    Clause('High_season', ['Holiday', 'Turistic_season'])

])
