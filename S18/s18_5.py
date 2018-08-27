# 　Python 中的回调地狱：链式回调
'''
def stage1(response1):
    request2 = step1(response1)
    api_call2(request2, stage2)

def stage2(response2):
    request3 = step2(response2)
    api_call3(request3, stage3)

def stage3(response3):
    step3(response3)

api_call1(request1, stage1)
'''

# 做异步编程，无需使用回调
'''
async def three_stages(request1):
    response1 = await api_call1(request1)  
    # 第一步     
    request2 = step1(response1)     
    response2 = await api_call2(request2)     
    # 第二步     
    request3 = step2(response2)     
    response3 = await api_call3(request3)     
    # 第三步     
    step3(response3) 

loop.create_task(three_stages(request1))  # 必须显式调度执行
'''