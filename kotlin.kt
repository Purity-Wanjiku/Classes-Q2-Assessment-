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

    val recipe1 = MoroccanRecipe("githeri", 6, "beans, nuts and maize", "30 mins", "stew", "well balanced meal")
    println(recipe 1.portions(6))
 
 
    val recipe2 = NigerianRecipe("Isombe", "beans, meat, onions", "30 mins", "boil and fry", "kills children with no pain")
    println(recipe2.allergic("yams"))
    
    val animals1 = Species("buffalo", "flesh", 45, "Run")
    val animals2 = Species("buffalo", "grass", 15, "Run")
    println(animals1.checkSpecies("Carnivore", "Herbivore"))
    println(animals2.checkSpecies("Carnivore", "Herbivore"))

    open class Predator(
        name: String,
        val appearance: String,
        diet: String,
        lifeSpan: Int
    ) : Species(name, diet, lifeSpan, "") {
        val predators = mutableListOf<String>()
        fun namingPredators(): List<String> {
            predators.add(name)
            return predators
        }
    }

    val predator1 = object : Predator("Antelope", "slimy", "meat", 12) {}
    val predator2 = object : Predator("Buffalo", "slimy", "meat", 12) {}
    println(predator1.namingPredators())
    println(predator2.namingPredators())

    open class Prey(
        specieName: String,
        diet: String,
        val defenseMechanism: String,
        lifeSpan: Int,
        migrationPatterns: String
    ) : Species(specieName, diet, lifeSpan, migrationPatterns)


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
 
 
 class Recipe(
        val recipeName: String,
        val serving: Int,
        ingredients: String,
        preparationTime: String,
        cookingMethod: String,
        nutritionalInfo: String
 ) : Recipe(ingredients, preparationTime, cookingMethod, nutritionalInfo) {
    fun portions(preferredServing: Int): String {
        return when {
            preferredServing > serving -> {
                val portionAmount = (preferredServing / serving)
                "The portion of ingredients can be increased $portionAmount times"
            }
                    preferredServing < serving -> {
                val portionAmount = (serving / preferredServing)
                "The portion of ingredients can be decreased $portionAmount times"
            }
            else ->{
                "The portion of food serves $serving"
            }
 
 
        }
    }
 }
 
 class NigerianRecipe(
        val recipeName: String,
        ingredients: String,
        preparationTime: String,
        cookingMethod: String,
        nutritionalInfo: String
 ) : Recipe(ingredients, preparationTime, cookingMethod, nutritionalInfo) {
    fun allergic(allergen: String): String {
        return if (allergen in ingredients) {
            "Beware! $allergen are in $recipeName dish"
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


open class Species(
    val name: String,
    val diet: String,
    val lifeSpan: Int,
    val migrationPatterns: String
) {
    val species = mutableListOf<String>()
    fun checkSpecies(specieA: String, specieB: String): List<String> {
        if (diet == "flesh" && lifeSpan >= 30) {
            species.add(specieA)
            println("$specieA is a carnivore with a lifespan of at least 30 years.")
        } else if (diet == "grass" && lifeSpan < 30) {
            species.add(specieB)
            println("$specieB is a herbivore with a lifespan of less than 30 years.")
        }
        return species
    }
}


   