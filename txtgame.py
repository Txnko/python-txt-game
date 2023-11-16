import time
import sys

inventory = []

creepy_doll = False

def has_key():
    if "doll" in inventory:
        return True
    else:
        return False

    
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.06)
        
def win():
    print(" ====================== \n                You May Rest \n ======================")
    start_game()
        
def died():
    print(" ====================== \n                 You Died \n ======================")
    start_game()


def start_game():

    delay_print("A dark gloom, a cold wisp, the smell of blood and the taste of metal. you have arrived at Maliketh's Ruins. \n")

    delay_print("The one who crawls in the shadows, you who does not fear death, what do they call you?... \n")

    name = input(": ")

    delay_print("Greetings, " + name + ". let us see what impact you shall cause... \n")

    def throne_room():

        delay_print("You step into the ruins, droplets of water fall from the caved in ceiling. a rotten throne made of bones and skulls sits in the middle. there are two doors either side, on the left, a large oak door soaked in blood. on the right a large metal door with multiple dents, from the inisde. \n")

        delay_print("What door do you enter Left/Right ?. \n")

        choice = input(": ")

        if choice == "right" and has_key() == False:
            delay_print("\n (You don't have the required items to enter this room.) \n")
            throne_room()


        if choice == "right" and has_key():

            def zodd():
                delay_print("You enter a large room covered in darkness, in the centre you see a mound of furr. the pile grows and turns into a beast... ZOD THE IMMORTAL.\n You quickly draw the Runic Sword and put on Maliketh's Mask.\n")
                delay_print("Do you stay and fight or do you run.\n")
                zchoice = input(": ")
                if zchoice == "run":
                    delay_print("\n  As you turn to run for the door Zodd charges at you and drives his blade through your chest. \"I wonder if the next one shall run too...\". \n ")
                    died()
                if zchoice == "fight":
                    delay_print("\n You unwaveringly raise your sword in front of Zodd and face the stricken beast directly. Aware that one of you will die, you cannot leave without a struggle. You battle for what seems like a lifetime, Zodd falls, your blade's runes turn to ash as Maliketh's mask cracks and hits the ground. You won, yet you also failed. You stumble and drop to the ground while Zodd's body lies motionless and a faint whisper can be heard. \"You won't be the last, I promise.\"\n")
                    win()
                else:
                    delay_print("\n (Incorrect input.) \n")
                    zodd()
            zodd()
            
            

        if choice == "left":

            def left_door():

                delay_print("\n you enter a hallway with three doors, what door do you dare enter. \n The first door covered in blood and scratches. \n The second door with strange runes etched into the door. \n The third door with nothing but an eye at the centre. \n")
                delay_print("Which door do you enter? (1/2/3).\n *if you want to exit to the throne room press 4*\n")
                choice = input("\n : ")

                if choice == "4":
                    throne_room()

                if choice == "3":

                    def room1():
                        delay_print("You enter an isolated room, you find shackled to the wall an Elven witch, her beatuy fills the room with a dull glow. \n")
                        delay_print("Do you: \n 1. free the witch despite your sense of survial telling you otherwise. \n 2. kill the witch. \n 3. leave the room. \n(1/2/3) \n ")
                        Witch_choice = input(": ")

                        if Witch_choice == "1":
                            delay_print("\n The Witch thanks you with a tear glistening in her eye, you turn to the door to continue your journey. you take a step to no avail, your whole body has becomed paralized and your vision darkens, the witch consumes your being and chains herself to the wall for her next wanderer. \n")
                            died()

                        if Witch_choice == "3":
                            delay_print("\n You turn back to the door, as you go to leave the room you feel a bruning scowl at the back of your head. you don't dare turn back and leave to the hallway. \n")
                            left_door()
                            
                        if Witch_choice == "2":
                            delay_print("\n You draw your wrist-mounted crossbow up to her head, she pleads for her life, chains rattling, eyes streaming with tears. you look her dead in the eye and shoot. Silence fills the room as her body turns to ash. in the remains you see a sparkle, you pull out a doll from the ashes. \n(+1 creepy doll)\n")
                            inventory.append("doll")
                            delay_print("\n You head towards the door, a lingering thought at the back of your mind... why did she deserve that. \n")
                            left_door()
                            
                        else:
                            delay_print("\n (Incorrect input.) \n")
                            room1()

                    room1()

                if choice == "2":

                    def room2():
                        delay_print("You enter the second door and see a small golin scholar writing something on a tiny desk. \n")
                        delay_print("do you: \n 1. try to talk to him. \n 2. do you leave the room?\n 3. do you offer him some food. \n ")
                        gob_choice = input(": ")

                        if gob_choice == "1":
                           delay_print("The Goblin suddenly stops writing as you utter a word, he looks up at you, his eyes draw you in, you feel like you can see everything yet nothing in it's eyes. a rune is burnt into your skull and you fall to the floor, the Goblin loomes over you, his eyes close and so do yours. \n")
                           died()

                        if gob_choice == "2":
                            delay_print("You leave the room as the goblin keeps writing, a shadow passes through you as you leave the room, you hear a faint whisper from behind \"Until next time struggler...\". \n ")
                            left_door()

                        if gob_choice == "3":
                            delay_print("You break off a piece of bread and leave it next to him, you turn to leave the room when you hear the shift of a chair. You look back to see the goblin staring at you. He points towards a chest in the corner. inside you a find a mask confused you turn to the goblin. \"Maliketh's Mask, that is. Death will come \". \n")
                            delay_print("You take the mask and stow it away, as you leave the Goblin returns to his seat and begins to write. \n (+1 Maliketh's Mask)")
                            left_door()

                        else:
                            delay_print("\n (Incorrect input.) \n")
                            room2()
                            
                    room2()
                    
                if choice == "1":

                    def room3():
                        delay_print("You enter the first door and see a blade stuck in the ground, the room is empty and filled with darkness, one single ray of moonlight displaying the blade. \n")
                        delay_print("do you: \n 1. try to take the sword out of the ground. \n 2. test how sharp the blade is. \n 3. do you leave the room. \n ")
                        blade_choice = input(": ")

                        if blade_choice == "1":
                            delay_print("As your hands grip the hilt, you feel a coldness wrap around your body... you've been petrified. \n")
                            died()

                        if blade_choice == "3":
                            delay_print("You leave the room as the goblin keeps writing, a shadow passes through you as you leave the room, you hear a faint whisper from behind \"Until next time struggler...\". \n ")
                            left_door()

                        if blade_choice == "2":
                            delay_print("Your finger touches the blade's edge and blood runs down the side, the ground shakes and the blade begins to shift, you pull the blade from the ground. \n")
                            delay_print("You sheath the sword as you head for the door. \n (+1 Runic Blade)")
                            left_door()
                        else:
                            delay_print("\n (Incorrect input.) \n")
                            room3()
                    
                    room3()

                else:
                    delay_print("\n (Incorrect input.) \n")
                    left_door()

                    

            left_door()

        else:
            delay_print("\n (Incorrect input.) \n")
            throne_room()

        
    throne_room()
    
start_game()
       
