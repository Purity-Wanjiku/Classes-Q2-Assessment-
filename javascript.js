// # 1. **Ancestral Stories:** In many African cultures, the art of storytelling is passed
// # down from generation to generation. Imagine you're creating an application that
// # records these oral stories and translates them into different languages. The
// # stories vary by length, moral lessons, and the age group they are intended for.
// # Think about how you would model `Story`, `StoryTeller`, and `Translator`
// # objects, and how inheritance might come into play if there are different types of
// # stories or storytellers.

// # input
// # Story, Storyteller, Translator, Language, Moral lesson, Length of the story,Age

// # output
// # Should provide the length of the story,lesson and language.

// # process
// # Create classes. Create attributes. Create functions/methods.

class Story {
    constructor(content, length, age_group, moral_lesson, title, language) {
      this.title = title;
      this.content = content;
      this.length = length;
      this.age_group = age_group;
      this.moral_lesson = moral_lesson;
      this.language = language;
    }
     story_details(story_teller) {
      return `${this.title} is ${this.length} pages long, told by ${story_teller} for people of age ${this.age_group} and the moral lesson is to teach them on how to ${this.moral_lesson}. It is written in ${this.language} language`;
    }
  }
   let story1 = new Story(
    "The boy who dreamt bigger than the world",
    300,
    30,
    "be a good person",
    "Born a Crime",
    "English"
  );
  let story2 = new Story(
    "Akoko and her sibling who died from eating a fish bone",
    247,
    15,
    "Akoko and her siblings are resilient",
    "River and The Source",
    "Sotho"
  );
   console.log("The Title:", story1.title);
  console.log(story1.story_details("Marcus"));
   class StoryTeller {
    constructor(teller_name, language_stack) {
      this.teller_name = teller_name;
      this.language_stack = language_stack;
      this.stories = [];
    }
     recorded(story) {
      this.stories.push(story);
      return this.stories;
    }
  }
   let teller1 = new StoryTeller("Joy", [
    "English",
    "Rwandese",
    "Burundi",
    "Kiswahili",
    "French",
  ]);
   console.log("Storyteller name:", teller1.teller_name);
  console.log(teller1.recorded(story1.title));
  console.log(teller1.recorded(story2.title));
   class Translator extends Story {
    constructor(name, translator_lang, content, title, language) {
      super(content, null, null, null, title, language);
      this.name = name;
      this.translator_lang = translator_lang;
    }
     translate() {
      return `${this.name} translated '${this.content}' to ${this.translator_lang}`;
    }
  }
   let translator = new Translator(
    "William Ambuyi",
    "Kiswahili",
    "The boy who dreamt bigger than the world",
    "Born a crime",
    "English"
  );
   console.log("My language is", translator.translator_lang);
console.log(translator.translate());
  

// Question2

class Recipe {
  constructor(ingredients, preparationTime, cookingMethod, nutritionalInfo) {
      this.ingredients = ingredients;
      this.preparationTime = preparationTime;
      this.cookingMethod = cookingMethod;
      this.nutritionalInfo = nutritionalInfo;
  }
}

class KenyanRecipe extends Recipe {
  constructor(recipeName, serving, ingredients, preparationTime, cookingMethod, nutritionalInfo) {
      super(ingredients, preparationTime, cookingMethod, nutritionalInfo);
      this.recipeName = recipeName;
      this.serving = serving;
  }

  portions(preferredServing) {
      if (preferredServing > this.serving) {
          const portionAmount = Math.round(preferredServing / this.serving);
          return `The portion of ingredients can be increased ${portionAmount} times`;
      } else if (preferredServing < this.serving) {
          const portionAmount = Math.round(this.serving / preferredServing);
          return `The portion of ingredients can be decreased ${portionAmount} times`;
      } else {
          return `The portion of food serves ${this.serving}`;
      }
  }
}

class RwandaRecipe extends Recipe {
  constructor(recipeName, ingredients, preparationTime, cookingMethod, nutritionalInfo) {
      super(ingredients, preparationTime, cookingMethod, nutritionalInfo);
      this.recipeName = recipeName;
  }

  allergic(allergen) {
      if (this.ingredients.includes(allergen)) {
          return `Beware! ${allergen} are in ${this.recipeName} dish`;
      } else {
          return `Relax! ${allergen} is not in ${this.recipeName} dish`;
      }
  }
}

const recipe1 = new KenyanRecipe("githeri", 6, "beans, nuts and maize", "30 mins", "stew", "well balanced meal");
console.log(recipe1.portions(6));

