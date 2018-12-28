# VirtualBank_HIT
哈尔滨工业大学 密码学原理与实践

这个项目是一个网上银行

使用方法

安装django，mysql

然后用mysql建一张叫做“bankdb”的库，只用建库不用建表，然后修改setting.py中DATABASE相关内容

在manage.py所在路径下，输入


    python manage.py makemigrations   

    python manage.py migrate

django会自动生成数据表

最后，启动django服务器


    python manage.py runserver 0.0.0.0:8000
    
    
   
