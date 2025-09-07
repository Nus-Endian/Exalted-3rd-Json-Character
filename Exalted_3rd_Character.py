import json
import cmd
import yaml
import sys, getopt
import argparse
#from rich import print
#from rich import pretty
#pretty.install()

TheCharacter = None

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

#Functions
def checkCharacterKey(dict, key):

    if key in dict.keys():
        print("", dict[key])
    else:
        print("Not present")
    return

def finddictkey(characterdict,characterkey):
      for k,characterkey in characterdict.items():        
         if isinstance(characterkey, dict):
                iterdict(v)
         else:            
             print (k,":",v)

def from_list_set_output_to_integer(in_list_set):
      # changes a list of sets to a running addition of all numbers
      thenumber = int(0)
      for item in in_list_set:
          for elementitem in item:
             if elementitem.isdigit():
               thenumber = thenumber + int(elementitem)
      return thenumber

def openCharacterFromFile(CharacterFilename):
    global TheCharacter
    with open(CharacterFilename) as f:
                TheCharacter = json.load(f)

def writeCharacterToFile(WriteCharacter, FileName):
    with open(FileName, "w") as outfile:
            json.dump(WriteCharacter, outfile, indent=4)

def updateCharacterValue(inCharacterKey,inCharacterValue):
    CharacterKey = inCharacterKey
    CharacterValue = inCharacterValue
    if inCharacterKey in TheCharacter:
        if inCharacterKey in TheCaracter['attributes']:
            print("Exist attributes")
        elif inCharacterKey in TheCharacter['abilities']:
            print("Exist abilities")
        else:
            TheCharacter[CharacterKey] = CharacterValue
            print("top Exists")
    else:
        print("Does not Exist")

def updateAttributeValue(inCharacterKey,inCharacterValue):
    CharacterKey = inCharacterKey
    CharacterValue = inCharacterValue
    if inCharacterKey in TheCharacter['attributes']:
        TheCharacter['attributes'][CharacterKey] = CharacterValue
        print("Exist attributes")
    else:
        print("Does not Exist")

def updateAbilityValue(inCharacterKey,inCharacterValue):
        CharacterKey = inCharacterKey
        CharacterValue = inCharacterValue
        if inCharacterKey in TheCharacter['abilities']:
            TheCharacter['abilities'][CharacterKey] = CharacterValue
            print("Exist attributes")
        else:
            print("Does not Exist")

def GetSingleCharacterItem  (CharacterObj,KeyValue):
    return yaml.dump(CharacterObj.get(KeyValue), default_flow_style=False)

class CharacterPrompt(cmd.Cmd):
    intro = 'Welcome to the Exalted 3rd Character Shell. Type help or ? to list commands.\n '
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
    def do_shortallcharacter(self, inp):
        statlist = []

        statlist.append(TheCharacter.get("charactername"))
        statlist.append(TheCharacter.get("essence"))
        statlist.append(TheCharacter.get("abilities"))
        statlist.append(TheCharacter.get("attributes"))
        statlist.append(TheCharacter.get("healthlevels"))


        print(yaml.dump(statlist, default_flow_style=False))

    #Top Level Statistics
    def do_name(self, inp):
        print(GetSingleCharacterItem(TheCharacter,"charactername"))
    def do_essence(self, inp):
        print("Essence " + GetSingleCharacterItem(TheCharacter,"essence"))
    def do_willpower(self, inp):
        GetSingleCharacterItem(TheCharacter,"willpower")

    #Attributes commands
    def do_attributes(self, inp):
        print(GetSingleCharacterItem(TheCharacter,"attributes"))

    #Abilities commands
    def do_abilities(self, inp):
        print(GetSingleCharacterItem(TheCharacter,"abilities"))
    def do_shortabilities(self, inp):
        print(yaml.dump(TheCharacter.get("abilities")))
    def do_ability(self, arg):
        #'Save future commands to filename:  RECORD rose.cmd'
        #self.file = open(arg, 'w')
        if arg == "":
            print("need an ability argument to print a value")
            print("or did you mean abilities")
            return
        print(TheCharacter.get("abilities")[arg])
        #arg)
    def help_ability(self):
        print("ability <ability>")
        print("print a single ability's value")

    #Weapons commands
    def do_showweapons(self, inp):
        print(GetSingleCharacterItem(TheCharacter,"weapons"))

    #show all charims
    def do_showallcharms(self, inp):
        print(GetSingleCharacterItem(TheCharacter,"charms"))
    def do_excellencies(self, inp):
        print(yaml.dump(TheCharacter.get("charms").get("excellencies"), default_flow_style=False))
    def do_charmlist(self, arg):
        arglist=arg.split()
        charmlist = []
        charm_build_list(arglist,charmlist)
        print(charmlist)


    #Dice Pools, common Pools
    def do_joinbattle(self, arg):
       # import pdb ; breakpoint()
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
        print(from_list_set_output_to_integer(statlist))
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
    
    #update value functions:
    def do_updateValue(self, arg):
        arglist=arg.split()
        if len(arglist) == 2:
            updateCharacterValue(arglist[0],arglist[1])
        else:
            print("updateValue <character stat> <new value>")

    def do_updateAbility(self, arg):
        arglist=arg.split()
        if len(arglist) == 2:
            updateAbilityValue(arglist[0],arglist[1])
        else:
            print("updateAbility <character stat> <new value>")
    def help_updateAbility(self):
        print("updateAbility <character stat> <new value>")

    def do_updateAttribute(self, arg):
        arglist=arg.split()
        if len(arglist) == 2:
            updateAttributeValue(arglist[0],arglist[1])
        else:
            print("updateAttribute <character stat> <new value>")
    def help_updateAttribute(self):
            print("updateAttribute <character stat> <new value>")

    #Untility Function
    def do_writefile(self, arg):
        writeCharacterToFile(TheCharacter,arg)
    def do_openfile(self, arg):
        openCharacterFromFile(CharacterFilename)    
    def help_writefile(self):
        print("writefile <characterfile.json>")
        print("This writes out to the file specified")
    def do_printCharacterRaw(self, arg):
        print(TheCharacter)

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))

def main(argv):
    global TheCharacter
#    print ('Argument List:', str(sys.argv))
#    print ('Arg length:', len(sys.argv))
#    if len(sys.argv) == 1:
#        print ('For help: use the -h option')
#        sys.exit()
#    try:
#        opts, args = getopt.getopt(argv,"c::",["ifile=","ofile="])
#    except getopt.GetoptError:
#        print ('Exalted_3rd_Character -c <characterfile>')
#        sys.exit()
#    for opt, arg in opts:
#        if opt == '-h':
#            print ('Exalted_3rd_Character -c <characterfile>')
#            sys.exit()
#        elif opt in ("-c", "--character"):
#            inCharacter = arg
#)
parser = argparse.ArgumentParser(
    prog='Exalted 3rd Edition Character Sheet helper',
    description='This assists a player is running their character',
    epilog='-c <character>')
parser.add_argument('-c', '--character', type=str, default='NewCharacter', help='Character Sheet to Load')
parser.add_argument('-l', '--cmdline', action='store_true')

args = parser.parse_args()

if args.character != 'NewCharacter':
    openCharacterFromFile(args.character)
    with open(args.character) as f:
        TheCharacter = json.load(f)

    if(TheCharacter is None):
        print("Please create a Character or open")

    print(str(TheCharacter.get("charactername")))
    print('Character tester')
 
    CharacterPrompt().cmdloop()


if __name__ == '__main__':
    main(sys.argv[1:])



