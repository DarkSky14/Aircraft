def _debag():
    try:
        with open("module/correct_start.py") as correct:
            correct.close()
        return ""
    except FileNotFoundError:
        return "src/"


fix_import = _debag()
