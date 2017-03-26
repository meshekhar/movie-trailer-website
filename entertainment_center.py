import media
import fresh_tomatoes
import random

toy_story = media.Movie("Toy Story",
                        "Toy Story is a 1995 American computer-animated buddy.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg", 
                        "https://www.youtube.com/watch?v=LKTU4AarZ7A")
                                                
power_rangers = media.Movie("Power Rangers", 
                        "A group of high-school kids, who are infused with unique superpowers, harness their abilities in order to save the world.",
                        "https://upload.wikimedia.org/wikipedia/en/7/78/Power_Rangers_%282017_Official_Theatrical_Poster%29.png", 
                        "https://www.youtube.com/watch?v=5kIe6UZHSXw")

beauty_and_the_beast = media.Movie("Beauty and the Beast", 
                        "Belle (Emma Watson), a bright, beautiful and independent young woman, is taken prisoner by a beast (Dan Stevens) in its castle. ",
                        "https://upload.wikimedia.org/wikipedia/en/d/d6/Beauty_and_the_Beast_2017_poster.jpg", 
                        "https://www.youtube.com/watch?v=omEtQlhhM64")

the_boss_baby = media.Movie("The boss baby", 
                        "A new baby's arrival impacts a family, told from the point of view of a delightfully unreliable narrator -- a wildly imaginative 7-year-old named Tim.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/0/0e/The_Boss_Baby_poster.jpg/220px-The_Boss_Baby_poster.jpg", 
                        "https://www.youtube.com/watch?v=tquIfapGVqs")

the_matrix = media.Movie("The Matrix", 
                        "The Matrix is a 1999 science fiction film written and directed by The Wachowski Brothers, starring Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving, and Joe Pantoliano.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/c/c1/The_Matrix_Poster.jpg/220px-The_Matrix_Poster.jpg", 
                        "https://www.youtube.com/watch?v=cqxwtEdxOCw")

lord_of_the_rings = media.Movie("The Lord of the Rings", 
                        "Journey to Middle-earth via the official The Lord of the Rings website. Get the insider scoop on the latest news, products and new content. Access videos ...",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/e/e9/First_Single_Volume_Edition_of_The_Lord_of_the_Rings.gif/220px-First_Single_Volume_Edition_of_The_Lord_of_the_Rings.gif", 
                        "https://www.youtube.com/watch?v=Pki6jbSbXIY")

movies = [toy_story, power_rangers, beauty_and_the_beast, the_boss_baby, the_matrix, lord_of_the_rings]
random.shuffle(movies)
fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)