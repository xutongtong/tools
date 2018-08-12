def get_mobiles(path):
    mobiles = open(path).read().split('\n')

    return mobiles

common_path = '/tools/python/'

paths = []
for i in [1]:
    paths.append(common_path + str(i) + '.new.txt')


mobiles = get_mobiles(common_path + 'origin.new.txt')

diff_mobiles = set()

for path in paths:
    tmp_mobiles = get_mobiles(path)
    diff = set(tmp_mobiles) - set(mobiles)
    diff_mobiles = diff_mobiles | diff

#print mobiles[0]
# print diff_mobiles
# print len(diff_mobiles)
with open("diff.new.txt", 'w') as f:
    f.write(str(list(diff_mobiles)))

with open("sql.txt", 'w') as f:
    sql_mobiles = '\', \''.join(diff_mobiles)
    sql = "insert into `ecs_highfive_order_users` (user_id, mobile) SELECT user_id, mobile_phone from ecs_users where `mobile_phone` in ('{}') ON DUPLICATE KEY UPDATE `updated_at` = now();"
    sql = sql.format(sql_mobiles)
    f.write(sql)


# sql = "INSERT INTO ecs_highfive_order_users (user_id, mobile) VALUES ({$userId}, '{$mobile}'"