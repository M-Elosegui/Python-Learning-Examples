#Password Generator Code
from random import randint, choice, shuffle

def pass_gen():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  pass_letters = [choice(letters) for _ in range(randint(8,10))]
  pass_symbols = [choice(symbols) for _ in range(randint(2,6))]
  pass_numbers = [choice(numbers) for _ in range(randint(2,4))]

  password_list = pass_letters + pass_numbers + pass_symbols
  shuffle(password_list)


  # password = ""
  # for char in password_list:
  #   password += char

  password = "".join(password_list)

  # print(f"Your password is: \n {password}")

  return password


# pass_gen()


