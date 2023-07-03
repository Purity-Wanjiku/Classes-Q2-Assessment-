# 1. **Ancestral Stories:** In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that
 # records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think about how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.

# input
# Story, Storyteller, Translator, Language, Moral lesson, Length of the story,Age

 # output
# Should provide the length of the story,lesson and language.

 # process
 # Create classes. Create attributes. Create functions/methods.

class Story:
   def __init__(self,content, length,age_group,moral_lesson,title,language):
       self.title = title
       self.content = content
       self.length=length
       self.age_group = age_group
       self.moral_lesson = moral_lesson
       self.language = language
   def Story_details(self,story_teller):
       return f"{self.title} is {self.length} pages long, told by {story_teller} for people of age{self.age_group} and the moral lesson  is to  teach them on how to {self.moral_lesson}. It is written in {self.language} language"
story1 = Story("The boy who dreamt bigger than the world",300,30,"be a good person","Born a Crime","English")
story2 = Story("Akoko and her sibling who died from eating a fish bone",247,15,"Akoko and her siblings are resilient","River and The Source","Sotho")
print("The Title:",story1.title)
print(story1.Story_details("Marcus"))
class StoryTeller (Story):
   def __init__(self,teller_name,language_stack,title):
       super().__init__(None,None,None,None,title,None)
       self.teller_name = teller_name
       self.language_stack = language_stack
       self.stories=[]
   def Recorded(self,story):
       self.stories.append(story)
       return self.stories
teller1 = StoryTeller("Joy",["English","Rwandese","Burundi","Kiswahili","French"],"Moon")
print ("Storyteller name:",teller1.teller_name)
print(teller1.Recorded(story1.title))
print(teller1.Recorded(story2.title))
class Translator(Story):
   def __init__(self,name,translator_lang,content,title):
       super().__init__(content,None,None,None,title,None)
       self.name = name
       self.translator_lang = translator_lang
   def translate(self):
       return f"{self.name} translated {self.content} to {self.translator_lang}"
translator1 = Translator("William Ambuyi","Kiswahili","The boy who dreamt bigger than the world","Born a crime")
print ("My language is",translator1.translator_lang)
print(translator1.translate())
class Story:
    def __init__(self, length, age_group, moral_lesson, title, language):
        self.title = title
        self.length = length
        self.age_group = age_group
        self.moral_lesson = moral_lesson
        self.language = language
    def display_story(self):
        return f"{self.title} is {self.length} pages long for people of age {self.age_group} and the moral lesson is to teach them on how to {self.moral_lesson}. It is written in {self.language} language"
story1 = Story(300, 30, "be a good person", "Trevor Noah", "English")
print("The Title:", story1.title)
print(story1.display_story())
class StoryTeller(Story):
    def __init__(self,title, teller_name):
        super().__init__(title, None, None, None, None)
        self.teller_name = teller_name
        # self.language_stack = language_stack
        self.books=[]
        # language_stack = []
    def books_written(self):
     return f"{self.books}.append{self.title}"
 
teller1 = StoryTeller(story1.title, "Joy")
print("Story teller name:", teller1.teller_name)
print(teller1.books_written())


class Translator:
    def __init__(self, translator_lang):
        self.translator_lang = translator_lang
translator1 = Translator("Kiswahili")
print("My language is", translator1.translator_lang)


# question2

class Recipe:
 def __init__(self,ingredients, preparation_time,cooking_method,nutritional_info):
     self.ingredients = ingredients
     self.preparation_time = preparation_time
     self.cooking_method = cooking_method
     self.nutritional_info = nutritional_info
class KenyanRecipe(Recipe):
 def __init__(self,recipe_name,serving,ingredients,preparation_time,cooking_method,nutritional_info):
        super().__init__(ingredients,preparation_time,cooking_method,nutritional_info)
        self.recipe_name = recipe_name
        self.serving = serving
 def portions(self,preferred_serving):
    if preferred_serving > self.serving:
        portion_amount = round(preferred_serving / self.serving)
        return f"The portion of ingredients can be increased {portion_amount} times "
    elif preferred_serving < self.serving:
        portion_amount = round(self.serving / preferred_serving)
        return f"The portion of ingredients can be decreased {portion_amount} times"
    else:
        return f"The portion of food serves {self.serving}"
