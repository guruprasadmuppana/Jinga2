import logging
from Template import Template


class TemplateEnvironment:

    TemplateFolder = "C:/CommunityBuilding/Projects/Jinga2/templates"

    globals = {"Company":"Jinga Plus Plus","Copyright":"\u00a9"} # global key words

    block_start_string = '{%'
    block_end_string = '%}'
    variable_start_string = '{{'
    variable_end_string = '}}'
    comment_start_string = '{#'
    comment_end_string =  '#}'

    def get_template(self,filename):
        file = self.TemplateFolder +"/" + filename
        # print(file)
        filecontent=""
        try:
            with open(file,"r") as f:
                filecontent = f.read()
        except Exception as e:
            print("Error: %s" % e)

        template = Template()
        template.template_text = filecontent
        return template

