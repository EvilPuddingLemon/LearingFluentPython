from concurrent import futures
from PythonTest.S17.flags import save_flag, get_flag, show, main

MAX_WORKERS = 20

def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower()+'.gif')
    return cc

def download_many(cc_list):

    cc_list = cc_list[:5]
    with futures.ThreadPoolExecutor(max_workers=4) as executor:
        to_do = []
        for cc in sorted(cc_list):
            # executor.submit 方法排定可调用对象的执行时间，然后返回一个期物，表示这个待执 行的操作。
            future = executor.submit(download_one, cc)
            to_do.append(future)  # 存储各个期物，后面传给 as_completed 函数
            msg = 'Scheduled for {}: {}'
            print(msg.format(cc, future))

        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)

    return len(results)  # 返回获取的结果数量

if __name__ == '__main__':
    main(download_many)