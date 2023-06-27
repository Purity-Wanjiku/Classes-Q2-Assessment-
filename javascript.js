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
 