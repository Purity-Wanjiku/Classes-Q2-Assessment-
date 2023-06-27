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

