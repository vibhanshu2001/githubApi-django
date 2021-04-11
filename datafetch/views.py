import requests
from django.conf import settings
from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def index(request):
    # apidata = requests.get('https://api.github.com/users/vibhanshu2001').json()
    # myid = apidata['login']
    return render(request, 'datafetch/index.html')
def search(request):
    if request.method == "POST":
        headers = {'Authorization': 'token ' + settings.GITHUB_API_KEY}
        search_params = request.POST['search']
        
        search_url = f'https://api.github.com/users/{search_params}'
        repos_url = f'https://api.github.com/users/{search_params}/repos'
        search_data = requests.get(search_url, headers=headers).json()
        repos_data = requests.get(repos_url, headers=headers).json()
        return render(request, 'datafetch/index.html',{'mydata':search_data,'myrepo':repos_data})
    return render(request, 'datafetch/search.html')