# Practice 1


import variables


def practice_1():
    import requests
    url = "https://en.wikipedia.org/wiki/main_page"
    res = requests.get(url)

    if res:
        print('Response OK')
    else:
        print('Response Failed')

    # print(res.headers["Content-Type"])
    # print(res.text)
    print(res.text.find("Did you know"))


# Practice 2
def practice_2():
    from lxml import etree

    root = etree.XML(variables.data_string)
    print(root.tag, type(root.tag))

    print(etree.tostring(root, pretty_print="True").decode("utf-8"))

    for element in root.iter("Book"):
        print(element.find("Title").text)
