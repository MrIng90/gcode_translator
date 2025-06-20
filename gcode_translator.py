import numpy as np
import sys
import datetime

G_Code_Move_Commands = {
    "linear": "G1",
    "clockwise": "G2",
    "counterclockwise": "G3",
    "not": "G4",
    "home": "G28"
}

def Move_Commands(command, i):
        text = ""
        text += G_Code_Move_Commands[command[i]]
        text += " "
        print(command[i])
        match command[i]:
            
            case "linear":
                text += XYZ_Movement(command[i + 1], command[i + 2])

            case "not":
                text += Wait_Time(command[i + 1], command[i + 2])
            
            case "home":
                pass
            
            case _:
                raise ValueError("Invalid Move Command")
        
        return text

G_Code_Set_Commands ={
    "units to inches": "G20",
    "units to milimeters": "G21",
    "absolute positioning": "G90",
    "relative positioning": "G91",
    "speed": "G1 F"
}

def Set_Commands(commands, i):
    text = ""

    text += G_Code_Set_Commands[commands[i]]

    match commands[i]:
        case "speed":
            text += commands[i + 1]
        case _:
            raise ValueError("Invalid Set Command")
    return text

def do_loop(text, i):
    output_text = ""
    splitted_text = [x for x in text[i].split(":")]
    splitted_text[0] = splitted_text[0][3:]
    number_of_loops = int(splitted_text[0])

    splitted_text2 = [x for x in splitted_text[1].split(";")]
    for i in range(len(splitted_text2)):
        splitted_text2[i] = [x for x in splitted_text2[i].split()]

    print(splitted_text2)

    for j in range(number_of_loops):
        for n in range(len(splitted_text2)):
            output_text += Move_Commands(splitted_text2[n], 1)
            output_text += "\n"


    return output_text



def XYZ_Movement(axis, number):
    match axis:
        case "x":
            return "X" + number
        case "y":
            return "Y" + number
        case "z":
            return "Z" + number



def Wait_Time(time, mode):
    match mode:
        case "milliseconds":
            return "P" + time
        case _:
            raise ValueError("Invalid Unit given")


def dissasemble_text(text):
    return [x for x in text.split("\n") if x.strip() != ()]

def read_file():
    return open(sys.argv[1], "r").read()

def write_new_commands(text):
    new_text = ""

    for i in range(len(text)):
        split_text = [x for x in text[i].split() if x.strip()]

        match split_text[0]:
            case "move":
                new_text += Move_Commands(split_text, 1)

            case "set":
                new_text += Set_Commands(split_text, 1) 

            case "do":
                new_text += do_loop(text, i)
                


            
            case _:
                raise ValueError("\"" + split_text[0] + "\"" +  " is not a valid command")

        new_text += "\n"

    return new_text

def write_to_file(text):
    open(str(input("Name file: ")) + ".gcode", "w").write(text)

if __name__ == "__main__":
    input_file = read_file()
    input_file_dissasemble = dissasemble_text(input_file)
    new_file_text = write_new_commands(input_file_dissasemble)
    write_to_file(new_file_text)
    




            





