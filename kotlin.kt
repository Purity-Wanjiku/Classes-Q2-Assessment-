fun main() {
    var story1 = Story(
        "The boy who dreamt bigger than the world",
        300,
        30,
        "be a good person",
        "Born a Crime",
        "English"
    )
 
 
    var story2 = Story(
        "Akoko and her sibling who died from eating a fish bone",
        247,
        15,
        "Akoko and her siblings are resilient",
        "River and The Source",
        "Sotho"
    )
 
 
    println("The Title: ${story1.title}")
    println(story1.storyDetails("Marcus"))
 
 
    var teller1 = StoryTeller("Joy", listOf("English", "Rwandese", "Burundi", "Kiswahili", "French"))
 
 
    println("Storyteller name: ${teller1.tellerName}")
    println(teller1.recorded(story1.title))
    println(teller1.recorded(story2.title))
 
 
    var translator = Translator(
        "William nambuyi",
        "Kiswahili",
        "The boy who dreamt bigger than the world",
        "Born a crime",
        "English"
    )
 
 
    println("My language is ${translator.translatorLang}")
    println(translator.translate())

    val recipe = Recipe(
        "Flour, eggs, milk, sugar",
        "15 minutes",
        "Pan frying",
        "Calories: 200 per serving"
    )
    val recipeName = "Pancakes"
    val serving = 4
    val portionsMessage = when {
        serving > 0 -> {
            val preferredServing = 6
            val portionAmount = preferredServing / serving
            "The portion of ingredients can be increased $portionAmount times"
        }
        serving < 0 -> {
            val portionAmount = serving / 6
            "The portion of ingredients can be decreased $portionAmount times"
        }
        else -> {
            "The portion of food serves $serving"
        }
    }

    val nigerianRecipe = NigerianRecipe(
        "Jollof Rice",
        "Rice, tomatoes, onions, peppers, spices",
        "45 minutes",
        "Stovetop cooking",
        "Calories: 300 per serving"
    )
    val allergen = "Peppers"
    val allergicMessage = if (allergen in nigerianRecipe.ingredients) {
        "Beware! $allergen are in ${nigerianRecipe.recipeName} dish"
    } else {
        "Relax! $allergen is not in ${nigerianRecipe.recipeName} dish"
    }

    println("Recipe:")
    println("Ingredients: ${recipe.ingredients}")
    println("Preparation Time: ${recipe.preparationTime}")
    println("Cooking Method: ${recipe.cookingMethod}")
    println("Nutritional Info: ${recipe.nutritionalInfo}")
    println()
    println("Portions:")
    println(portionsMessage)
    println()
    println("Nigerian Recipe:")
    println("Ingredients: ${nigerianRecipe.ingredients}")
    println("Preparation Time: ${nigerianRecipe.preparationTime}")
    println("Cooking Method: ${nigerianRecipe.cookingMethod}")
    println("Nutritional Info: ${nigerianRecipe.nutritionalInfo}")
    println("Allergen Check:")
    println(allergicMessage)
    
    
    



    val animalOne = Predator("Lion", "Herbivores", 30, 13, listOf("Antelopes", "Gazelles", "Zebras"))
    println(animalOne.track())

    val animalTwo = Prey("Zebra", "Grass", 8, 7, listOf("Cheetah", "Lion", "Black Panther"))
    println(animalTwo.track())

 }




// 1. **Ancestral Stories:** In many African cultures, the art of storytelling is passed
// down from generation to generation. Imagine you're creating an application that
// records these oral stories and translates them into different languages. The
// stories vary by length, moral lessons, and the age group they are intended for.
// Think about how you would model `Story`, `StoryTeller`, and `Translator`
// objects, and how inheritance might come into play if there are different types of
// stories or storytellers.

 open class Story(
    var content: String, var length: Int, var ageGroup: Int, var moralLesson: String, var title: String, var language: String
 ) {
    fun storyDetails(storyTeller: String): String {
        return "$title is $length pages long, told by $storyTeller for people of " +
                "age $ageGroup and the moral lesson is to teach them on how to $moralLesson. " +
                "It is written in $language language"
    }
 }
 
 
 class StoryTeller(var tellerName: String, var languageStack: List<String>) {
    var stories = mutableListOf<String>()
 
 
    fun recorded(story: String): List<String> {
        stories.add(story)
        return stories
    }
  fun storyLanguage():String{
  var x =   languageStack.joinToString ( ", " )
    return ("I have written stories in $x languages." )
 }
 }
 
 
 class Translator(
    var name: String, var translatorLang: String, content: String, title: String, language: String
 ) : Story(content, 0, 0, "", title, language) {
 
 
 val recordings = mutableListOf<String>()
 
 
 fun recordingsTranslated():List<String>{
    recordings.add(title)
    return  recordings
 }
 
 
    fun translate(): String {
        return "$name translated '$content' to $translatorLang"
    }
 }
 

//  2. **African Cuisine:** You're creating a recipe app specifically for African cuisine.
// The app needs to handle recipes from different African countries, each with its
// unique ingredients, preparation time, cooking method, and nutritional
// information. Consider creating a `Recipe` class, and think about how you might
// create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
// `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
// Methods.

open class Recipe(
    val ingredients: String,
    val preparationTime: String,
    val cookingMethod: String,
    val nutritionalInfo: String
)

class NigerianRecipe(
    val recipeName: String,
    ingredients: String,
    preparationTime: String,
    cookingMethod: String,
    nutritionalInfo: String
) : Recipe(ingredients, preparationTime, cookingMethod, nutritionalInfo) {
    fun allergic(allergen: String): String {
        return if (allergen in ingredients) {
            "Beware! $allergen is in $recipeName dish"
        } else {
            "Relax! $allergen is not in $recipeName dish"
        }
    }
}




//  3. **Wildlife Preservation:** You're a wildlife conservationist working on a
// program to track different species in a national park. Each species has its own
// characteristics and behaviours, such as its diet, typical lifespan, migration
// patterns, etc. Some species might be predators, others prey. You'll need to
// create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
// These classes might relate to each other through inheritance.

open class Species(val name: String, val diet: String, val lifespan: Int, val month: Int) {
    open fun track(): String {
        return when {
            month <= 0 -> "Month not available"
            month <= 6 -> {
                val migrationPattern = "South to East"
                "$name\nDiet: $diet\nLifespan: $lifespan years\nMigration pattern: $migrationPattern"
            }
            month in 7..12 -> {
                val migrationPattern = "North to West"
                "$name\nDiet: $diet\nLifespan: $lifespan years\nMigration pattern: $migrationPattern"
            }
            else -> "Month is not in the calendar"
        }
    }
}

class Predator(name: String, diet: String, lifespan: Int, month: Int, val prey: List<String>) :
    Species(name, diet, lifespan, month) {
    override fun track(): String {
        val baseTrack = super.track()
        return "$baseTrack\nPrey: $prey"
    }
}

class Prey(name: String, diet: String, lifespan: Int, month: Int, val predator: List<String>) :
    Species(name, diet, lifespan, month) {
    override fun track(): String {
        val baseTrack = super.track()
        return "$baseTrack\nPredator: $predator"
    }
}

   
