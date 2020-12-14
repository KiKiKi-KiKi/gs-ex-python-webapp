from urllib.request import urlopen
from bs4 import BeautifulSoup
from pprint import pprint
from re import search, split
from datetime import date as dt
from data.list import songs

TARGET_URL = 'https://ja.wikipedia.org/wiki/%E3%82%A2%E3%82%A4%E3%82%AB%E3%83%84!_(%E3%82%A2%E3%83%8B%E3%83%A1)'

START_YEAR = '2012年'


def format_date(jp_date_str):
    date_array = [int(n) for n in split('[年月日]', jp_date_str) if n]
    # 配列を展開して関数に渡す
    return dt(*date_array)


def froamt_table_row(_year):
    year = _year

    def _format(data):
        # 関数外の変数にアクセスするには nonlocal キーワードが必要
        nonlocal year
        rowData = []
        cells = data.find_all(['td', 'th'])
        last_cell = len(cells) - 1

        for index, cell in enumerate(cells):
            text = cell.get_text()
            if index == 0:
                # 話数を数値化
                m = search(r'\d+', text)
                n = (m and m.group()) or text
                rowData.append(int(n))
            elif index == last_cell:
                #  放送日
                date = text.replace('\n', '')

                # 年の変更があったら year をアップデート
                m = search(r'\d+年', text)
                if m != None:
                    year = m.group()
                else:
                    date = f'{year}{date}'

                rowData.append(format_date(date))
            else:
                rowData.append(text)

        return rowData

    return _format


def merge_op_ed(data):
    op_list = songs.get('op')
    ed_list = songs.get('ed')

    new_data = []

    for d in data:
        n = d[0]
        op_ed = {}
        for op in op_list:
            if n in op['stories']:
                op_ed['op'] = op['title']
                break

        for ed in ed_list:
            if n in ed['stories']:
                op_ed['ed'] = ed['title']
                break

        d.insert(-1, op_ed)
        new_data.append(d)

    return new_data


def get_web_data():
    with urlopen(TARGET_URL) as res:
        html = res.read().decode('utf-8')

    soup = BeautifulSoup(html, 'html.parser')
    tables = soup.select('.NavContent .wikitable')

    data = []
    table_format = froamt_table_row(START_YEAR)
    for t in tables:
        rows = t.select('tr')
        for i, row in enumerate(rows):
            if i == 0:
                continue

            rowData = table_format(row)
            data.append(rowData)

    return merge_op_ed(data)


# get_web_data()
pprint(get_web_data())
