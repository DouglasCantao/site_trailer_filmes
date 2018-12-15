# -*- coding: utf-8 -*-
import webbrowser


class Movie():
    '''Essa classe define o que é necessário para criar objetos do tipo Movie.
    '''

    def __init__(self, title, trailer_youtube_url, storyline,
                 poster_image_url):

        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.storyline = storyline
        self.poster_image_url = poster_image_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    '''
    Adicionar sublinhado no início dos atribútos para ajudar no encapsulamento
     @property
     def title(self):
         return self._title
    '''