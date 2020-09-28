import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
from typing import *
from parser.errors import *
import difflib
import config
import re
import logging
from helpers import filters


def _get_html(url: str) -> str:
    logging.info(f'{url[:50]}... requesting ')
    response = requests.get(url, headers=config.HEADERS)
    logging.info(f'{url[:50]}... responded with status {response.status_code}')
    # logging.info(f'{url[:50]}... responded with html {response.text}')
    return response.text


def _generate_soup_from_url(url: str) -> Tag:
    soup: Tag = BeautifulSoup(_get_html(url), features='html.parser')
    logging.info(f'{url[:50]}... generated soup for {soup.name}')
    return soup


def generate_xpath(element: Tag) -> str:
    element_tree_reversed = []

    while True:
        parent: Tag = element.parent
        i = 0
        for child in parent.children:
            if child == element:
                break
            if child.name == element.name:
                i += 1
        element_tree_reversed.append(f'{element.name}[{i}]')

        if element.name == 'html':
            break

        element = parent

    element_tree = reversed(element_tree_reversed)
    return '/%s' % '/'.join(element_tree)


def apply_xpath(url, xpath):
    root_element = _generate_soup_from_url(url)
    for tag in xpath.split('/'):
        if tag == '':
            continue

        child_index: List[Tuple] = re.findall('(.*)\[(.{1,3})]', tag)

        children = list(filter(
            lambda child: child is not None and child.name == tag,
            list(root_element.children)
        ))

        if child_index:
            tag, i = child_index[0]

        if len(children) == 0:
            return None
        elif len(children) == 1:
            root_element = children[0]
        else:
            if child_index:
                root_element = children[int(i)]

    return root_element


def contains_price(tag: Tag, price):
    if tag.name == 'script':
        return False

    if tag.string and tag.string.find(price) != -1:
        return True

    attrs: List[str] = tag.attrs.values()
    logging.info(attrs)
    for attr in attrs:
        if str(attr).find(price) != -1:
            return True

    return False


def find_element(url: str, price: str) -> Tuple[Tag, str]:
    price = filters.filter_price(price)
    logging.info(f'Checking for {price}')
    soup = _generate_soup_from_url(url)
    element: Tag = soup.find(
        lambda tag: contains_price(tag, price)
    )
    if element is None:
        raise ElementNotFound(price)
    return element, generate_xpath(element)


def check_element(url, element, xpath):
    soup = BeautifulSoup(_get_html(url), features='html.parser')
    old_element = apply_xpath(soup, xpath)
    return old_element == element


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    print(
        find_element(
            'https://www.asos.com/ru/asos-design/chernye-suzhennye-knizu-dzhinsy-asos-design/prd/20146594?clr=chernyj&colourwayid=60012430&SearchQuery=&cid=17565',
            '2 590,00 руб'
        )
    )
