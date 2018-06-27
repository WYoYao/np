from multiprocessing import Process,Pool
import os

# 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...ParentPid %s ' % (name, os.getpid(),os.getppid()))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')


# Pool
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
from multiprocessing import Process,Pool
import time,random

def tiem_task(name):
    print('Run child process %s (%s)...ParentPid %s ' % (name, os.getpid(),os.getppid()))
    start = time.time()
    time.sleep(5)
    end = time.time()
    # print("START TIME: %s , END TIME: %s " % (int(start),int(end)))
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__ =="__main__":
    print('Parent process %s.' % os.getpid())
    p = Pool()
    for i in range(4):
        p.apply_async(tiem_task, args=(i,))
    # print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
