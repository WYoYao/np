print('  dobi'.lstrip())
# 'dobi'
print('db.kun.ac.cn'.lstrip('dkb'))
# '.kun.ac.cn'
print(' dobi   '.rstrip())
# ' dobi'
print('db.kun.ac.cn'.rstrip('acn'))
# 'db.kun.ac.'
print('   dobi   '.strip())
# 'dobi'
print('db.kun.ac.cn'.strip('db.c'))
# 'kun.ac.cn'
print('db.kun.ac.cn'.strip('cbd.un'))
# 'kun.a'
