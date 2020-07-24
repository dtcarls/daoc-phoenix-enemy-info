import sys, re, pickledb, time
from phoenix_parser import PhoenixParser
from rrs import RealmRanks
import tkinter as tk

## Counts and returns the # of successful attacks with both hands
def parse_enemies(db, openFile,tkWindow,label,charinfoStr,found,charName):
    """Friend or Fiend"""
    try:
        line = openFile.readline()
        if line:
            if not found and line.find('You target') != -1:
                result = re.search(r"\[([A-Z][a-z]+)\]", line)
                if result:
                    charName = result.group(1)
                    found = True
            elif found:
                found = False
                if line.find('enemy realm!') != -1:
                    print("ENEMY: " + str(charName))
                    if not db.get(charName):
                        char = PhoenixParser(charName)
                        p = char.info
                        charinfo = p.player_name + "\n" + p.player_level + "\n" + p.player_class + "\n" + p.player_rr
                        if p.player_realm == "Mid":
                            label.configure(bg='blue')
                            db[charName]= {'bg':'blue','info':charinfo}
                        else:
                            label.configure(bg='red')
                            db[charName]= {'bg':'red','info':charinfo}
                        charinfoStr.set(charinfo)
                    else:
                        p = db.get(charName)
                        label.configure(bg=p['bg'])
                        charinfoStr.set(p['info'])
                # else:
                #     print("friend: " + str(charName))
                #     charinfoStr.set("FRIEND\n"+str(charName))
                #     label.configure(bg='green')
        tkWindow.after(10,lambda:parse_enemies(db, openFile,tkWindow,label,charinfoStr,found,charName))
    except Exception as e:
        print(e)
        openFile.close()
        exit(0)

def main() :
    in_path = 'C:\\Users\\deant\\Documents\\Electronic Arts\\Dark Age of Camelot\\'
    log_name = 'chat.log'
    #log_name = 'chat_buffers.tmp'
    db = pickledb.load('daoc.db', False)
    print(in_path+log_name)
    try:
        window = tk.Tk()
        charinfo = tk.StringVar()
        label = tk.Label(
            textvariable = charinfo,
            background = "purple",
            foreground = "white",
            font = ("Courier", 44)
            )
        label.pack()
        charinfo.set("Welcome")
        window.attributes('-topmost', True)
        readf = open(in_path+log_name, 'r')
        ### Go to end of file
        #readf.seek(0,2)
        parse_enemies(db, readf, window, label, charinfo, False, '')
        window.mainloop()
        readf.close()
        db.dump()
        print("here")
    except IOError:
        print("Failed to open "+ log_name)

main()