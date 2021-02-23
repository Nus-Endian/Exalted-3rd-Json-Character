import json
import cmd
import yaml

#Functions
def checkCharacterKey(dict, key):

    if key in dict.keys():
        print("", dict[key])
    else:
        print("Not present")
    return

class CharacterPrompt(cmd.Cmd):
    intro = 'Welcome to Exalted 3rd Character Shell. Type help or ? to list commands.\n '
    prompt = 'Character: '
    def do_exit(self, inp):
        print("Thank you for using Exalted 3rd Character Interfaces")
        return True

    #Overall Character commands
    def do_character(self, inp):
        #print(TheCharacter.keys())
        #print(str(TheCharacter))
        print(yaml.dump(TheCharacter, default_flow_style=False))
    def do_shortcharacter(self, inp):
        print(str(TheCharacter))

    #Top Level Statistics
    def do_name(self, inp):
        print(yaml.dump(TheCharacter.get("name"), default_flow_style=False))
    def do_essence(self, inp):
        print(yaml.dump(TheCharacter.get("essence"), default_flow_style=False))
    def do_willpower(self, inp):
        print(yaml.dump(TheCharacter.get("willpower"), default_flow_style=False))

    #Attributes commands
    def do_attributes(self, inp):
        print(yaml.dump(TheCharacter.get("attributes"), default_flow_style=False))

    #Abilities commands
    def do_abilities(self, inp):
        print(yaml.dump(TheCharacter.get("abilities"), default_flow_style=False))
    def do_shortabilities(self, inp):
        print(str(TheCharacter.get("abilities")))
    def do_ability(self, arg):
        #'Save future commands to filename:  RECORD rose.cmd'
        #self.file = open(arg, 'w')
        if arg == "":
            print("need an ability argument to print a value")
            print("or did you mean abilities")
            return
        print(TheCharacter.get("abilities")[0][arg])
        #arg)

    def do_dice(self, arg):
        print("arg " + arg)
        print(type(arg))
        for t_key in TheCharacter:
            print(TheCharacter.get(t_key))
            print(type(TheCharacter.get(t_key)))

    def help_character(self):
        print("Print the entire character statistics")
    def help_shortcharacter(self):
        print("Print condensed entire character statistics")
    def help_abilities(self):
        print("Prints long form of abilities")
    def help_shortabilities(self):
        print("Prints a condensed list of Character abilities")
    def help_attributes(self):
        print("Prints list of character Attributes")

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))


with open('Character.json') as f:
    TheCharacter = json.load(f)

print(str(TheCharacter.get("charactername")))


CharacterPrompt().cmdloop()


#LoopBreaker = 1
#while LoopBreaker > 0:
#    print("What do you want")
#    t_input = input("Character: ")

#    if t_input.lower() == "exit":
#        exit()

#    if t_input in TheCharacter:
#        print("yes," + t_input + " is one of the keys")

#    if t_input.lower() == "character":
#        print(TheCharacter.keys())

#    checkCharacterKey(TheCharacter, t_input.lower())
