from django.shortcuts import render, HttpResponse

from members.models import Members


# Create your views here.
def main(request):
    return render(request, "main.html")


def members(request):
    mymembers = Members.objects.all().values()
    context = {'mymembers': mymembers}
    return render(request, "all_members.html", context)


def details(request, id):
    mymember = Members.objects.get(id=id)
    context = {'mymember': mymember}
    return render(request, "details.html", context)
