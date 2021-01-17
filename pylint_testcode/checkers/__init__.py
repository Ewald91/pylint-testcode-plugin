from pylint_testcode.checkers.AbsoluteUrl import AbsoluteUrlChecker
from pylint_testcode.checkers.MissingAssertion import AssertionsChecker

def register_checkers(linter):
    linter.register_checker(AbsoluteUrlChecker(linter))
    linter.register_checker(AssertionsChecker(linter))