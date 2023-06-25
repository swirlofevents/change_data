from os.path import dirname, realpath

path = dirname(realpath(__file__))
test_page_filename = "{}/{}".format(path, "test_page.html")

html_data = ""
with open(test_page_filename, encoding="utf8") as file:
    html_data = file.read()
