from concurrent import futures
from PythonTest.S17.flags import save_flag, get_flag, show, main

MAX_WORKERS = 20

def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower()+'.gif')
    return cc

def download_many(cc_list):
    # 设定工作的线程数量：允许的最大值与要处理的数量之间较小的值
    #workers = min(MAX_WORKERS, len(cc_list))
    #with futures.ThreadPoolExecutor(workers) as executor:
    with futures.ProcessPoolExecutor() as executor:
        # map方法跟内置的map函数类似，把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回
        # 不过会在多个线程中并发调用
        res = executor.map(download_one, sorted(cc_list))

    return len(list(res))  # 返回获取的结果数量

if __name__ == '__main__':
    main(download_many)