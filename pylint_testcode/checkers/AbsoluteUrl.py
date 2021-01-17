from urllib.parse import urlparse
from pylint import checkers
from pylint import interfaces

from pylint_testcode.__pkginfo__ import BASE_ID


class AbsoluteUrlChecker(checkers.BaseChecker):
    '''
    This checker will track down all test-methods and functions and
    check if they include at least 1 assertion of any kind.
    '''
    __implements__ = interfaces.IAstroidChecker

    name = 'no-absolute-url'

    msgs = {
        'W%d01' % BASE_ID: ("No absolute url in open browser command.",
                  'no-absolute-url',
                  'Avoid using absolute urls. Use a base-url in your project '
                  'configuration instead. '
                  ),
        }
    def __init__(self, linter=None):
        super(AbsoluteUrlChecker, self).__init__(linter)
        self._webdriver_variable = ''

    def is_absolute(self, url):
        return bool(urlparse(url).netloc)

    def get_webdriver_variable(self, node):
        try: 
            for child in node.body:
                if child.value.func.expr.name == 'webdriver':
                    self._webdriver_variable = child.targets[0].name # webdriver instance name 
                    return True
        except AttributeError:
            pass

    def visit_functiondef(self, node):        
        if self.get_webdriver_variable(node):
            driver = self._webdriver_variable
            try:
                for child in node.body:
                    if  (child.value.func.attrname == 'get' and # check on .get method
                        child.value.func.expr.name == driver): # see if .get method is called on webdrivers instance
                        if self.is_absolute(child.value.args[0].value):# find input string to .get method
                            self.add_message('no-absolute-url', node=node)
            except AttributeError:
                pass
