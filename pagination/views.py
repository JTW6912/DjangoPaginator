from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.conf import settings
# Create your views here.

def list(request):
    student_data = Student.objects.all()
    return render(request,'list.html',{'student_data':student_data})

def get_page_range(currentPage,totalPage,SIZE=9):

    start = currentPage - int(SIZE/2)
    start = start if start >= 1 else 1
    end = start + SIZE-1
    end = end if end <= totalPage else totalPage
    return range(start,end+1)
def page_list(request):

    page_num = request.GET.get('page')

    student_data = Student.objects.all()

    #创建paginator对象
    paginator = Paginator(student_data,settings.PAGE_SIZE,orphans=settings.OPHANS_PAGE_RANGE)

    #获取paginator对象
    paginator.get_page(request.GET.get('page'))

    #获取page对象
    student_page = paginator.get_page(page_num)

    PageRange = get_page_range(currentPage=student_page.number,totalPage=paginator.num_pages,SIZE = settings.PAGE_RANGE_SIZE)
    return render(request,'page_list.html',{'student_page':student_page,'PageRANGE':PageRange})