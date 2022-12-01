from django.shortcuts import render
from django.shortcuts import HttpResponse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .models import Product


def show(request):
    #return HttpResponse("welcame to wallmart.My name is biplob mia.")

    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver.get("https://www.ubereats.com/search?diningMode=DELIVERY&kn=FastFood&pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMk5ldyUyMFlvcmslMjIlMkMlMjJyZWZlcmVuY2UlMjIlM0ElMjJDaElKT3dnXzA2VlB3b2tSWXY1MzRRYVBDOGclMjIlMkMlMjJyZWZlcmVuY2VUeXBlJTIyJTNBJTIyZ29vZ2xlX3BsYWNlcyUyMiUyQyUyMmxhdGl0dWRlJTIyJTNBNDAuNzEzNTIlMkMlMjJsb25naXR1ZGUlMjIlM0EtNzQuMDA2ODg1JTdE&q=Fast%20Food&sc=HOME_FEED_ITEM")

    # total_food = 26*3
    # title_list = []
    # for i in range(1, total_food+1):
    #     x_path = '//*[@id="main-content"]/div/div/div[2]/div/div[2]/div['+str(i)+']/div/a/h3'
    #     print(x_path)
    #     title = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, x_path)))
        
    #     title_list.append(title.text)

    #     print(title_list)
    
    # love = {"title":[title_list], "price":200}
    # titl = "wallmart Product One"
    # product = Product(title =titl)
    # product.save()
    return render(request, 'wallmart/form.html')
def add(request):
    if (request.method == "POST"):
        url = request.POST.get('w_url')
        x1 = request.POST.get('x1')
        x2 = request.POST.get('x2')
        t_count = request.POST.get('t_count')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(url)
        total_food = 15*4
        title_list = []
        # image_list = []
        for i in range(1, total_food+1):
            loop_div = x1+"div["+str(i)+"]"+x2
            print(loop_div)
            x_path =loop_div
            title = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, x_path)))
            title_list.append(title.text)
            product = Product(title =title.text)
            product.save()
        print(title_list)
        return HttpResponse(x2)
    else:
        return HttpResponse("This is not POST METHOD")
        #     image = '//*[@id="maincontent"]/main/div/div[3]/div/div/div/div/div/section/div/div[1]/div/div/div/div[1]/div[2]/div[1]/img'

        # #print(x_path)

        
        #     img = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, x_path)))

        
        # image_list.append(img.get_attribute('src'))

        
        # print(image_list)
        
        #return render(request, 'wallmart/form.html')
    
    #return HttpResponse(title)

# Create your views here.
