import media
import fresh_tomatoes

freaky_friday = media.Movie("Sexta-Feira Muito Louca",
                            "Comédia",
                            "Inglês",
                            "https://upload.wikimedia.org/wikipedia/pt/thumb/1/1e/Freaky_friday_post.jpg/200px-Freaky_friday_post.jpg",
                            "https://www.youtube.com/watch?v=nZ8KJ4MzzOw",
                            "97",
                            "2003")

o_show_de_truman = media.Movie("O Show de Truman - O Show da Vida",
                         "Drama/Comédia",
                         "Inglês",
                         "https://upload.wikimedia.org/wikipedia/pt/thumb/8/85/TheTrumanShow.jpg/245px-TheTrumanShow.jpg",
                         "https://www.youtube.com/watch?v=loTIzXAS7v4",
                         "103",
                         "1998")

operacao_cupido = media.Movie("Operação Cúpido",
                         "Comédia",
                         "Inglês",
                         "https://upload.wikimedia.org/wikipedia/pt/thumb/b/b2/Cartaz_do_filme_The_Parent_Trap.jpeg/240px-Cartaz_do_filme_The_Parent_Trap.jpeg",
                         "https://www.youtube.com/watch?v=32WeiH4TrIY",
                         "128",
                         "1998")

medianeras = media.Movie("Medianeras: Buenos Aires da Era do Amor Virtual",
                         "Drama",
                         "Espanhol",
                         "https://upload.wikimedia.org/wikipedia/pt/thumb/0/0b/Medianeras.jpg/200px-Medianeras.jpg",
                         "https://www.youtube.com/watch?v=fPc9D5eLLig",
                         "95",
                         "2011")

preso_na_escuridao = media.Movie("Preso na Escuridão",
                          "Drama",
                          "Espanhol",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/a/a6/Abre_los_ojos_movie.jpg/220px-Abre_los_ojos_movie.jpg",
                          "https://www.youtube.com/watch?v=PBtnPuB0x3U",
                          "117",
                          "1997")

titanic = media.Movie("Titanic",
                         "Romance",
                         "Inglês",
                         "https://upload.wikimedia.org/wikipedia/pt/thumb/2/22/Titanic_poster.jpg/250px-Titanic_poster.jpg",
                         "https://www.youtube.com/watch?v=zCy5WQ9S4c0",
                         "194",
                         "1997")


movies = [freaky_friday, o_show_de_truman, operacao_cupido, medianeras, preso_na_escuridao, titanic]

fresh_tomatoes.open_movies_page(movies)