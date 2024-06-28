from django.shortcuts import render


def homepage(request):

    return render(request,"books/index.html")

def searchpage(request):
    return render(request,"books/searchpage.html")

def user_profile(request):
    if request.user.is_authenticated:
        # Fetch user details
        user_details = {
            'fname':request.user.first_name,
            'email': request.user.email,
            'full_name': request.user.get_full_name(),  # Assumes you have first_name and last_name fields
            'username': request.user.username,
        }
    # Pass the user details to the template in the context dictionary
    context = {'user_details': user_details}
    return render(request,"books/profile.html",context)