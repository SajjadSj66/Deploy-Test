from django.shortcuts import render, HttpResponse

from members.models import Members


# Create your views here.
def main(request):
    return render(request, "main.html")


def members(request):
    mymembers = Members.objects.all()
    context = {'mymembers': mymembers}
    return render(request, "all_members.html", context)


def details(request, slug):
    mymember = Members.objects.get(slug=slug)
    context = {'mymember': mymember}
    return render(request, "details.html", context)
