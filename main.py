Foletterhome = [
  #Title
  "A Letter Home",

  #Prose String
  """
  Hi mom,

  Just writing to tell you that I've quit my job as a OCCUPATION and I'm moving to COUNTRY. The truth is, I've always been passionate about PLURAL_NOUN, and COUNTRY is the best place in the world to build a career around them. I'll need to start small-- At first, all I'll be allowed to do is to VERB near them, but when people see how ADJECTIVE I can be, I'm sure to rise to the top.

  Don't worry about me, and tell dad to take good care of my PERSONAL_ITEM. I'll be sure to call every HOLIDAY.

  Love,

  NAME
  """,

  # Replacements
  [
    ["an occupation", "OCCUPATION"],
    ["a country", "COUNTRY"],
    ["a plural noun", "PLURAL_NOUN"],
    ["a verb", "VERB"],
    ["an adjective", "ADJECTIVE"],
    ["a personal item", "PERSONAL_ITEM"],
    ["a holiday", "HOLIDAY"],
    ["a name", "NAME"]
  ]
]

sale = [
  #Title
  "A Great Sale",

  #Prose String
  """
  SALE SALE SALE

  Today Only : Buy NUMBER PLURAL_NOUN and get a free NOUN!

  Sign up for our exclusive METAL card and receive PERCENTAGE off your first purchase!
  """,

  #Replacements
  [
    ["a number", "NUMBER"],
    ["a plural noun", "PLURAL_NOUN"],
    ["a noun", "NOUN"],
    ["a type of metal, such as silver or copper", "METAL"],
    ["a percentage, including the % symbol", "PERCENTAGE"]
  ]
]

showandtell = [
  #Title
  "Show and Tell",

  #Prose String
  """
  Have you seen my pet ANIMAL? It's the best -- No pet can VERB1 as ADVERB as it can. It's NUMBER years old, and its name is NAME. You can VERB2 it if you want, but becareful, because it might VERB3."
  """,

  #Replacement
  [
    ["an animal", "ANIMAL"],
    ["a verb", "VERB1"],
    ["an adverb", "ADVERB"],
    ["a number", "NUMBER"],
    ["a name", "NAME"],
    ["a transitive verb, such as 'speak to,' 'notice,' or 'touch'", "VERB2"],
    ["a verb", "VERB3"]
  ]
]

stories = [
  letterhome,
  sale,
  showandtell,
]

def show_menu():
  print ("Menu")
  print ("Select your desired story to start the game")
  print ("")

def game():
  show_menu()

  for index, story in enumerate(stories):
    title = story [0]
    print (str(index) + " - " + title)
  
  print ("")
  selection = int(input("Please choose a story by inputting the corresponding number:"))
  print ("")

  story = stories [selection] 
  prosestring = story [1]
  replacement = story[2]

  for prompt, placeholder in replacement:
    prompt = "Please input " + str(prompt) + " : "
    user_input = input(prompt)
    prosestring = prosestring.replace(placeholder, user_input)

  print("")
  print(story[0])
  print(prosestring)
  print("")
  print("Thank you for playing")

game()

play_again = "random"

while play_again !="N":
  print("")
  play_again = str(input("Would you like to play another game? (Y/N) "))

  if play_again == "Y":
    print("")
    game()
  
  elif play_again == "N":
    print ("Thank you for playing!")
    
  else:
    print ("Please input Y or N only")