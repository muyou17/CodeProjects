names = ['Hieu', 'Hoa', 'Hao', 'Kiem', 'Hieu', 'Hieu', 'Hoa']
name_cnt = dict()
for name in names:
    name_cnt[name] = name_cnt.get(name, 0) + 1
print(name_cnt)