const recipe2 = new RwandaRecipe("Isombe", ["beans", "meat", "onions"], "30 mins", "boil and fry", "kills children with no pain");
console.log(recipe2.allergic("yams"));
console.log(recipe2.allergic("beans"));


// question3

class Species {
    constructor(name, diet, lifespan, month) {
        this.name = name;
        this.diet = diet;
        this.lifespan = lifespan;
        this.month = month;
    }

    track() {
        if (this.month <= 0) {
            return 'Month not available';
        } else if (this.month <= 6) {
            const migrationPattern = 'South to East';
            return `${this.name}\nDiet: ${this.diet}\nLifespan: ${this.lifespan}\nMigration pattern: ${migrationPattern}`;
        } else if (this.month >= 6 && this.month <= 12) {
            const migrationPattern = 'North to West';
            return `${this.name}\nDiet: ${this.diet}\nLifespan: ${this.lifespan}\nMigration pattern: ${migrationPattern}`;
        }
        return 'Month is in the calendar';
    }
}

class Predator extends Species {
    constructor(name, diet, lifespan, month, prey) {
        super(name, diet, lifespan, month);
        this.prey = prey;
    }

    track() {
        const track = super.track();
        return `${track}\nPrey: ${this.prey}`;
    }
}

class Prey extends Species {
    constructor(name, diet, lifespan, month, predator) {
        super(name, diet, lifespan, month);
        this.predator = predator;
    }

    track() {
        const track = super.track();
        return `${track}\nPredator: ${this.predator}`;
    }
}

const animalOne = new Predator('Lion', 'Herbivores', '30 years', 13, ['Antelopes', 'Gazelles', 'Zebras']);
console.log(animalOne.track());

const animalTwo = new Prey('Zebra', 'Grass', '8 years', 7, ['Cheetah', 'Lion', 'Black Panther']);
console.log(animalTwo.track());

// q4

class MusicFestival {
  constructor() {
    this.artists = [];
    this.genre = ['hiphop', 'reggae', 'R&B', 'acoustic'];
    this.instruments = [];
    this.lineUp = [];
  }
}
class Stage extends MusicFestival {
  constructor() {
    super();
    this.lights = 'white';
    this.instrument = ['Drum', 'microphone'];
  }
  addToLineUp(musicType) {
    if (this.genre.includes(musicType)) {
      this.lineUp.push(musicType);
    } else {
      return 'This music type is not available';
    }
  }
  stageManagement() {
    if (this.genre == 'hip hop') {
      this.lights = 'Blue lights';
      return this.lights;
    } else if (this.genre == 'reggae') {
      this.lights = 'Green lights';
      return this.lights;
    } else if (this.genre == 'R&B') {
      this.lights = 'Bright lights';
      return this.lights;
    } else {
      return this.lights;
    }
  }
  instrumentAssign() {
    if (this.genre == 'hiphop') {
      this.instrument.push('bass');
      return this.instrument;
    } else if (this.genre == 'R&B') {
      this.instrument.push('saxophone');
      return this.instrument;
    } else if (this.genre == 'reggae') {
      this.instrument.push('lead');
      return this.instrument;
    } else {
      return this.instrument;
    }
  }
}
const festival = new MusicFestival();
const stage = new Stage();
stage.addToLineUp('hiphop');
stage.addToLineUp('reggae');
console.log(stage.lineUp);
console.log(stage.stageManagement());
console.log(stage.instrumentAssign());

// q5

class Product {
  constructor(name, price, quantity) {
     this.name = name;
     this.price = price;
     this.quantity = quantity;
  }
  get totalValue() {
     if (this.price > 0 && this.quantity > 0) {
       return `The total price is ${this.price * this.quantity}\$`;
     } else {
       return `The total price is invalid`;
     }
  }
  }
  const product = new Product("apple", 122, 2);
  console.log(product.totalValue());
  const product1 = new Product("mango", 0, 0);
  console.log(product1.totalValue());
// q6
class Student {
  constructor(name, age, grades) {
    this.name = name;
    this.age = age;
    this.grades = grades;
  }
  get averageGrade() {
    return this.grades.reduce((acc, grade) => acc + grade) / this.grades.length;
  }
  get details() {
    return `The student is called ${this.name} and is ${this.age} and scored an ${this.grades}`;
  }
  get hasPassed() {
    return this.averageGrade() >= 60;
  }
  get hasFailed() {
    return this.averageGrade() <= 60;
  }
}
const student = new Student("Diana", 24, [25, 56, 78, 80]);
const student2 = new Student("Diana", 24, [25, 96, 78, 90]);
const student3 = new Student("Diana", 24, [25, 12, 8, 10]);



 