import json
class playerprefs:
    def __init__(self, code):
        self.code = code
    def savebool(self, boolvalue:bool):
        bumba = '"'
        hoba = "{"
        hobas = "}"
        file = open(self.code+"prefs"+".json", "w")
        def sucuk(bools:bool):
            if bools == True:
                return "True"
            else:
                return "False"
        text = f"""
{hoba}
    {bumba}playerprefs{bumba}: [
        {hoba}
            {bumba}{self.code}{bumba}: {bumba}{sucuk(boolvalue)}{bumba}
        {hobas}
    ]
{hobas}
        """
        file.write(text)
        file.close()
    def getbool(self):
        with open(self.code+"prefs"+".json",) as f:
            data = json.load(f)
        a = ""
        for name in data["playerprefs"]:
            a = name[self.code]
        def sck(bas):
            if bas == "True":
                return True
            elif bas == "False":
                return False
        return sck(a)
while True:
    class prefix:
        def __init__(self):
            try:
                file = open("prefix.comaz", "x")
                file.close()
            except:
                pass
            file = open("prefix.comaz", "r")
            asd = file.readline()
            self.prefix = asd.replace(" ", "")
            file.close()
        def setPrefix(self, newPrefix):
            file = open("prefix.comaz", "w")
            file.write(newPrefix)
            file.close()
            zile = open("prefix.comaz", "r")
            asd = zile.readline()
            self.prefix = asd.replace(" ", "")
            zile.close()
        def getPrefix(self):
            if self.prefix == "":
                return "?"
            else:
                return self.prefix.replace(" ", "")
    class mutedUsers:
        def __init__(self):
            protmutedList = []
            self.mutedList = []
            try:
                file = open("alreadymutedusersList.comaz", "x")
                file.close()
            except:
                pass
            Lengthcount = 0
            file = open("alreadymutedusersList.comaz", "r")
            for line in file:
                if line != "\n":
                    Lengthcount += 1
            file.close()
            file = open("alreadymutedusersList.comaz", "r")
            for i in range(Lengthcount):
                protmutedList.append(file.readline())
            file.close()
            asd = ""
            for i in protmutedList:
                asd = i.replace("\n", "")
                self.mutedList.append(asd)
        def addUser(self, userID):
            self.mutedList.append(userID)
        def getUsers(self):
            return self.mutedList
    print(mutedUsers().getUsers())
    asda = input("msg: ")
    if asda.startswith(prefix().getPrefix()+"prefix"):
        bumbesz = asda.replace(prefix().getPrefix()+"prefix", "")
        prefix().setPrefix(bumbesz)
    elif asda.startswith(prefix().getPrefix()+"getprefix"):
        buasz = asda.replace(prefix().getPrefix()+"getprefix", "")
        print(prefix().getPrefix())
    else:
        commands = [prefix().getPrefix()+"ban", prefix().getPrefix()+"mute", prefix().getPrefix()+"warn"]
        file = open("botcommand.comaz", "w")
        asd = asda.replace(" ", "\n")
        bumbe = asd.replace("_", " ")
        file.write(bumbe)
        file.close()
        bumbez = []
        zile = open("botcommand.comaz", "r")
        for i in range(3):
            bumbez.append(zile.readline())
        zile.close()
        vindak = []
        zindak = ""
        for i in bumbez:
            zindak = i
            vumbak = zindak.replace("\n", "")
            vindak.append(vumbak)
        command = []
        id = []
        reason = []
        command.append(vindak[0])
        id.append(vindak[1])
        reason.append(vindak[2])
        if command[0] == prefix().getPrefix()+"ban":
            print(f"""
---
|✔| {id[0]} was banned | {reason[0]}
---
            """)
        elif command[0] == prefix().getPrefix()+"mute":
            for i in mutedUsers().getUsers():
                print(i)
                if id[0] == i:
                    playerprefs("isMuted").savebool(False)
                else:
                    playerprefs("isMuted").savebool(True)
            print(playerprefs("isMuted").getbool())
            if playerprefs("isMuted").getbool():
                print(f"""
-----
|❌| {id[0]} cant muted because this user already muted
-----
                """)
            else:
                print(f"""
---
|✔| {id[0]} was muted | {reason[0]}
---
                """)
        elif command[0] == prefix().getPrefix()+"warn":
            print(f"""
---
|✔| {id[0]} was warned | {reason[0]}
---
            """)
        else:
            print("prefix: "+prefix().getPrefix())
        print(bumbez)
        print(vindak)
        print(command),print(id),print(reason)