recipe1 = KenyanRecipe("githeri", 6, "beans, nuts and maize", "30 mins", "stew", "well balanced meal")
print(recipe1.portions(6))
class RwandaRecipe(Recipe):
 def __init__(self,recipe_name,ingredients,preparation_time,cooking_method,nutritional_info):
        super().__init__(ingredients, preparation_time,cooking_method,nutritional_info)
        self.recipe_name = recipe_name
 def allergic(self,allergen):
     if allergen in self.ingredients:
        return f"Beware! {allergen} are in {self.recipe_name} dish"
     else:
        return f"Relax! {allergen} is not in {self.recipe_name} dish"
recipe2 = RwandaRecipe("Isombe",["beans","meat","onions"],"30 mins","boil and fry","kills children with no pain")
print(recipe2.allergic("yams"))


# question3

class Species:
    def __init__(self, name, diet, lifespan, month):
        self.name = name
        self.diet = diet
        self.lifespan = lifespan
        self.month = month
    def track(self):
        if self.month<=0:
            return 'Month not available'
        elif self.month<=6:
            migration_pattern = 'South to East'
            return f"{self.name}\n Diet:{self.diet}\n Lifespan:{self.lifespan}\n Prey:{self.prey}\n Migration pattern:{migration_pattern}"
        elif self.month>=6 and self.month<=12:
            migration_pattern = 'North to West'
            return f"{self.name}\n Diet:{self.diet}\n Lifespan:{self.lifespan}\n Migration pattern:{migration_pattern}"
        return 'Month is in the  calendar'
class Predator(Species):
    def __init__(self, name, diet, lifespan, month, prey):
        super().__init__(name, diet, lifespan, month)
        self.prey = prey
    def track_predator(self):
        track = super().track()
        return f"{track}\n Prey:{self.prey}"
class Prey(Species):
    def __init__(self, name, diet, lifespan, month, predator):
        super().__init__(name, diet, lifespan, month)
        self.predator = predator
    def track_prey(self):
        track = super().track()
        return f"{track}\n Predator:{self.predator}"
animal_one = Predator('Lion', 'Herbivores', '30yrs', 13, ['Antelopes', 'Gazelles', 'Zebras'])
print(animal_one.track_predator())
animal_two = Prey('Zebra', 'Grass', '8yrs', 7, ['Cheetah', 'Lion', 'Black Panther'])
print(animal_two.track_prey())

# 4. **African Music Festival:** You're in charge of organising a Pan-African music
# festival. Many artists from different countries, each with their own musical style
# and instruments are scheduled to perform. You need to write a program to
# manage the festivar lineup, schedule, and stage arrangements. Think about how
# you might model the `Artist`, `Performance`, and `Stage` classes, and consider
# how you might use inheritance if there are different types of performances or
# Stages.
class Artist:
  def __init__(self, name, country, specialization):
    self.name = name
    self.country = country
    self.specialization = specialization

class Performance:
  def __init__(self, artist, startTime, endTime):
    self.artist = artist
    self.startTime = startTime
    self.endTime = endTime

class Stage:
  def __init__(self, name, capacity):
    self.name = name
    self.capacity = capacity
    self.performances = []

  def add_performance(self, performance):
    self.performances.append(performance)

  def __str__(self):
    stage_info = f"Stage: {self.name}\nCapacity: {self.capacity}\nPerformances:\n"
    performance_info = "\n".join(f"Artist: {performance.artist.name}, Start Time: {performance.startTime}, End Time: {performance.endTime}" for performance in self.performances)
    return stage_info + performance_info


# 5. Create a class called Product with attributes for name, price, and quantity.
# Implement a method to calculate the total varue of the product (price * quantity).
# Create multiple objects of the Product class and calculate their total varues.
class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_value(self):
        if self.price > 0 and self.quantity > 0:
            return f"The total price is {self.price * self.quantity}$"
        else:
            return f"The total price is invalid"
product = Product("apple",122,2)
print(product.total_value())
product1= Product("mango",0,0)
print(product1.total_value())

# 6. Implement a class called Student with attributes for name, age, and grades (a
# list of integers). Include methods to calculate the average grade, display the
# student information, and determine if the student has passed (average grade >=
# 60). Create objects for the Student class and demonstrate the usage of these
# Methods.

class Student:
   def __init__(self,name,age,grades):
       self.name=name
       self.age=age
       self.grades=grades

   def average_grade(self):
       return sum(self.grades)/len(self.grades)

   def details(self):
       return f'The student is called {self.name} and is {self.age} and scored an {self.grades}'
   def has_passed(self):
       average=self.average_grade()
       return average>=60
   def has_failed(self):
       averages=self.average_grade()
       return averages<=60
student=Student("Diana","24",[25,56,78,80])
student2=Student("Diana","24",[25,96,78,90])
student3=Student("Diana","24",[25,12,8,10])




