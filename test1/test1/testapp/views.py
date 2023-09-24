from email import message
from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *

# Create your views here.
def home(request):
    categories = Category.objects.all()
    cars=Product.objects.all()
    context={"cars":cars, "categories":categories}
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subscribe_model_instance = SubscribedUsers()
        subscribe_model_instance.name = name
        subscribe_model_instance.email = email
        subscribe_model_instance.save()

        # messages.success(request, f'{email} email was successfully subscribed to our newsletter!')
        return render(request, 'subscribed.html', context)
    return render(request, 'home.html', context)

def about(request):
    categories = Category.objects.all()
    context={"categories":categories}
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subscribe_model_instance = SubscribedUsers()
        subscribe_model_instance.name = name
        subscribe_model_instance.email = email
        subscribe_model_instance.save()

        # messages.success(request, f'{email} email was successfully subscribed to our newsletter!')
        return render(request, 'subscribed.html', context)
    return render(request, 'about.html', context)

def contact(request):
    categories = Category.objects.all()
    context = {"categories":categories}
    # if request.method == 'POST':
    #     name = request.POST['name']
    #     email = request.POST['email']
    #     subscribe_model_instance = SubscribedUsers()
    #     subscribe_model_instance.name = name
    #     subscribe_model_instance.email = email
    #     subscribe_model_instance.save()

    #     # messages.success(request, f'{email} email was successfully subscribed to our newsletter!')
    #     return redirect(request.META.get("HTTP_REFERER", "/"))
    if request.method=="POST":
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        comment = request.POST['comment']

        Contact(contact_name=firstName, contact_surname=lastName, 
        contact_email=email,contact_comment=comment).save()

        return render(request, 'response.html', context)
    
    return render(request, 'contact.html', context)


def subscribe(request):
    categories = Category.objects.all()
    context = {"categories":categories}
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subscribe_model_instance = SubscribedUsers()
        subscribe_model_instance.name = name
        subscribe_model_instance.email = email
        subscribe_model_instance.save()

        # messages.success(request, f'{email} email was successfully subscribed to our newsletter!')
        return render(request, 'subscribed.html', context)
    
    return render(request, 'home.html', context)

    
def cars_specifications(request, id):
    categories = Category.objects.all()
    carDetail = Product.objects.get(product_id=id)
    context = {"carDetail": carDetail, "categories":categories}
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subscribe_model_instance = SubscribedUsers()
        subscribe_model_instance.name = name
        subscribe_model_instance.email = email
        subscribe_model_instance.save()

        # messages.success(request, f'{email} email was successfully subscribed to our newsletter!')
        return render(request, 'subscribed.html', context)
    return render(request, 'cars_specifications.html', context)

def category_products(request, id):
    categories = Category.objects.all()
    category = Category.objects.get(category_id=id)
    pro_cat = Product.objects.filter(product_category=category)
    context = {"category":category, "categories":categories, "pro_cat":pro_cat}
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subscribe_model_instance = SubscribedUsers()
        subscribe_model_instance.name = name
        subscribe_model_instance.email = email
        subscribe_model_instance.save()

        # messages.success(request, f'{email} email was successfully subscribed to our newsletter!')
        return render(request, 'subscribed.html', context)
    return render(request, 'category_products.html', context)

