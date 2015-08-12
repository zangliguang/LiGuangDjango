# LiGuangDjango
黎光 Django项目

2015/8/7，基本搭建
-------------

1，创建项目：django-admin startproject LiGuangWeb 执行python manage.py runserver测试
2，创建app：python manage.py startapp liguang_first，在settings INSTALLED_APPS中注册
3，创建管理员用户 python manage.py createsuperuser 完成后打开http://127.0.0.1:8000/admin/测试
4，设置DB：settings 文件DATABASES中设置DB信息
5，添加module文件，运行python manage.py makemigrations 来为这些修改创建迁移文件
                  运行python manage.py migrate 以运用这些改变到数据库中（mysql注意刷新）
   在module中定义self方法，查询是可显示自定义内容格式，例如：
       def __str__(self):
         return self.businessclass_name
6，进入django shell  python manage.py shell或python+import django+django.setup()
   在shell中可对db操所，例如：

    from liguang_first.models import BusinessClass
    bc=BusinessClass(businessclass_name="test_bc")
    bc.order=-1
    bc.save()
    BusinessClass.objects.all()
    [<BusinessClass: test_bc>]
7，admin 文件中注册modules admin.site.register(BusinessClass)，即可展示User列表
8,自定义表单显示，注册modules时，定义module admin类，注册时作为第二个参数传入。例如：
    class BusinessInline(admin.TabularInline):
        model = Business
        extra = 3
    class BusinessClassAdmin(admin.ModelAdmin):
        fieldsets = [
            (None,               {'fields': ['businessclass_name']}),
            ('Data order', {'fields': ['businessclass_order'], 'classes': ['collapse']}),
        ]
        inlines = [BusinessInline]
        list_display = ('businessclass_name', 'businessclass_order')

    admin.site.register(BusinessClass,BusinessClassAdmin)

    inlines代表外键关联

    另外BusinessClassAdmin中可添加
    排序：list_filter = ['businessclass_order']
    查找：search_fields = ['business_name']

2015/8/10，businessclass 列表查询
----------------------------

url中定义
url(r'^bclist/', views.bclist)

    url(r'^bclist/', views.bclist),
   
views 中定义

    def bclist(request):
    BusinessClasslist = BusinessClass.objects.all()
    return render(request, 'liguang_first/bc_list_view.html',
                  {'BusinessClasslist': BusinessClasslist})
              
项目文件中定义templates文件夹，templates中再次定义liguang_first文件夹，其内定义html文件，可直接用路径 

    liguang_first/bc_list_view.html
html 文件定义

    {% if BusinessClasslist %}
    <ul>
    {% for bc in BusinessClasslist %}
        <li><a href="/liguang_first/businessclass/{{ bc.id }}/">{{ bc.businessclass_name }}</a></li>
    {% endfor %}
    </ul>
      {% else %}
    <p>businessclass are available.</p>
     {% endif %}
下来应该看看form继承使用，default admin的增删改查

## 2015/8/12 一个小的登录注册 ##
仿照网上写的，还需细改，具体看代码。


