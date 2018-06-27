# 子进程
# 很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。
import subprocess

print('$ nslookup wyoyao.github.com')
r = subprocess.call(['nslookup', 'wyoyao.github.com'])
print(type(r))
print('Exit code:', r)