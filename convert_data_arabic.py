import re
import string
import pandas as pd
from hazm import *
import string
import emoji
import hazm
import json
import os
import re


import pandas as pd
import csv
df = pd.read_csv("data_covert_char.csv")

def unifing_alphabets(text):
    text = re.sub(r'ﺍ|ﺁ|ا|اَ|اِ|اُ|اٌ|اٍ|اً|أ|إ|آ', 'ا', text)
    text = re.sub(r'اَ|اِ|اُ|اٌ|اٍ|اً|أ|إ', 'ا', text)
    # text = re.sub(r'ﺄ|ﺄ|أ|ﺃ|أ', 'أ', text)
    text = re.sub(r'ﺎ|ﺎ|ا|ﺍ|ا', 'ا', text)
    text = re.sub(r'ﺂ|ﺂ|آ|ﺁ|آ', 'آ', text)
    text = re.sub(r'ء|ﺀ|ء|ء|ء', 'ء', text)

    text = re.sub(r'ﺏ|بَ|بِ|بُ|بّ|ﺑ|ﺒ|ﺐ', 'ب', text)
    text = re.sub(r'ﭗ|ﭙ|ﭘ|ﭖ|پ|پَ|پِ|پُ', 'پ', text)
    text = re.sub(r'ﺗ|ﺘ|ﺖ|ﺕ|تَ|تِ|تُ|تّ', 'ت', text)
    text = re.sub(r'ثَ|ثِ|ثُ|ث|ﺙ|ﺛ|ﺜ|ﺚ', 'ث', text)

    text = re.sub(r'جَ|جِ|جُ|جّ|ﺝ|ﺟ|ﺠ|ﺞ|ج', 'ج', text)
    text = re.sub(r'چَ|چِ|چُ|چّ|ﭻ|ﭽ|ﭼ|ﭺ|چ', 'چ', text)
    text = re.sub(r'ﺢ|ﺤ|ﺣ|ﺡ|ح|حَ|حِ|حُ', 'ح', text)
    text = re.sub(r'ﺦ|ﺨ|ﺧ|ﺥ|خَ|خِ|خُ', 'خ', text)

    text = re.sub(r'ﺪ|دَ|دِ|دُ|دّ|ﺩ|د', 'د', text)
    text = re.sub(r'ذَ|‌ذِ|ذُ|ﺬ|ﺫ|ذ', 'ذ', text)
    text = re.sub(r'ﺮ|رَ|رِ|رُ|رّ|ﺭ', 'ر', text)
    text = re.sub(r'ﺰ|زَ|زِ|زُ|زّ|ﺯ', 'ز', text)
    text = re.sub(r'ﮋ|ﮊ|ژ|ژَ|ژِ|ژُ', 'ژ', text)

    text = re.sub(r'ﺱ|ﺲ|ﺴ|ﺳ|سَ|سِ|سُ|سّ', 'س', text)
    text = re.sub(r'شَ|شِ|شُ|ﺵ|ﺷ|ﺸ|ﺶ', 'ش', text)

    text = re.sub(r'ﺺ|ﺼ|ﺻ|ﺹ|ص|صَ|صِ|صُ', 'ص', text)
    text = re.sub(r'ضَ|ضِ|ضُ|ض|ﺽ|ﺿ|ﻀ|ﺾ', 'ض', text)
    text = re.sub(r'طَ|طِ|طُ|ط|ﻁ|ﻃ|ﻄ|ﻂ', 'ط', text)
    text = re.sub(r'ﻆ|ﻈ|ﻇ|ﻅ|ظ|ظَ|ظِ|ظُ', 'ظ', text)

    text = re.sub(r'ﻊ|ﻌ|ﻋ|ﻉ|ع|عَ|عِ|عُ', 'ع', text)
    text = re.sub(r'غَ|غِ|غُ|غ|ﻍ|ﻏ|ﻐ|ﻎ', 'غ', text)
    text = re.sub(r'ﻒ|ﻔ|ﻓ|ﻑ|ف|فَ|فِ|فُ|فّ', 'ف', text)
    text = re.sub(r'قَ|قِ|قُ|قّ|ق|ﻕ|ﻗ|ﻘ|ﻖ', 'ق', text)

    text = re.sub(r'ﻙ|ک|کَ|کِ|کُ|ك|كَ|كِ|كُ|کّ|كّ|ﮐ|ﮑ|ﻛ|ﮏ|ﮎ|ﻜ|ڪ|ﻚ|ګ', 'ک', text)
    text = re.sub(r'گَ|گِ|گُ|ﮔ|ﮕ|ﮔ|ﮓ|ﮒ', 'گ', text)


    text = re.sub(r'لَ|لِ|لُ|لّ|ﻞ|ﻠ|ﻟ|ﻝ|ل', 'ل', text)
    text = re.sub(r'م|ﻡ|ﻣ|ﻤ|ﻢ|مَ|مِ|مُ', 'م', text)
    text = re.sub(r'ﻥ|ﻧ|ﻨ|نَ|نِ|نُ|نّ|ﻦ|ن', 'ن', text)


    text = re.sub(r'وَ|وِ|وُ|ؤ|ؤَ|ؤُ|ؤِ|وّ|ؤّ|ﻭ|ﻮ|و', 'و', text)
    text = re.sub(r'هَ|هِ|هُ|ة|ﻩ|ﻫ|ﻬ|ﻪ|ه', 'ه', text)
    text = re.sub(r'ةَ|ﺓ|ةُ|ة|ﺔ', 'ة', text)


    text = re.sub(r'ﻯ|ﻲ|ی|ﯼ|ﯽ|ﻳ|ﯿ|ﯾ|ﻴ|یَ|یِ|یُ|ي|يَ|يِ|يُ|يّ|یّ|ﻱ|ى|ﻰ', 'ی', text)
    text = re.sub(r'ئَ|ئِ|ئُ|ئّ', 'ئ', text)

    return text



sentence_arabic = pd.Series(df['sentence'].astype(str))
# print(sentence_arabic)


lists = sentence_arabic.apply(unifing_alphabets)



# print(lists)

for i in lists:
    print(i)
#
    with open('data_ar_convert_pr.csv', 'a+') as f:
        writer = csv.writer(f)
        writer.writerow([i])
