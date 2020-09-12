import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
import re
import pprint

pp = pprint.PrettyPrinter().pprint


def get_xpath(element):
    components = []

    while True:
        parent: Tag = element.parent

        i = 0
        for child in parent.children:
            if child == element:
                break
            if child.name == element.name:
                i += 1
        components.append(f'{element.name}[{i}]')

        if element.name == 'html':
            break
        element = parent

    components.reverse()
    return '/%s' % '/'.join(components)


def get_element(element, xpath):

    for tag in xpath.split('/'):
        if tag == '':
            continue

        iteration = re.findall('(.*)\[(.{1,3})\]', tag)
        if iteration:
            tag, i = iteration[0]

        children = list(filter(
            lambda child: child is not None and child.name == tag,
            list(element.children)
        ))
        if len(children) == 0:
            return None
        elif len(children) == 1:
            element = children[0]
        else:
            element = children[int(i)]

    return element


def get_html(url):
    return requests.get(url).text


def contains_price(tag: Tag, price):
    return all(
        [
            tag.name != 'script',
            any([
                (tag.string is not None and tag.string.find(price) > -1),
                price in tag.attrs.values()
            ])
        ]
    )


def get_element_and_xpath(url, price: str):
    for s in [' ', 'p', 'р', 'r', '₽']:
         price = price.replace(s, '')

    soup = BeautifulSoup(get_html(url), features='html.parser')
    element = soup.find(
        lambda tag: contains_price(tag, price)
    )
    if element is None:
        return None
    return element, get_xpath(element)


def check_element(url, element, xpath):
    soup = BeautifulSoup(get_html(url), features='html.parser')
    old_element = get_element(soup, xpath)
    return old_element == element


if __name__ == '__main__':
    url = 'https://www.velosite.ru/produ%D1%81t/ktm-wild-cross-24-18/2019/'
    print(get_element_and_xpath(url, '36990'))
