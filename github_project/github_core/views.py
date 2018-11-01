from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import filters
import requests
import json
from github_core.pagination import CustomPagination

# Create your views here.
class GithubtesteViewSet(viewsets.ViewSet):
    def list(self, request):
        search = request.GET.get('search', None)
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 10))
        limit = 30 if limit > 30 else limit
        if search:
            url = 'https://api.github.com/users/%s' % search
        else:
            url = 'https://api.github.com/users?since={0}'.format(((page - 1) * limit) + 1)
       
        response = requests.get(url)
        user_list = response.json()

        next_page = page + 1
        previous_page = page - 1 if page > 1 else 0
        scheme = request._request.scheme
        host = request._request.get_host()
        path = request._request.get_full_path().split('?')[0]
        return Response({
            'next': f'{scheme}://{host}{path}?page={next_page}&limit={limit}',
            'previous': f'{scheme}://{host}{path}?page={previous_page}&limit={limit}' if previous_page else None,
            'count': None,
            'limit': limit,
            'results': user_list
        })

class GithubrepositoriosViewSet(viewsets.ViewSet):
        # filter_backends = (filters.SearchFilter,)
        # search_fields = ('username')
    def list(self, request):
        search = request.GET.get('search', None)
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 10))
        limit = 30 if limit > 30 else limit
        search = request.GET.get('search', None)
        if search:
            url = 'https://api.github.com/users/%s/repos' % search
           # https://api.github.com/users/giovannamascarenhas/repos
        else:
            url = 'https://api.github.com/users/repos{0}'.format(((page - 1) * limit) + 1)
        #repos = {}
        url = 'https://api.github.com/users/%s/repos' 
        response = requests.get(url)
        repos_list = response.json()

        next_page = page + 1
        previous_page = page - 1 if page > 1 else 0
        scheme = request._request.scheme
        host = request._request.get_host()
        path = request._request.get_full_path().split('?')[0]
        return Response({
            'next': f'{scheme}://{host}{path}?page={next_page}&limit={limit}',
            'previous': f'{scheme}://{host}{path}?page={previous_page}&limit={limit}' if previous_page else None,
            'count': None,
            'limit': limit,
            'results': repos_list
        })
