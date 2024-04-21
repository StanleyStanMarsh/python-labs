# TODO Найдите количество книг, которое можно разместить на дискете

floppy_size = 1.44 * 1024 * 1024
num_of_pages = 100
num_of_lines = 50
num_of_chars = 25

num_of_books = int(floppy_size // (4 * num_of_chars * num_of_lines * num_of_pages))

print("Количество книг, помещающихся на дискету:", num_of_books)
