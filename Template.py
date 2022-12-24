import re


class Template:
    template_text = ""
    globals = {"Company": "Jinja Plus Plus", "Copyright": "\u00a9"}  # global key words

    def render_Old(self, *args, **kwargs):
        # print(args)
        # print(kwargs)
        # print(self.template_text)

        str = "My company name is {{Template.globals[\"Company\"]}}."
        # print(str)

        patternBegin = '{{'
        patternEnd = '}}'

        name = "Jinja"
        address = "Bangalore, BG Road"
        template_text = "My company name is {{name}}! And {{address}} is its address"
        # template_text = "My company name is {{name}}! And address is a great company"

        names = []
        dictNames = {}
        templatizedstring = ""
        while (len(template_text) > 0):
            splits = re.split(patternBegin, template_text)
            if len(splits[0]) != len(template_text):
                variablename = re.split(patternEnd, splits[1])  # splits[1] is the second part of split
                names.append(variablename[0])
                dictNames[variablename[0]] = eval(variablename[0])
                variablevalue = eval(variablename[0])
                part = splits[0] + patternBegin + variablename[0] + patternEnd
                # templatizedstring = templatizedstring + part
                # print("******" + part)
                # remove the matched part and work the remaining string
                template_text = template_text.replace(part, "")
                part = splits[0] + variablevalue
                templatizedstring = templatizedstring + part

            else:
                # print("******" + template_text)
                templatizedstring = templatizedstring + template_text
                break
        # print(names)
        # print(dictNames)
        # print(templatizedstring)
        return


    def removeComments(self):
        patternBegin = '{#'
        patternEnd = '#}'

        template_text = self.template_text

        names = []
        dictNames = {}
        templatizedstring = ""
        while len(template_text) > 0:
            splits = re.split(patternBegin, template_text)
            if len(splits[0]) != len(template_text):
                variablename = re.split(patternEnd, splits[1])  # splits[1] is the second part of split
                # names.append(variablename[0])
                # dictNames[variablename[0]] = kwargs[variablename[0]]
                # variablevalue = kwargs[variablename[0]]
                part = splits[0] + patternBegin + variablename[0] + patternEnd
                # print(part)
                # remove the matched part and work the remaining string
                template_text = template_text.replace(part, "")
                part = splits[0]
                templatizedstring = templatizedstring + part
            else:
                # print(template_text)
                templatizedstring = templatizedstring + template_text
                break
        # print(names)
        # print(dictNames)
        # print("Final templatized")
        # print(templatizedstring)
        self.template_text = templatizedstring
        return


    def render(self, *args, **kwargs):
        # print(args)
        # print(kwargs)
        # print(self.template_text)
        self.removeComments()
        patternBegin = '{{'
        patternEnd = '}}'

        template_text = self.template_text

        names = []
        dictNames = {}
        templatizedstring = ""
        while len(template_text) > 0:
            splits = re.split(patternBegin, template_text)
            if len(splits[0]) != len(template_text):
                variablename = re.split(patternEnd, splits[1])  # splits[1] is the second part of split
                if variablename[0] != "":
                    names.append(variablename[0])
                    # dictNames[variablename[0]] = kwargs[variablename[0]]
                    try:
                        variablevalue = kwargs[variablename[0]]
                    except Exception as e:
                        print("Error: %s" % e)
                        print("Error: template variable is not passed to the function ")
                        variablevalue=""
                    part = splits[0] + patternBegin + variablename[0] + patternEnd
                    # print(part)
                    # remove the matched part and work the remaining string
                    template_text = template_text.replace(part, "")
                    part = splits[0] + variablevalue
                    templatizedstring = templatizedstring + part
                else:
                    part = splits[0] + patternBegin + patternEnd
                    # remove the matched part and work the remaining string
                    template_text = template_text.replace(part, "")
                    part = splits[0]
                    templatizedstring = templatizedstring + part
            else:
                # print(template_text)
                templatizedstring = templatizedstring + template_text
                break
        # print(names)
        # print(dictNames)
        # print("Final templatized")
        # print(templatizedstring)
        self.template_text = templatizedstring
        return

        # while len(template_text) > 0:
        #     splits = re.split(patternBegin, template_text)
        #     if len(splits[0]) != len(template_text):
        #         variablename = re.split(patternEnd, splits[1])  # splits[1] is the second part of split
        #         names.append(variablename[0])
        #         dictNames[variablename[0]] = kwargs[variablename[0]]
        #         variablevalue = kwargs[variablename[0]]
        #         part = splits[0] + patternBegin + variablename[0] + patternEnd
        #         # print(part)
        #         # remove the matched part and work the remaining string
        #         template_text = template_text.replace(part, "")
        #         part = splits[0] + variablevalue
        #         templatizedstring = templatizedstring + part
        #     else:
        #         # print(template_text)
        #         templatizedstring = templatizedstring + template_text
        #         break

