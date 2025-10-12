print('\n >>>>>>>>>>>>>>>>>>>> BMI计算器 >>>>>>>>>>>>>>>>>>')
height = 170
weight = 62
bmi = weight / (height / 100) ** 2 # 优先计算括号内的
print(f'{bmi = :.2f}')
if 18.5 <= bmi < 24:
    print('你的身材很棒！')
elif bmi > 24:
    print('你需要减肥啦！')
else:
    print('你太瘦啦！')


status_code = int(input('响应状态码: '))
match status_code:
    case 400: description = 'Bad Request'
    case 401: description = 'Unauthorized'
    case 403: description = 'Forbidden'
    case 404: description = 'Not Found'
    case 405: description = 'Method Not Allowed'
    case 418: description = 'I am a teapot'
    case 429: description = 'Too many requests'
    case _: description = 'Unknown Status Code'
print('状态码描述:', description)

