import random

def get_player_numbers():
    n = int(input("请输入玩家总人数: "))
    good_num = int(input("请输入好人数: "))
    little_num = int(input("请输入小弟数: "))
    bad_num = n - good_num - little_num
    return n, good_num, little_num, bad_num

n, good_num, little_num, bad_num = get_player_numbers()



# 生成序号列表
indexs = list(range(n))

# 生成好人和小弟序号
good_index = random.sample(indexs, good_num)
little_index = random.sample([i for i in indexs if i not in good_index], little_num)

# 生成颠覆者序号
bad_index = set(indexs) - set(good_index) - set(little_index)

# 生成身份列表
good_list = ['战略', '市场', '数分', '产品', '设计', '技术', '测试', '运营', '客服', '公关', 'HR']
bad_list = ['无能的嫡系', '黑话发明家', 'PUA的老板']

# 生成身份字典
dict = {}
for i in indexs:
    if i in good_index:
        dict[i] = random.choice(good_list)
        good_list.remove(dict[i])
    elif i in little_index:
        bad_identity = random.choice(bad_list)
        good_identity = random.choice(good_list)
        dict[i] = f'坏身份: {bad_identity}, 好身份: {good_identity}'
        bad_list.remove(bad_identity)
        good_list.remove(good_identity)
    else:
        good_identity = random.choice(good_list)
        dict[i] = f'坏身份: 颠覆者, 好身份: {good_identity}'
        good_list.remove(good_identity)

# 输出
print('序号', '\t', '身份')
for i, v in dict.items():
    print(i + 1, '\t', v)
