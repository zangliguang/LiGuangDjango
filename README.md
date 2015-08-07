# LiGuangDjango  
黎光 Django项目  
2015/8/7，基本搭建  
1，创建项目：django-admin startproject LiGuangWeb 执行python manage.py runserver测试  
2，创建app：python manage.py startapp liguang_first，在settings INSTALLED_APPS中注册  
3，创建管理员用户 python manage.py createsuperuser 完成后打开http://127.0.0.1:8000/admin/测试  
4，设置DB：settings 文件DATABASES中设置DB信息  
5，添加module文件,
运行python manage.py makemigrations 来为这些修改创建迁移文件
运行pythonmanage.py migrate 以运用这些改变到数据库中（mysql注意刷新）  
在module中定义self方法，查询是可显示自定义内容格式，例如：*
       
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
   >class BusinessInline(admin.TabularInline):  
   >     model = Business  
  >      extra = 3  
  >  class BusinessClassAdmin(admin.ModelAdmin):  
   >     fieldsets = [  
   >        (None,               {'fields': ['businessclass_name']}),  
   >         ('Data order', {'fields': ['businessclass_order'], 'classes': ['collapse']}),  
   >       ]  
   >     inlines = [BusinessInline]  
   >     list_display = ('businessclass_name', 'businessclass_order')  
  
 >   admin.site.register(BusinessClass,BusinessClassAdmin)  

    inlines代表外键关联  
    另外BusinessClassAdmin中可添加  
    排序：list_filter = ['businessclass_order']  
    查找：search_fields = ['business_name']

2015/8/7，设置首页
 1，views 中设置
     >def homePage(req):
         return  HttpResponse("LiGuang HOMEPAGE")
   
   站内跳转:return HttpResponseRedirect("参数");
   站外跳转:return HttpResponseRedirect("http://www.baidu.com/");
     url设置url('^$', homePage),

 2，user 设置，可自定义，也可继承默认的user，例如
        class CustomUser(models.Model):
            user = models.OneToOneField(User)
            //.....other properties
           def __str__(self):
             return self.user.username
    若完全继承默认user，且无其他属性时，应该用默认user，一对一关系很麻烦。
    定义CustomUseradmin，定义所要展示属性的方法，方法中确定所需值，确定列名。
       
    class CustomUserAdmin(admin.ModelAdmin):
       list_display = ['get_firstname','get_lastname']
       def get_firstname(self, obj):
           return obj.user.first_name
       get_firstname.short_description = 'firstname'
       
       def get_lastname(self, obj):
        return obj.user.last_name
      get_lastname.short_description = 'lastname'
  虽然实现了功能，强烈感觉不能这么玩。

