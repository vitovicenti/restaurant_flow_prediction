# logicTopDown.py - Top-down Proof Procedure for Definite Clauses
# AIFCA Python3 code Version 0.9.4 Documentation at http://aipython.org
# Download the zip file and read aipython.pdf for documentation

# Artificial Intelligence: Foundations of Computational Agents http://artint.info
# Copyright David L Poole and Alan K Mackworth 2017-2022.
# This work is licensed under a Creative Commons
# Attribution-NonCommercial-ShareAlike 4.0 International License.
# See: http://creativecommons.org/licenses/by-nc-sa/4.0/deed.en


from src.logic.problem import yes


def prove( kb, ans_body, indent="" ):
    """returns True if kb |- ans_body
    ans_body is a list of atoms to be prove
    """
    flag = True

    kb.display(2, indent, 'yes <-', ' & '.join(ans_body))
    if ans_body:
        selected = ans_body[0]  # select first atom from ans_body
        print(" Proving -> ", selected)
        if selected in kb.askables:

            return (yes(input("\n     Is " + selected + " true? \n"))

                    and prove(kb, ans_body[1:], indent + "    "))
        else:

            return any(prove(kb, cl.body + ans_body[1:], indent + "    ")
                       for cl in kb.clauses_for_atom(selected))
    else:

        return True  # empty body is true


def g():
    from src.logic.problem import general_occupation

    occupation = 0

    if bool(prove(general_occupation, ['occupation_100'])):
        occupation = 100

    elif bool(prove(general_occupation, ['occupation_80'])):
        occupation = 80

    elif bool(prove(general_occupation, ['occupation_60'])):
        occupation = 60

    elif bool(prove(general_occupation, ['occupation_40'])):
        occupation = 40

    elif bool(prove(general_occupation, ['occupation_20'])):
        occupation = 20

    return occupation
