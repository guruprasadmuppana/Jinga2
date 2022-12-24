import logging
import unittest
import re

from TemplateEnvironment import TemplateEnvironment


class MyTestCase(unittest.TestCase):

    def test_LoadingPureHTML(self):
        env = TemplateEnvironment()
        try:
            template = env.get_template("HelloWorldTemplate.html")
        except Exception as e:
            print("Error: %s" % e)
        else:
            logging.info("Failed to load template file")

        template.template_text
        htmlstring = """<html>
            <body>
                <h1> Hello World</h1>
            </body>
        </html>"""

        # template.render()

        template.template_text = template.template_text.replace(" ", "")
        htmlstring = htmlstring.replace(" ", "")
        templatelen = len(template.template_text)
        htmlstringlen = len(htmlstring)
        self.assertEqual(templatelen, htmlstringlen,
                         "File Content should match with the hardcoded expected value in Test case ")


    def test_LoadingNullFile(self):
        env = TemplateEnvironment()
        try:
            template = env.get_template("NullFile.html")
        except Exception as e:
            print("Error: %s" % e)
        else:
            logging.info("Failed to load template file")
        template.template_text
        htmlstring = ""
        template.template_text = template.template_text.replace(" ", "")
        htmlstring = htmlstring.replace(" ", "")
        templatelen = len(template.template_text)
        htmlstringlen = len(htmlstring)
        self.assertEqual(templatelen, htmlstringlen,
                         "Null File should not fail")

    def test_LoadingInvalidFile(self):
        env = TemplateEnvironment()
        template = env.get_template("DoesNotExist.html")
        htmlstring = ""
        template.template_text = template.template_text.replace(" ", "")
        htmlstring = htmlstring.replace(" ", "")
        templatelen = len(template.template_text)
        htmlstringlen = len(htmlstring)
        self.assertEqual(templatelen, htmlstringlen,
                         "For invalid file, exceptions should be handled gracefully")

    def test_LoadingPureHTMLWithEmptyVariable(self):
        env = TemplateEnvironment()
        try:
            template = env.get_template("HelloWorldTemplateWithEmptyVariable.html")
        except Exception as e:
            print("Error: %s" % e)
        else:
            logging.info("Failed to load template file")

        template.template_text
        htmlstring = """<html>
            <body>
                <h1> Hello World</h1>
            </body>
        </html>"""
        template.render()
        template.template_text = template.template_text.replace(" ", "")
        htmlstring = htmlstring.replace(" ", "")
        templatelen = len(template.template_text)
        htmlstringlen = len(htmlstring)
        self.assertEqual(templatelen, htmlstringlen,
                         "File Content should match after removing empty placeholder in Test case ")


    def test_LoadingFileWithVariables_kwarg_format_1(self):
        env = TemplateEnvironment()
        template = env.get_template("TemplateWithVariables.html")
        template.render(name="Guru", game="Tennis")
        expectedstring = """<html>
            <body>
                <p> Hello Guru,
                Are you going to play Tennis today?
                </p>
            </body>
        </html>"""

        pattern = "\s"
        matches = re.split(pattern, expectedstring)
        expected_text = ""
        for match in matches:
            expected_text = expected_text + match

        pattern = "\s"
        matches = re.split(pattern, template.template_text)
        processed_text = ""
        for match in matches:
            processed_text = processed_text + match

        templatelen = len(processed_text)
        expectedstringlen = len(expected_text)
        # print(templatelen,expectedstringlen)
        self.assertEqual(templatelen, expectedstringlen,
                         "Variables values did not replace during the processing")

    # TODO: Need to work on this scenario.
    # def test_LoadingFileWithVariables_kwarg_format_2(self):
    #     env = TemplateEnvironment()
    #     template = env.get_template("TemplateWithVariables.html")
    #     template.render({"name":"Guru", "game":"Tennis"})
    #     expectedstring = """<html>
    #         <body>
    #             <p> Hello Guru,
    #             Are you going to play Tennis today?
    #             </p>
    #         </body>
    #     </html>"""
    #
    #     pattern = "\s"
    #     matches = re.split(pattern, expectedstring)
    #     expected_text = ""
    #     for match in matches:
    #         expected_text = expected_text + match
    #
    #     pattern = "\s"
    #     matches = re.split(pattern, template.template_text)
    #     processed_text = ""
    #     for match in matches:
    #         processed_text = processed_text + match
    #
    #     templatelen = len(processed_text)
    #     expectedstringlen = len(expected_text)
    #     # print(templatelen,expectedstringlen)
    #     self.assertEqual(templatelen, expectedstringlen,
    #                      "Variables values did not replace during the processing")

    # invalida scenario. variable names cannot be consider. Only dictionary or Keyword pairs will work
    # def test_LoadingFileWithVariables_kwarg_format_3(self):
    #     env = TemplateEnvironment()
    #     template = env.get_template("TemplateWithVariables.html")
    #     name="Guru"
    #     game="Tennis"
    #     template.render(name,game)
    #     expectedstring = """<html>
    #         <body>
    #             <p> Hello Guru,
    #             Are you going to play Tennis today?
    #             </p>
    #         </body>
    #     </html>"""
    #
    #     pattern = "\s"
    #     matches = re.split(pattern, expectedstring)
    #     expected_text = ""
    #     for match in matches:
    #         expected_text = expected_text + match
    #
    #     pattern = "\s"
    #     matches = re.split(pattern, template.template_text)
    #     processed_text = ""
    #     for match in matches:
    #         processed_text = processed_text + match
    #
    #     templatelen = len(processed_text)
    #     expectedstringlen = len(expected_text)
    #     # print(templatelen,expectedstringlen)
    #     self.assertEqual(templatelen, expectedstringlen,
    #                      "Variables values did not replace during the processing")

    def test_LoadingFileHTMLFileWithComment(self):
        env = TemplateEnvironment()
        template = env.get_template("HelloWorldTemplateWithComments.html")

        expectedstring = """<html>
            <body>
                <h1> Hello World</h1>
            </body>
        </html>"""
        # print(template.template_text)
        # print(expectedstring)

        template.render()
        # expectedstring = """<html>
        #     <body>
        #         <p> Hello Guru,
        #         Are you going to play Tennis today?
        #         </p>
        #     </body>
        # </html>"""

        pattern = "\s"
        matches = re.split(pattern, expectedstring)
        expected_text = ""
        for match in matches:
            expected_text = expected_text + match

        pattern = "\s"
        matches = re.split(pattern, template.template_text)
        processed_text = ""
        for match in matches:
            processed_text = processed_text + match

        templatelen = len(processed_text)
        expectedstringlen = len(expected_text)
        # print(templatelen,expectedstringlen)
        self.assertEqual(templatelen, expectedstringlen,
                         "Variables values did not replace during the processing")


    def test_LoadingFileWithVariablesWithComments_kwarg_format_1(self):
        env = TemplateEnvironment()
        template = env.get_template("TemplateWithVariablesWithComments.html")

        expectedstring = """<html>
            <body>
                <p> Hello Guru,
                Are you going to play Tennis today?
                </p>
            </body>
        </html>"""
        # print(template.template_text)
        # print(expectedstring)

        template.render(name="Guru", game="Tennis")
        pattern = "\s"
        matches = re.split(pattern, expectedstring)
        expected_text = ""
        for match in matches:
            expected_text = expected_text + match

        pattern = "\s"
        matches = re.split(pattern, template.template_text)
        processed_text = ""
        for match in matches:
            processed_text = processed_text + match

        templatelen = len(processed_text)
        expectedstringlen = len(expected_text)

        # print(processed_text)
        # print(expected_text)
        # print(templatelen,expectedstringlen)
        self.assertEqual(templatelen, expectedstringlen,
                         "Variables values did not replace during the processing")


if __name__ == '__main__':
    unittest.main()

# 4. HTML with a tag 1) only once 2) multiple times repeated for the same tags
# 5. HTML with two tags
# 6. HTML with invalid tag 1) only once and 2) multiple times repeated for the same invalid tags
# 7. HTML with multiple invalid tags
# 8. HTML with both valid and invalid tags
# 9. with no content of HTML but only key words

# how to handle Globals at Enviroment level and template level?

# template.render(knights='that say nih')
# template.render({'knights': 'that say nih'})
