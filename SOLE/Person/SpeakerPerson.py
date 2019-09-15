import SOLE
import random


class SpeakerPerson(SOLE.Person.BasePerson):

    _day_times = ["morning", "afternoon", "evening"]
    _jobs = ["manager", "accountant", "technician", "consultant", "office worker"]

    _positive_phrases = [
        "What a great day to be alive!",
        "I love elevators! Imagine having to take the stairs...",
        "Stairs used to be cutting edge science. Thank goodness we've progressed since then!",
        "[Person name] won't get to tell me I'm late today!",
        "Almost there, I'll be home any minute now.",
        "I love the smell of freshly cleaned carpets.",
    ]

    _neutral_phrases = [
        "I better get a move on.",
        "Another day, another rat race lap.",
        "[Person name] will hopefully be ready by the time I get [home/to work].",
        "I want to be a good {JOB_TITLE}.",
        "Another day, another TPS report.",
        "Another day, another crashed server.",
        "Another day, another coffee.",
    ]

    _negative_phrases = [
        "This is taking forever.",
        "I'm going to be late thanks to this elevator!",
        "I hate waiting around like this.",
        "I took this job so I WOULDN'T waste time!",
        "That was a terrible experience.",
    ]

    def __init__(self):
        setattr(self, "job_title", self.return_job())

    def return_job(self):
        return random.choice(self._jobs)

    def speak_positive(self):
        print(random.choice(self._positive_phrases))

    def speak_neatral(self):
        pass

    def speak_negative(self):
        pass
