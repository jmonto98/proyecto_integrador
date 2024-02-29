from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie
import matplotlib.pyplot as plt 
import matplotlib 
import io 
import urllib, base64

# Create your views here.

def home (request):
    #return HttpResponse('<h1>Welcome to my page</h1>')
    #return render(request, 'home.html', {'name':'John Montoya'})
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html',{'searchTerm':searchTerm, 'movies':movies})

def about(request):
    #return HttpResponse('<h1>Welcome to About Page</h1>')
    return render(request, 'about.html')

def statistics_view(request): 
    matplotlib.use('Agg') 
    years = Movie.objects.values_list('year', flat=True).distinct().order_by('year') # Obtener todos los años de las películas 
    movie_counts_by_year = {} # Crear un diccionario para almacenar la cantidad de películas por año 
    for year in years: # Contar la cantidad de películas por año 
        if year: 
            movies_in_year = Movie.objects.filter(year=year) 
        else: 
            movies_in_year = Movie.objects.filter(year__isnull=True) 
            year = "None" 
        
        count = movies_in_year.count() 
        movie_counts_by_year[year] = count
        bar_width = 0.5 # Ancho de las barras 
        bar_spacing = 0.5 # Separación entre las barras 
        bar_positions = range(len(movie_counts_by_year)) # Posiciones de las barras 
        
        # Crear la gráfica de barras 
        plt.bar(bar_positions, movie_counts_by_year.values(), width=bar_width, align='center') 
        # Personalizar la gráfica 
        plt.title('Movies per year') 
        plt.xlabel('Year') 
        plt.ylabel('Number of movies') 
        plt.xticks(bar_positions, movie_counts_by_year.keys(), rotation=90) 
        # Ajustar el espaciado entre las barras 
        plt.subplots_adjust(bottom=0.3) 
        # Guardar la gráfica en un objeto BytesIO 
        buffer = io.BytesIO() 
        plt.savefig(buffer, format='png') 
        buffer.seek(0) 
        plt.close() 
        
        # Convertir la gráfica a base64 
        image_png = buffer.getvalue()
        buffer.close() 
        graphic = base64.b64encode(image_png) 
        graphic = graphic.decode('utf-8')
        
         # Renderizar la plantilla statistics.html con la gráfica 
        return render(request, 'statistics.html', {'graphic': graphic})
    

def statistics_view2(request): 
    matplotlib.use('Agg') 
    # Obtener todas las películas 
    all_movies = Movie.objects.all() 
    
    # Crear un diccionario para almacenar la cantidad de películas por año 
    movie_counts_by_year = {} 
    
    # Filtrar las películas por año y contar la cantidad de películas por año 
    for movie in all_movies: 
        year = movie.year if movie.year else "None" 
        if year in movie_counts_by_year: 
            movie_counts_by_year[year] += 1 
        else: 
            movie_counts_by_year[year] = 1 
        
    # Ancho de las barras 
    bar_width = 0.5 
    # Posiciones de las barras 
    bar_positions = range(len(movie_counts_by_year)) 
    
    # Crear la gráfica de barras 
    plt.bar(bar_positions, movie_counts_by_year.values(), width=bar_width, align='center') 
    
    # Personalizar la gráfica 
    plt.title('Movies per year') 
    plt.xlabel('Year') 
    plt.ylabel('Number of movies') 
    plt.xticks(bar_positions, movie_counts_by_year.keys(), rotation=90) 
    
    # Ajustar el espaciado entre las barras 
    plt.subplots_adjust(bottom=0.3) 
    
    # Guardar la gráfica en un objeto BytesIO
    buffer = io.BytesIO() 
    plt.savefig(buffer, format='png') 
    buffer.seek(0) 
    plt.close() 
    
    # Convertir la gráfica a base64 
    image_png = buffer.getvalue() 
    buffer.close() 
    graphic = base64.b64encode(image_png) 
    graphic = graphic.decode('utf-8') 
    
    # Renderizar la plantilla 
    # statistics.html con la gráfica 
    return render(request, 'statistics.html', {'graphic': graphic})