# blog_title = "Welcome to my blog"
# posts = [{'title':'iphone 11'},
#              {'title':'iphone 12'},
#              {'title':'iphone 13'},
#              {'title':'iphone 14'},
#              {'title':'iphone 15'},
#              {'title':'iphone 16'},
#              ]

# # for post in posts:
# print(posts[0]['title'])


# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def __str__(self):
#         return f"'{self.title}' by {self.author}"

# my_book = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams")
# print(my_book) # Output: 'The Hitchhiker's Guide to the Galaxy' by Douglas Adams


# for i in range(1, 11):
#     if i % 3 == 0:  
#         continue
#     print(i,end=" ")


def prime(num):
    for i in range(2,int(num**0.5)):
        if num % i == 0:
            return False
        else:
            num = num-1
            return True
        
        
num  = 83
check = True
while  check:
    num = num-1
    check = prime(num)
    
print(num)