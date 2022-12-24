# This is a sample Python script.



# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Template import Template
from TemplateEnvironment import TemplateEnvironment
import re

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #TODO: Global variable
    #TODO: Script block

    env = TemplateEnvironment()
    print(env.TemplateFolder)
    template = env.get_template("HelloWorldTemplate.html")
    # print(template)
    # template.render("Hello",a="AAAA",b="BBB")

    pattern = "\s"
    matches = re.split(pattern,template.template_text)
    # print(matches)
    str=""
    for match in matches :
        str = str + match
    # print(str)

    # print(Template.globals["Company"])
    # print(Template.globals["Copyright"])
    #
    # print(TemplateEnvironment.globals["Company"])
    # print(TemplateEnvironment.globals["Copyright"])


    # Template('Hello {{ name }}!')


    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
