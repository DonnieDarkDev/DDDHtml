from DDDHtml import *
test=HTML_Document("Testing title")
test.html_add_child("Testing Body")
test_str=test.html_as_str()
with open('test.html', 'w') as test_html:
    test_html.write(test_str)
print(test_str)