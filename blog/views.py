from django.shortcuts import render
from .models import Billet
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# Create your views here.
def post_list(request):
    billets=Billet.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'billets': billets})#request代表接受用户在网上给的东西；第二个参数指明template文件；第三个参数给出template所需要的信息，这些信息有个名字。名字放在冒号前，为字符串

def post_detail(request, pk):
    billet = get_object_or_404(Billet, pk=pk)
    return render(request, 'blog/post_detail.html', {'billet': billet})