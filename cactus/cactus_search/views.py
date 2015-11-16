#-*- coding: utf-8 -*-
from django.shortcuts import render

def home(request):
        return render(request, 'cactus_search/home.html')

from cactus_search.forms import SearchForm

def search(request):
        # S'il s'agit d'une requête POST
        if request.method == 'POST':  
                # Nous reprenons les données
                form = SearchForm(request.POST)  

                # Nous vérifions que les données envoyées sont valides
                if form.is_valid(): 
                        # Ici nous pouvons traiter les données du formulaire
                        keyword = form.cleaned_data['keyword']
                        envoi = True

        # Si ce n'est pas du POST, c'est probablement une requête GET
        else:
                # Nous créons un formulaire vide
                form = SearchForm()  
                        
                
        return render(request, 'cactus_search/search.html', locals())
