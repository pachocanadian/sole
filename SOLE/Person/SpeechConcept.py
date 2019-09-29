import random

class SpeakerTest:
    """ Concept for variables and f strings that people will speak. Variables are current just a placeholder for testing. """

    day_times = ["morning", "afternoon", "evening"]
    jobs = ["manager", "accountant", "technician", "consultant", "office worker"]
    ages = [i for i in range(18, 71)]
    genders = ['man', 'woman']
    times = ['morning', 'afternoon', 'evening']
    sports_teams = ['X-rays', 'Yankees', 'Zulus']
    foods = ['apples', 'bananas', 'steak', 'potatoes', 'rice', 'curries']
    drinks = ['water', 'milk', 'juice', 'tea', 'coffee', 'beer', 'wine', 'vodka']

    place_holder_variable = "x"

    first_name, last_name, occupation, age, gender, time_of_day, target_floor, favourite_sports_team, favourite_food, favourite_drink, time_in_building = (
        place_holder_variable * 11
    )

    def assign_variable(self, list, attribute):
        try:
            attribute = random.choice(list)

        except Exception:
            print("Invalid list to assign to SpeakerPerson attribute. Passing.")
            pass

    positive_phrases = [
        "What a great day to be alive!",
        "I love elevators! Imagine having to take the stairs...",
        "Stairs used to be cutting edge science. Thank goodness we've progressed since then!",
        "Almost there, I'll be home any minute now.",
        "I love the smell of freshly cleaned carpets.",
        f"My favourite thing about being a {occupation} is getting to work here!",
        f"{first_name} {last_name}, reporting for duy!",
        f"I can't wait to see the {favourite_sports_team} play this weekend!",
        f"Getting to {target_floor} is always fast here.",
    ]

    neutral_phrases = [
        "I better get a move on.",
        "Another day, another rat race lap.",
        "Another day, another crashed server.",
        "Another day, another coffee.",
        "Ugh... here we go again.",
        "I need to go to the bathroom." f"I am a {gender}, let me on the elevator, please.",
        f"{first_name} will hopefully be ready by the time I get there.",
        f"I want to be a good {occupation}",
        f"I hope {favourite_drink} and {favourite_food} are on the menu today.",
        f"I get off at floor {target_floor}.",
        f"I've been here for {time_in_building} minutes.",
    ]

    negative_phrases = [
        "This is taking forever.",
        "I'm going to be late thanks to this elevator!",
        "I hate waiting around like this.",
        "I took this job so I WOULDN'T waste time!",
        "This is a terrible experience.",
        "Let me in, let me in, let me in...",
        "Let me on, let me on, let me on...",
        "Feeling cruddy.",
        "I want to leave.",
        "There's no way I'd come here again.",
        f"I hate the {time_of_day}!"
        f"I wouldn't want to be here if I was younger than {age}.",
        f"I just want to get to {target_floor} already!",
    ]

    def speak_positive(self):
        print(random.choice(self.positive_phrases))
    
    def speak_neutral(self):
        print(random.choice(self.neutral_phrases))

    def speak_negative(self):
        print(random.choice(self.negative_phrases))

a = SpeakerTest()
a.speak_positive()
a.speak_neutral()
a.speak_negative()