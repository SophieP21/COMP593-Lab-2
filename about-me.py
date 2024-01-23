def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        'full_name': 'Sophie Pierson',
        'student_id': '10325359',
        'pizza_toppings': ['PEPPERONI', 'CHEESE', 'MUSHROOMS'],
        'movie': [
            {'genre': 'scifi', 'title': 'starwars'},
            {'genre': 'action', 'title': 'averngers'}
        ]
    }

    about_me['movie'] = {'genre': 'action', 'title': 'spiderman into the spiderverse'}

    print_student_name_and_id(about_me)
    print_pizza_toppings(about_me)
    add_pizza_toppings(about_me, ('SPINACH', 'TOMATO'))
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)


# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    first_name = about_me['full_name'].split()[0]
    print(f"My name is {about_me['full_name']}, but you can call me The Chosen One {first_name}")
    print(f"My student ID is {about_me['student_id']}")

    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    
  
    about_me['pizza_toppings'].append(toppings)
    about_me['pizza_toppings'].sort()
    about_me['pizza_toppings'].lower()
    
    
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    for topping in about_me['pizza_toppings']:
        print(f"-{topping}")
    
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    genres = [movie['genre'] for movie in about_me['movie']]
    print(", ".join(genres))
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    titles = [movie['title'].title() for movie in movie_list]
    titles_sentence = ", ".join(titles[:-1]) + f", and {titles[-1]}"
    print(f"Some of my favourite movies are {titles_sentence}!")
    return
    
if __name__ == '__main__':
    main()