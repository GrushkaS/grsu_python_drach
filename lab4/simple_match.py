# Для каждого регулярного выражения, которое требуется написать,
# указаны строки, соответствующие этому выражению (они отмечены знаком +),
# а также строки, не соответствующие этому выражению (отмечены знаком -)

# + a
# + ab
# - b
# - ba
REGEXP_1 = 'a{1,}b{0,}'

# + aab
# + abb
# + acb
# - ab
# - aabc
REGEXP_2 = 'a+[a-c]b+$'

# + sofia.mp3
# + sofia.mp4
# - sofia.mp7
# - sofia.mp34
REGEXP_3 = r'^[a-z]{1,}.mp[3-4]$'

# + taverna
# + versus
# + vera
# + zveri
# - zver
#
REGEXP_4 = '^(zver.+|(?!zver).*)$'

# - a
# - aa
# + aaa
# - aaaa
# - b
# - bb
# + bbb
# - bbbb
# - ccc
REGEXP_5 = '[a-b]{3}$'

# - Ok
# - OkOk
# + OkOkOk
# - OkOkOkOk
# - ab
# - abab
# + ababab
# - abababab
REGEXP_6 = '([a-z][a-z]){3}$|([A-Z][a-z]){3}$'

# - aaa
# - aaa aaa
# + aaa Aaa aaa
# + aaa aaa Aaa
# + Aaa aaa aaa
# - A
# - aaa A aaa
REGEXP_7 = r'(([a-z]|[A-Z]){3}\s*){3}'

# + abc
# + abc03
# + a-b-c-3
# + a.b.c.0
# - Aabc
# - abc1
# - #abc
REGEXP_8 = r'(([a-c][-.]){3}[03])|([a-c]{3}[03]*$)'