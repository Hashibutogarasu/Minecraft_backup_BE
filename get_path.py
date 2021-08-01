import os
import glob

class mcfunction():
    def getmcpath():
        mcpath = (os.environ["APPDATA"].replace("Roaming","")+"Local/"+"packages/")

        mcpath = mcpath.replace("\\","/")
        
        for name in glob.glob(f'{mcpath}*'):
            name = (name.replace("\\","/"))
            name = (name.replace(mcpath,""))
            name_path = "MinecraftUWP" in name
            if(name_path==True):
                break

        mcpath = (mcpath+name+"/LocalState/games/com.mojang/")

        return mcpath

mcpath = mcfunction.getmcpath()

print(mcpath)