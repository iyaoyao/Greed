

##一个Django和Vue.js配置的Demo


####开始
1. 创建Django工程
    
    ```django-admin.py startproject Greed```
    
2. 创建一个app

    ```python manage.py startapp backend```
    
3. 创建一个Vue.js项目
    
    ```vue init webpack Frontend```

###配置

1. settings
    ```
    #vim Greed/settings.py
    
    TEMPLATES[0]["DIRS"].append(os.path.join(BASE_DIR, 'Frontend/dist'))
    
    STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "Frontend/dist/static"),
    ]
        
    
    ```
    
 
###启动

1. cd Frontend
2. npm install
3. npm run build
4. 启动Django程序


    
    
