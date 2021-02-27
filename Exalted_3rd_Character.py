import json
import cmd
import yaml


#General helpfunctions for CharacterPrompt
def dice_build_statlist(in_arglist,in_statlist):
    statlist=in_statlist
    arglist=in_arglist
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
    return statlist

def charm_build_list(in_arglist,in_charmlist):
    charmlist=in_charmlist
    arglist=in_arglist
    for t_key in arglist:
            if t_key in TheCharacter.get("charms"):
                ttmp = TheCharacter.get("charms").get(t_key)
                charmlist.append(ttmp)
    return charmlist

class CharacterPrompt(cmd.Cmd):
    intro = 'Welcome to Exalted 3rd Character Shell. Type help or ? to list commands.\n '
    prompt = 'Character: '
    def do_exit(self, inp):
        print("Thank you for using Exalted 3rd Character Interfaces")
        return True

    #Overall Character commands
    def do_allcharacter(self, inp):
        print(yaml.dump(TheCharacter, default_flow_style=False))
    def help_allcharacter(self):
        print("Print the entire character statistics")
    def do_shortallcharacter(self, inp):
        print(str(TheCharacter))
    def do_shortcharacter(self, inp):
        statlist = []
        statlist.append(TheCharacter.get("charactername"))
        statlist.append(TheCharacter.get("essence"))
        statlist.append(TheCharacter.get("abilities"))
        statlist.append(TheCharacter.get("attributes"))
        statlist.append(TheCharacter.get("healthlevels"))
        print(yaml.dump(statlist, default_flow_style=False))

    #Top Level Statistics
    def do_name(self, inp):
        print(yaml.dump(TheCharacter.get("name"), default_flow_style=False))
    def help_name(self, inp):
        print("Shows the character Name")
    def do_essence(self, inp):
        print(yaml.dump(TheCharacter.get("essence"), default_flow_style=False))
    def help_essence(self, inp):
        print("Shows the Exalt's permanent esssence")
    def do_willpower(self, inp):
        print(yaml.dump(TheCharacter.get("willpower"), default_flow_style=False))
    def help_willpower(self, inp):
        print("Shows permanent willpower")

    #Attributes commands
    def do_attributes(self, inp):
        print(yaml.dump(TheCharacter.get("attributes"), default_flow_style=False))

    #Abilities commands
    def do_abilities(self, inp):
        print(yaml.dump(TheCharacter.get("abilities"), default_flow_style=False))
    def do_shortabilities(self, inp):
        print(str(TheCharacter.get("abilities")))
    def do_ability(self, arg):
        if arg == "" or len(arg.split()) > 1:
            print("need one ability argument to print a value")
            print("or did you mean abilities")
            return
        print(TheCharacter.get("abilities")[arg])

    #Weapons commands
    def do_showweapons(self, inp):
        print(yaml.dump(TheCharacter.get("weapons"), default_flow_style=False))

    #show all charims
    def do_showallcharms(self, inp):
        print(yaml.dump(TheCharacter.get("charms"), default_flow_style=False))
    def do_excellencies(self, inp):
        print(yaml.dump(TheCharacter.get("charms").get("excellencies"), default_flow_style=False))
    def do_charmlist(self, arg):
        arglist=arg.split()
        charmlist = []
        charm_build_list(arglist,charmlist)
        print(charmlist)


    #Dice Pools, common Pools
    def do_joinbattle(self, arg):
        self.onecmd("dice perception awareness")
    def help_joinbattle(self):
        print("shows join battle roll (perception+awareness)")
    def do_shapespell(self, arg):
        self.onecmd("dice intelligence occult")
    def help_shapespell(self):
        print("shows the roll how to shape (case) a spell (intelligence+occult)")
    def do_decisiveattack(self, arg):
        print("########## Archery #########")
        self.onecmd("dice dexterity archery")
        print("########## Melee #########")
        self.onecmd("dice dexterity melee")
        print("###### Martial Arts ######")
        self.onecmd("dice dexterity martialarts")
        print("########## Thrown ########")
        self.onecmd("dice dexterity thrown")
    def help_decisiveattack(self):
        print("prints out default all main physical attack pools")
    def do_rush(self, arg):
        self.onecmd("dice dexterity athletics")
    def help_rush(self):
        print("Show Rush pool (dexterity+athletics)")
    def do_disengage(self, arg):
        self.onecmd("dice dexterity dodge")
    def help_disengage(self):
        print("Show Disengage pool (dexterity+dodge)")
    def do_naturalsoak(self, arg):
        self.onecmd("dice stamina")
    def help_naturalsoak(self):
        print("Show Natural Soak (Stamina)")




    #Dice pools, any
    def do_dice(self, arg):
        arglist=arg.split()
        statlist = []
        dice_build_statlist(arglist,statlist)
        print(statlist)
    def help_dice(self):
        print("Usage: dice (ability/attribute/essence/willpower)")
        print("This will give use all stats and the number of dots specified")
        print("example: ")
        print("Character: dice strength dodge")
        print("{'strength', '2'}, {'dodge', '2'}]")

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
