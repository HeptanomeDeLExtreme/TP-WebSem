#-*- coding: utf-8 -*-
from django.shortcuts import render
import results


def home(request):
        return render(request, 'cactus_search/home.html')

from cactus_search.forms import SearchForm

def search(request):
        # In case of request  POST
        if request.method == 'POST':  
                # We get back the form's data
                form = SearchForm(request.POST)  

                # We verify if the form's data is valid
                if form.is_valid(): 
                        # Here we can work on the form's data
                        keywords = form.cleaned_data['keywords']
                        envoi = True

                        groups = results.getResults(keywords)

                        movies = results.getMovies(keywords)

        # If not POST, it should be GET
        else:
                # We create an empty form
                form = SearchForm()  
                        
                
        return render(request, 'cactus_search/search.html', locals())
