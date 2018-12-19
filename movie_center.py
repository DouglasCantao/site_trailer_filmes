# -*- coding: utf-8 -*-
from media import Movie
import fresh_tomatoes


'''
Este módulo é responsável pela instanciação dos objetos Movie,
chamada do serviço fresh_tomatoes e execução.'''

final_fantasy = Movie('Final Fantasy',
                      'https://www.youtube.com/watch?v=wut2am39z-c',
                      'Continuando a história baseada no jogo de sucesso de ' +
                      'PlayStation Final Fantasy VII...',
                      'https://bit.ly/2Eu0WJM',
                      'tt0385700')


django = Movie('Django Unchained',
               'https://www.youtube.com/watch?v=_iH0UBYDI4g',
               'É um filme de aventura e faroeste estadunidense de 2012 ' +
               'escrito e dirigido por Quentin Tarantino...',
               'https://bit.ly/2PuUuDn',
               'tt1853728')


inception = Movie('Inception',
                  'https://www.youtube.com/watch?v=2wd_FjobppI',
                  'Don Cobb é um ladrão que invade os sonhos das pessoas e' +
                  'rouba segredos do subconsciente. As habilidades ' +
                  'especiais de Cobb fazem com que ele seja procurado ' +
                  'pelo mundo...',
                  'https://bit.ly/2C93RVC',
                  'tt1375666')

# Criação da lista de objetos Movie para ser utilizado
# como parâmetro no método open_movie_page
movies = [django, final_fantasy, inception]

# Execução do serviço responsável por gerar a webpage
# com os filmes passados no parâmetro.
fresh_tomatoes.open_movies_page(movies)
