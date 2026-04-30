name = "Push up", "Running", "Plank"
exercise_type = "Building muscle", "Streaching", "Building six-packs"
calories_burned = "205 calories", "182 calories", "157 calories"

#a list to store workout sessions
workouts = ["Push up", "Running", "Plank"]

class FitnessProgressTracker:
    def __init__(self):
        self.workouts = ["Push up", "Running", "Plank"]

    def add_workout(self):
        name = input("Enter exercise name:")
        type = input("Enter exercise type:")
        calories= input("Enter exercise calories burned") 

        workout = [name, type, calories]
        self.workouts.append(workout)

    def average_calories(self):

      #calculate the average calorie

      number1 = int(input("205"))
      number2 = int(input("182")) 
      number3 = int(input("157"))

      average = (number1 + number2 + number3) / 3

      print("The average of those 3 numbere is:", average)
      return average 
    
    
    def display_summary(self):
         for workhout in self.workouts:
               print(workouts["name"], workouts["exercise_type" ], workouts["calories"])


         print("Average:", self.average_calorie())

         # While loops that have a question while it's counting numbers

         countdown = 10

         while countdown > 0:
             print(countdown)
             countdown -= 1

             print("Another workout or stop?")

             calories = int(input("205, 182, 157"))


             # Store each workout as a dictionary

         X = {
             "Name": {"Push up": 205, "Running": 182, "Plank": 157},
             
        }

         print("Lucky:", self.name)

         for workout in self.workouts:
             print ("-", workout["Push up"],["Building muscle"],["205 calories"])
         workout(["Running"], ["Streaching"], ["182 calories"])
         workhout(["Plank"],["Building six-packs"], ["157 calories"])         

          