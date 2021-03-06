# -*- coding: utf-8 -*-
import webbrowser

import requests
import json


class Movie():
    '''Essa classe define o que é necessário para criar objetos do tipo Movie.
    '''
    # Constantes para armazenar a key e url da api do IMDB.
    api_key = 'b70a215653cf425fcd66f233cd12098e'
    api_url = 'https://api.themoviedb.org/3/movie/%s?api_key=%s'

    # Construtor para inicialização dos atributos dinamicamente.
    def __init__(self, title, trailer_youtube_url, storyline,
                 poster_image_url, movie_id=''):

        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.movie_id = movie_id

    # Método responsável por abrir o trailer na página web.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    '''
    Adicionar sublinhado no início dos atribútos para ajudar no encapsulamento
     @property
     def title(self):
         return self._title
    '''

    # Método responsável por retornar a avaliação do filme conforme IMDB.
    def get_rating(self):

        response = requests.get(self.api_url % (self.movie_id, self.api_key))

        result = json.loads(response.content.decode('utf-8'))

        return result['vote_average']
