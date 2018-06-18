# -*- coding: UTF-8 -*-
from collections import defaultdict
import jieba
import json
import logging
import os
import regex


class Cut:
    def __init__(self):
        jieba.initialize()
        cht_tag_path = 'dict/cht_tag.tsv'
        self.cht_tags = defaultdict(str)

        if os.path.exists(cht_tag_path):
            with open(cht_tag_path, 'r') as f:
                for l in f.readlines():
                    tag = l.strip().split('\t')[0]
                    self.cht_tags[(tag)] = 1
                    jieba.add_word(tag)
            logging.info('[Cut] cht dict loaded.')
        else:
            logging.info('[Cut] cht dict not found.')

    def cut(self, input_str, pretty_json=False):
        input_str = (input_str.lower().strip())
        not_cht = re.sub('[^a-zA-Z0-9-.]', ' ', input_str)

        eng_list = [i for i in not_cht.split(' ') if i]
        eng_list = [i.strip('-') for i in eng_list if i.strip('-')]

        seed_p1 = [w for w in eng_list if re.match(
            '^(?=.*[0-9])(?=.*[a-z])([a-z0-9-]+)$', w)]
        seed_p2 = [w for w in eng_list if '-' in w]
        seed_p3 = [w for w in eng_list if re.match('^[a-z]+-[a-z]+$', w)]
        seed_list = sorted(set(seed_p1 + seed_p2) - set(seed_p3))
        seed_list = [s.strip('.') for s in seed_list if s.replace('-', '')]

        eng_dict = defaultdict(list)
        for s in seed_list:
            if re.match('^[0-9]+[a-z\-]+[0-9]+$', s):
                eng_dict['nash'].append(s)
            elif '-' in s:
                eng_dict['dash'].append(s)
            elif re.match('^[0-9\.]+[a-z]+$', s):
                eng_dict['nash'].append(s)
            elif re.match('^[a-z]+[0-9]+$', s):
                eng_dict['ansh'].append(s)
            else:
                eng_dict['hash'].append(s)

        for s in eng_list:
            if re.match('^[0-9\.]+$', s):
                eng_dict['num'].append(s)
        seed_list += eng_dict['num']

        eng_dict['word'] = sorted(
            set([w for w in eng_list if w not in seed_list]))

        cht = re.sub('[^\u4E00-\u9FFF]', ' ', input_str)
        cht_list = jieba.lcut(cht, cut_all=False)
        cht_list = [i.strip() for i in cht_list if i.strip()]
        cht_list = [i.strip('-') for i in cht_list if i.strip('-')]

        cht_dict = defaultdict(list)

        if self.cht_tags:
            cht_dict['tag'] = [w for w in cht_list if (w) in self.cht_tags]
            cht_dict['word'] = [
                w for w in cht_list if (w) not in self.cht_tags]

        tag_list = cht_dict['tag'] + eng_dict['word'] + eng_dict['dash'] + \
            eng_dict['hash'] + eng_dict['nash'] + eng_dict['ansh']
        tag_list = sorted(set(tag_list))
        result_d = {"input": input_str, "eng": eng_dict, "tag_list": tag_list,
                    "num_list": eng_dict['num'], "cht": {"word": cht_dict['word']}}
        if pretty_json:
            return json.dumps(result_d, sort_keys=True, indent=4, separators=(',', ': '))
        else:
            return result_d


if __name__ == "__main__":
    pass
