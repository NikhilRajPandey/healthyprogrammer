
import datetime
import pygame

pygame.init()

# costmizable variables
water = 'water.mp3'
eyes = 'eyes.mp3'
physical = 'physical.mp3'

input_name = input("Please input your name:")

print(f"{input_name.capitalize()} welecome to the office")

file = input_name

water_alarm = 20 # minutes
eyes_alarm = 30 # minutes
physical_alarm = 45 # minutes


# non-costimizable variables
ex = True
d = datetime.datetime.now()
water_timer = d.minute + water_alarm
eyes_timer = d.minute + eyes_alarm
physical_timer = d.minute + physical_alarm

_file = open(file,'a')

print(d)
while ex!= False:
    new_d = datetime.datetime.now()

    if water_timer >= 60 or eyes_timer >= 60 or physical_timer >= 60:
        if water_timer >= 60:
            water_timer = water_timer - 60
            d = datetime.datetime.now()
            minute = d.minute

        if eyes_timer >= 60:
            eyes_timer = eyes_timer - 60
            d = datetime.datetime.now()
            minute = d.minute

        if physical_timer >= 60:
            physical_timer = physical_timer - 60
            d = datetime.datetime.now()
            minute = d.minute
    else:
        if new_d.minute == physical_timer and new_d.minute == water_timer:
            print("Drink water and then do physical",new_d)

            pygame.mixer.music.load(water)
            pygame.mixer.music.play()

            _input4 = input()

            if _input4.lower() == "drank":
                _file.write(f"Drank Water at {datetime.datetime.now()} \n \n")
                pygame.mixer.music.stop()

            pygame.mixer.music.load(physical)
            pygame.mixer.music.play()

            _input5 = input()
            if _input5.lower() == "pydone":
                pygame.mixer.music.stop()
                _file.write(f"Physical Exercise done at {datetime.datetime.now()} \n \n")
                d = datetime.datetime.now()
                eyes_timer = d.minute + eyes_alarm
                water_timer = d.minute + water_alarm
                physical_timer = d.minute + physical_alarm


        elif new_d.minute == physical_timer and new_d.minute == eyes_timer:
            print("First do eyes exercise and then do physical")

            pygame.mixer.music.load(water)
            pygame.mixer.music.play()

            _input6 = input()

            if _input6.lower() == "eydone":
                _file.write(f"Eye Exercise done at {datetime.datetime.now()} \n \n ")
                pygame.mixer.music.stop()

            pygame.mixer.music.load(physical)
            pygame.mixer.music.play()

            _input7 = input()
            if _input7.lower() == "pydone":
                pygame.mixer.music.stop()
                _file.write(f"Physical Exercise done at {datetime.datetime.now()} \n \n")

                d = datetime.datetime.now()
                eyes_timer = d.minute + eyes_alarm
                water_timer = d.minute + water_alarm
                physical_timer = d.minute + physical_alarm



        elif new_d.minute == water_timer and new_d.minute == eyes_timer:
            print("Drink water and then do eyes exercise")

            pygame.mixer.music.load(water)
            pygame.mixer.music.play()

            _input8 = input()

            if _input8.lower() == "eydone":
                _file.write(f"Eye Exercise done at {datetime.datetime.now()} \n \n")
                pygame.mixer.music.stop()

            pygame.mixer.music.load(physical)
            pygame.mixer.music.play()

            _input9 = input()
            if _input9.lower() == "drank":
                pygame.mixer.music.stop()
                _file.write(f"Drank Water at {datetime.datetime.now()} \n \n ")
                d = datetime.datetime.now()
                eyes_timer = d.minute + eyes_alarm
                water_timer = d.minute + water_alarm
                physical_timer = d.minute + physical_alarm

        elif new_d.minute == water_timer:
            print("Please drank water",new_d)
            pygame.mixer.music.load(water)
            pygame.mixer.music.play()

            _input = input()

            if _input.lower() == "drank":
                pygame.mixer.music.stop()
                _file.write(f"Drank Water at {datetime.datetime.now()} \n \n")
                water_timer = d.minute + water_alarm

        elif new_d.minute == eyes_timer:
            print("Please do eyes exercise",new_d)
            pygame.mixer.music.load(eyes)
            pygame.mixer.music.play()

            _input2 = input()

            if _input2.lower() == "eydone":
                pygame.mixer.music.stop()
                _file.write(f"Eye Exercise done at {datetime.datetime.now()} \n \n")
                eyes_timer = d.minute + eyes_alarm

        elif new_d.minute == physical_timer:
            print("Please do physical exercise",new_d)
            pygame.mixer.music.load(physical)
            pygame.mixer.music.play()

            _input3 = input()

            if _input3.lower() == "pydone":
                pygame.mixer.music.stop()
                _file.write(f"Physical Exercise done at {datetime.datetime.now()} \n \n")
                d = datetime.datetime.now()
                eyes_timer = d.minute + eyes_alarm
                water_timer = d.minute + water_alarm
                physical_timer = d.minute + physical_alarm



_file.close()



















