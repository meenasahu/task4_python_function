def workout_planner(fitness_level,focus_area,time_available):
     print(f'fitness_level={fitness_level}')
     print(f'focus_area ={focus_area }')
     print(f'time_available = {time_available}') 
     
     
     return{
        'fitness-level':fitness_level,
        'focus-area':focus_area,
        'time-available':time_available
        
    }
     
print('---')
gym=('beginner','cardio',10)
print(gym)
print('---')
gym1=('intermidiate','splits',10)
print(gym1)
print('---')


print("============================================================")



def book(book_name,book_author,no_pages):
     print(f'book_name={book_name}')
     print(f'book_author ={book_author}')
     print(f'no_pages = {no_pages}') 
     
     
     return{
        'book-name':book_name,
        'book-author':book_author,
        'no-pages':no_pages
        
    }
     
print('---')
book1=('to_kill_a_mocking_bird','harper_lee',281)
print(book1)
print('---')
book2=('pride_and_prejudice','jane_austen',432)
print(book2)
print('---')
