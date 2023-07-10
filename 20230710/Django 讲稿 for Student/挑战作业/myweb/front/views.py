from django.shortcuts import render

# Create your views here.
'''
    404 错误处理函数
'''
def page_not_found(request, exception):
    return render(request, '404.html')

'''
    500 服务器内部异常处理函数
'''
def server_error(request):
    return render(request, '500.html')
