from django.shortcuts import render

def contactlist(request):
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs':blogs})

def contactdetail(request, contact_id):
    contactdetail = get_object_or_404(Contact, pk=contact_id)
    return render(request, 'contact/contactdetail.html', {'contact':contactdetails})
