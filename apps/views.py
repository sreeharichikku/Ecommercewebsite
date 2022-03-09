from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from products import products

from .forms import NewUserForm, formcontact

# Create your views here.
# from .models import Products
from .models import Productss, cart


def home(request):
    return render(request, 'home.html')


def register_request(request):
    if request.method == "POST":

        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm
    return render(request=request, template_name="signup.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="signin.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")


def contact(request):
    if request.method == 'POST':
        form = formcontact(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("home")
            except:
                pass
    else:
        form = formcontact()
        return render(request, 'contact.html', {'form': form})


def shopnow(request):
    products = Productss.objects.all()

    data = {
        'products': products
    }
    return render(request, 'products.html', data)


def add_to_cart(request):
    context = {}
    items = cart.objects.filter(user_id=request.user.id, status=False)
    context["items"] = items

    if request.user.is_authenticated:
        if request.method == "POST":
            pid = request.POST["pid"]
            qty = request.POST["qty"]
            is_exist = cart.objects.filter(product_id=pid, user_id=request.user.id, status=False)
            if len(is_exist) > 0:
                context["msz"] = "Item Already Exists in Your Cart"
                context["cls"] = "alert alert-warning"
            else:
                product = get_object_or_404(Productss, id=pid)
                usr = get_object_or_404(User, id=request.user.id)
                c = cart(user=usr, product=product, quantity=qty)
                c.save()
                context["msz"] = "{} Added in Your Cart".format(product.name)
                context["cls"] = "alert alert-success"
    else:
        context["status"] = "Please Login First to View Your Cart"
    return render(request, "cart.html", context)


def delete(request, id):
    items = cart.objects.get(id=id)
    items.delete()
    return redirect('cart')


def get_cart_data(request):
    items = cart.objects.filter(user__id=request.user.id, status=False)
    sale,total,quantity = 0 , 0 , 0
    for i in items:
        sale += float(i.product.sale_price)*i.quantity
        total += float(i.product.price)*i.quantitys
        quantity += int(i.quantity)

        res = {
            "total": total, "offer": sale, "quan": quantity,
        }
        return render(request,'cart.html', res)


def change_quan(request):
    if "quantity" in request.GET:
        cid = request.GET["cid"]
        qty = request.GET["quantity"]
        cart_obj = get_object_or_404(cart,id=cid)
        cart_obj.quantity = qty
        cart_obj.save()
    return HttpResponse(cart_obj.quantity)


