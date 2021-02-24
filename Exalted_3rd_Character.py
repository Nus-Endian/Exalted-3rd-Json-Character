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
        print(TheCharacter.get("abilities")[arg])
        #arg)

    #Dice Pools, common Pools
    def do_joinbattle(self, arg):
        self.onecmd("dice perception awareness")
    def help_joinbattle(self):
        print("shows joinbattle (perception+awareness)")

    #Dice pools, any
    def do_dice(self, arg):
        arglist=arg.split()

        statlist = []
        for t_key in arglist:
            if t_key in TheCharacter:
                    ttmp = {TheCharacter.get(t_key), t_key}
                    statlist.append(ttmp)
            else:
                if t_key in TheCharacter.get("abilities"):
                    ttmp = {TheCharacter.get("abilities").get(t_key), t_key}
                    statlist.append(ttmp)
                if t_key in TheCharacter.get("attributes"):
                    ttmp = {TheCharacter.get("attributes").get(t_key), t_key}
                    statlist.append(ttmp)
        print(statlist)
    def help_dice(self):
        print("Usage: dice (ability/attribute/essence/willpower)")
        print("This will give use all stats and the number of dots specified")
        print("example: ")
        print("Character: dice strength dodge")
        print("{'strength', '2'}, {'dodge', '2'}]")

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

if __name__ == '__main__':
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
