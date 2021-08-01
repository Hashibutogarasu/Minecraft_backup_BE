import sys
import os
import glob
import shutil
import datetime


dt_now = datetime.datetime.now()

try:
    backuppath=os.path.expanduser('~/mcbackup').replace("\\","/")
    os.mkdir(backuppath)
except:
    pass

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

    def getmcworldpath():

        path = mcfunction.getmcpath()
                
        mcworldpath=path+"minecraftWorlds/"
        
        return mcworldpath


def main():
    mc = mcfunction
    
    mcpath = (mc.getmcpath())
    
    worldpath = mc.getmcworldpath()
    
    files = os.listdir(worldpath)
    
    for worldfile in files:
        try:        
            print(f"\r{worldpath+worldfile}\nバックアップ中.... [0%]",end="")
            shutil.make_archive(f'{backuppath}/backup_{dt_now.strftime("%Y_%m_%d_%H_%M_%S")}', 'zip', root_dir=worldpath)
            print(f"\rバックアップ中... [100%]",end="")
            
        except Exception as e:
            print(f"エラーが発生しました。{worldpath+worldfile}は圧縮されません。\nエラー内容:{e}")
    
    
    print(f'\nワールドデータは{backuppath}/backup_{dt_now.strftime("%Y_%m_%d_%H_%M_%S")}.zipに保存されました。')




if __name__ == "__main__":

    if(os.path.exists(mcfunction.getmcpath())==True):
        print("Minecraft:インストール済み")
    else:
        print("Minecraftがインストールされていません。")
        confirm = input()
        sys.exit()
    try:
        main()
    except Exception as e:
        print("予期せぬエラーが発生しました。")
        print(e)
        sys.exit()
    except KeyboardInterrupt:
        print("バックアップをキャンセルしました。")