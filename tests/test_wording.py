import jieba
import logging
from wording.cut import Cut


def test_cut():
    jieba.setLogLevel(logging.INFO)
    # logging.basicConfig(level=logging.INFO)
    c = Cut()

    test_cases = [
        {
            "cht": {
                "word": [
                    "吋"
                ]
            },
            "eng": {
                "ansh": [],
                "dash": [],
                "hash": [],
                "nash": [
                    "475mm"
                ],
                "num": [
                    "19"
                ],
                "word": [
                    "nwb"
                ]
            },
            "input": "日本nwb 三節式雨刷 19吋/475mm",
            "num_list": [
                "19"
            ],
            "tag_list": [
                "475mm",
                "nwb",
                "三節式",
                "日本",
                "雨刷"
            ]
        },
        {

            "cht": {
                "word": [
                    "跨域",
                    "全",
                    "音域"
                ]
            },
            "eng": {
                "ansh": [
                    "o3"
                ],
                "dash": [],
                "hash": [],
                "nash": [],
                "num": [],
                "word": [
                    "s",
                    "spearx",
                    "t"
                ]
            },
            "input": "【spearx 聲特科技】 spearx 跨域美聲 t+s o3全音域留聲耳機-黑色",
            "num_list": [],
            "tag_list": [
                "o3",
                "s",
                "spearx",
                "t",
                "留聲",
                "科技",
                "美聲",
                "耳機",
                "聲特",
                "黑色"
            ]
        }
    ]

    for test_case in test_cases:
        assert test_case == c.cut(test_case['input'])
