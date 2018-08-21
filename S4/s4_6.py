s1 = 'café'
s2 = 'cafe\u0301'
print(s1, s2)
print(len(s1), len(s2))
print(s1 == s2)

from unicodedata import normalize, name
print(len(normalize('NFC', s1)), len(normalize('NFC', s2)))
print(len(normalize('NFD', s1)), len(normalize('NFD', s2)))

print(normalize('NFC', s1) == normalize('NFC', s2))
print(normalize('NFD', s1) == normalize('NFD', s2))

ohm = '\u2126'
print(ohm)
print(name(ohm))
ohm_c = normalize('NFC', ohm)
print(ohm_c)
print(name(ohm_c))
print(ohm == ohm_c)
print(normalize('NFC', ohm) == normalize('NFC', ohm_c))

half = '½'
print(normalize('NFKC', half))
four_squared = '4²'
print(normalize('NFKC', four_squared))
micro = 'µ'
micro_kc = normalize('NFKC', micro)
print(micro, micro_kc)
print(ord(micro), ord(micro_kc))
print(name(micro), name(micro_kc))

# 将所有文本变成小写
micro_cf = micro.casefold()
print(name(micro_cf))
print(micro, micro_cf)
eszett = 'ß'
print(name(eszett))
eszett_cf = eszett.casefold()
print(eszett, eszett_cf)


# 比较规范化Unicode字符串
def nfc_equal(str1, str2):
    return normalize('NFC', str1) == normalize('NFC', str2)

def fold_equal(str1, str2):
    return (normalize('NFC', str1).casefold() ==
            normalize('NFC', str2).casefold())

s1 = 'café'
s2 = 'cafe\u0301'
print(s1 == s2)
print(nfc_equal(s1, s2))
print(nfc_equal('A', 'a'))

s3 = 'Straße'
s4 = 'strasse'
print(s3 == s4)
print(nfc_equal(s3, s4))
print(fold_equal(s3, s4))
print(fold_equal(s1, s2))
print(fold_equal('S', 's'))

# 去掉全部组合符号
import unicodedata
import string

def shave_marks(txt):
    norm_txt = unicodedata.normalize('NFD', txt)
    shaved = ''.join(c for c in  norm_txt
                     if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)

order = '“Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”'
print(shave_marks(order))
Greek = 'Zέφupoς, Zéfiro'
print(shave_marks(Greek))

def shave_marks_latin(txt):
    """把拉丁基字符中所有的变音符号删除"""
    norm_txt = unicodedata.normalize('NFD', txt)
    latin_base = False
    keepers = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base:
            continue
            # 忽略拉丁基字符上的变音符号
        keepers.append(c)
        # 如果不是组合字符，那就是新的基字符
        if not unicodedata.combining(c):
            latin_base = c in string.ascii_letters
    shaved = ''.join(keepers)
    return unicodedata.normalize('NFC', shaved)

print(shave_marks_latin(order))
print(shave_marks(Greek))

#  把一些西文印刷字符转换成ASCII 字符

print(len(""",ƒ;†ˆ‹‘’“”•––˜›"""))
print(len("""'f"*^<''""---~>"""))
single_map = str.maketrans(""",ƒ;†ˆ‹‘’“”•––˜›""", """'f"*^<''""---~>""")
multi_map = str.maketrans({
    '€': '<euro>',
    '…': '...',
    'Œ': 'OE',
    '™': '(TM)',
    'œ': 'oe',
    '‰': '<per mille>',
    '‡': '**',
})

multi_map.update(single_map)

def dewinize(txt):
    """把Win1252符号替换成ASCII字符或序列"""
    return txt.translate(multi_map)

def asciize(txt):
    no_marks = shave_marks_latin(dewinize(txt))
    no_marks = no_marks.replace('ß', 'ss')
    return unicodedata.normalize('NFKC', no_marks)

print(dewinize(order))
print(asciize(order))




