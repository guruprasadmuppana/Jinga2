import logging
import unittest
import re

from TemplateEnvironment import TemplateEnvironment


class MyTestCase(unittest.TestCase):


    def test_LoadingPureHTMLWithEmptyVariable(self):
        print("Empty varaible begin")
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
        print("Empty varaible end")

        self.assertEqual(templatelen, htmlstringlen,
                         "File Content should match after removing empty placeholder in Test case ")



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
