def stories(start, end):
    return [i for i in range(start, (end + 1))]


songs = {
    'op': [
        {
            'title': 'Signalize!',
            'stories': stories(1, 25)
        },
        {
            'title': 'ダイヤモンドハッピー',
            'stories': stories(26, 50)
        },
        {
            'title': 'KIRA☆Power',
            'stories': stories(51, 75)
        },
        {
            'title': 'SHINING LINE*',
            'stories': stories(76, 101)
        },
        {
            'title': 'Du-Du-Wa DO IT!!',
            'stories': stories(102, 126)
        },
        {
            'title': 'Lovely Party Collection',
            'stories': stories(127, 152)
        },
        {
            'title': 'START DASH SENSATION',
            'stories': stories(153, 176) + [178]
        },
    ],
    "ed": [
        {
            'title': 'カレンダーガール',
            'stories': stories(1, 25) + [125]
        },
        {
            'title': 'ヒラリ/ヒトリ/キラリ',
            'stories': stories(26, 43) + stories(45, 50)
        },
        {
            'title': 'アリスブルーのキス',
            'stories': [44]
        },
        {
            'title': 'オリジナルスター☆彡',
            'stories': stories(50, 75)
        },
        {
            'title': 'Precious',
            'stories': stories(76, 101)
        },
        {
            'title': 'Good morning my dream',
            'stories': stories(102, 124) + [126]
        },
        {
            'title': 'チュチュ・バレリーナ',
            'stories': stories(127, 152)
        },
        {
            'title': 'lucky train!',
            'stories': stories(153, 178)
        },
    ]
}
