'''
# 循环中使用else子句
for item in my_list:
    if item.flavor == 'banana':
        break
else:
    raise ValueError('No banana flavor found!')
'''
'''
# 清晰控制try中只包含可能抛出预期异常的子句
try:         
    dangerous_call()     
except OSError:        
    log('OSError...')     
else:         
    after_call()
'''
