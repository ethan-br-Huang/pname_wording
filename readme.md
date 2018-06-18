## Installing
```
git clone https://github.com/ethan-br-Huang/pname_wording.git
cd pname_cut
python setup.py install
```

## Packages
* wording


## Jieba Cut
```
from wording.cut import Cut
c = Cut()
print(c.cut("Faber-Castell 鋼珠筆芯5入", True))
```

```
[Output]
{
  "cht": {
    "word": [
      "入"
    ]
  },
  "eng": {
    "ansh": [],
    "dash": [],
    "hash": [],
    "nash": [],
    "num": [
      "5"
    ],
    "word": [
      "faber-castell"
    ]
  },
  "input": "faber-castell 鋼珠筆芯5入",
  "num_list": [
    "5"
  ],
  "tag_list": [
    "faber-castell",
    "鋼珠筆芯"
  ]
}

```

## Test
```
pytest tests
```