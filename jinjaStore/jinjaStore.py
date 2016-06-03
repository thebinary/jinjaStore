"""

Author      : The Binary <binary4bytes@gmail.com>
Purpose     : Store of Jinja Templates for rendering

"""

import os
import inspect
import jinja2

class FileNotFound(Exception):
    pass

class JinjaStore:
    """
    JinjaStore for Templating

    Render using 3 locations:
        - sys : templates included with module
                pointed using templateName as 'sys/<templatePath>'
        - user : user defined path for templates
                pointed using templateName as 'user/<templatePath>'
        - cwd : templates inside current working directory
                pointed using templateName as 'cwd/<templatePath>'

    Note:
        Each <templatePath> will have an implicit 'templates' prepended to the
        path and '.jinja2' appended to the path.
        So, 'cwd/employee/hod' points to file '<cwd>/employee/hod.jinja2'

    """

    def __init__(self, userTemplatePath=''):
        """ JinjaStore initializor """
        modulePath = \
        os.path.dirname(os.path.realpath(inspect.getfile(self.__class__)))
        currentPath = os.getcwd()
        sysTemplatePath = modulePath + os.sep + 'templates'
        cwdTemplatePath = currentPath + os.sep + 'templates'

        # Template Paths Jinja Environments
        userTemplates = None
        if userTemplatePath <> '':
            userTemplates = userTemplatePath + os.sep + 'templates'
            userTemplates = jinja2.Environment()
            userTemplates.loader = jinja2.FileSystemLoader(userTemplatePath)

        sysTemplates = jinja2.Environment()
        sysTemplates.loader = jinja2.FileSystemLoader(sysTemplatePath)

        cwdTemplates = jinja2.Environment()
        cwdTemplates.loader = jinja2.FileSystemLoader(cwdTemplatePath)

        self.sysTemplates = sysTemplates
        self.cwdTemplates = cwdTemplates
        self.userTemplates = userTemplates

    def __renderTemplate(self, templateSelector, templateName, varsDict):
        """ Render Template found in given template location selector """
        return templateSelector.get_template(templateName).render(varsDict)

    def renderTemplate(self, templateName, varsDict):
        """
        Render Template using templateName and given variable Dictionary

        eg: renderTemplate('sys/employee/hod', {'name': 'Binary'})

        """
        selector = templateName.split(os.sep)[0]
        actualTemplateName = os.sep.join(templateName.split(os.sep)[1:]) + \
        ".jinja2"

        templator = None
        if selector == 'sys':
            templator = self.sysTemplates
        elif selector == 'cwd':
            templator = self.cwdTemplates
        elif selector == 'user':
            templator = self.userTemplates

        result = None
        if templator <> None:
            try:
                result = self.__renderTemplate(templator, actualTemplateName, varsDict)
            except jinja2.exceptions.TemplateNotFound as je:
                raise FileNotFound(je)
        return result


if __name__ == '__main__':
    obj = JinjaStore()
    print obj.renderTemplate('sys/samples/employee/hod', { 'employee_id': 100,
        'employee_name': 'Binary'})
