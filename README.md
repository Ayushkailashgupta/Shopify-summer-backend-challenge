# Shopify-summer-backend-challenge

## Inventory Management Web-App
This is a simple Inventory Management Wep-app where you can perform CRUD(create, read, update, delete) operations. You can aslo import the data and download it as a csv file. The hosted version of the application can be tested and is available at https://shopifyayush.herokuapp.com/ .

Inorder to run the application locally, you need following dependencies installed on your system along with Python version 3.8.8

1. asgiref 3.4.1
2. backports.zoneinfo 0.2.1
3. Django 4.0.1
4. gunicorn 20.1.0
5. sqlparse 0.4.2
6. whitenoise 5.3.0

You can install them via pip install <pacakage_name>.

To run the application you need to execute following commands:

1. python manage.py makemigrations
2. python manage.py migrate
3. python manage.py runserver

After this you will get a url which you can use to access the application.

Here are some of the snap-shots of the application:

1. Home-page:

<img width="1440" alt="Screen Shot 2022-01-16 at 5 44 25 PM" src="https://user-images.githubusercontent.com/91396470/149681446-fd2c0859-3522-434a-a386-1c7beb5a555f.png">

2. Add a product to inventory - here price and quantity have default values and you can change them:

<img width="1440" alt="Screen Shot 2022-01-16 at 5 51 45 PM" src="https://user-images.githubusercontent.com/91396470/149681506-7a2e003f-5204-47db-b55a-81028001f5ae.png">

3. Updating a existing product:

<img width="1413" alt="Screen Shot 2022-01-16 at 5 50 19 PM" src="https://user-images.githubusercontent.com/91396470/149681517-81d7a376-5565-4aac-94e5-49046b076a00.png">

4. And for Deleting a product you just need to click on delete button infront of product.

5. products.csv - screenshot

<img width="1440" alt="Screen Shot 2022-01-16 at 5 58 27 PM" src="https://user-images.githubusercontent.com/91396470/149681657-1141423d-957b-44f5-9b46-dbe093023348.png">

6. Snapshot of code for "Push a button export product data to a CSV"

<img width="820" alt="Screen Shot 2022-01-16 at 6 15 12 PM" src="https://user-images.githubusercontent.com/91396470/149682135-44aa9f71-44ec-4bfb-ba3c-dd826e7b45d4.png">
