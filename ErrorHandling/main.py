# #FileNotFound
#
#
# try:
#     file = open("any_file.txt")
#     a_dictionary = {"key": "value_to_be_printed"}
#     print(a_dictionary["key"])
#
# except FileNotFoundError:
#     print("There was an error")
#     file = open("any_file.txt","w")
#     file.write("Something \n")
#
# except KeyError as error_message:
#     print(f"The key {error_message} doesnt exist in the dictionary")
#
# else:
#     content = file.read()
#     print(content)
#
# finally:
#     file = open("any_file.txt","a")  # "a" is append, "w" is overwrite
#     file.write("Something x2 \n")
#     file.close()
#     print("File was closed.")
#
#     raise: TypeError("This is an example of a created error")
#         #can call error types


######################

#
# height = float(input("Your height: "))
# weight = int(input("Now your weight: "))
#
# if height > 3:
#     raise ValueError(" Humans arent over 3 meters!! ")
#
# bmi = weight / height ** 2
# print(bmi)

#############################
# Facebook posts example, ErrorHandling

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 15, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass

print(total_likes)

###################################