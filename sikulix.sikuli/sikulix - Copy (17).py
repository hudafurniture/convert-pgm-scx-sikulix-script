import sys.argv
import os
# Define path and file name
#-------------------X
#pgm_path = "C:\\sikulix\\pgm_files\\"
#pgm_file_name = "ASAF-BMA-2000"
#sys.argv[1]
#pgm_path_and_file = pgm_path + pgm_file_name + ".pgm"
#-------------------X
directory = "C:\\Ardis\\younis\\2024\\CNC\\CNC_NEW_SCX"


def count_pgm_files(dir):
    if not os.path.isdir(dir):
        return "Directory does not exist." 
    pgm_files = []
    for _, _, files in os.walk(dir):
        pgm_files.extend([file for file in files if file.lower().endswith('.pgm')])
    return len(pgm_files)



log_file = os.path.join(directory,'log.txt')

with open(log_file, 'w') as output:
    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            if dir != "scx":
                pgm_dir = directory + "\\" + dir   
                dir_len = count_pgm_files(pgm_dir)
                counter = 0
                print(pgm_dir)
                for root, dirs, files in os.walk(pgm_dir):
                    for file in files:
                        if file.lower().endswith('.pgm'):
                            file_path = os.path.join(root, file)
                            file_path_windows = file_path.replace('/', '\\')
                            file_name = os.path.splitext(os.path.basename(file_path))[0]
                            if os.path.isfile(file_path):
                                #print(file_path)
                                #print(file_name + ".pgm")
                                scx_file = pgm_dir+ "\\scx\\" + file_name + ".scx"
                                if os.path.exists(scx_file):
                                    continue
                                #--------
                                #### Convert pgm to xxl
                                click("1710936488595.png")
                                wait(1)
                                type("Parsifal")
                                wait(3)
                                type(Key.ENTER)
                                wait(4)
                                reg1 = Region(0,0,134,89)
                                reg1.click("1710943232808.png")
                                wait(1)
                                type(file_path_windows)
                                wait(1)
                                type(Key.ENTER)
                                reg1.click("1710945763614.png")
                                wait(2)
                                reg2 = Region(0,165,209,22)
                                reg2.click()
                                wait(1)
                                type(file_name + ".xxl")
                                type(Key.TAB)
                                type(Key.RIGHT)
                                type(Key.RIGHT)
                                type(Key.ENTER)
                                type(Key.ENTER)
                                type(Key.LEFT)
                                type(Key.ENTER)
                                reg3 = Region(1872,0,48,30)
                                reg3.click()
                                type(Key.ENTER)
                                type(Key.RIGHT)
                                type(Key.ENTER)
                                wait(2)
                                #--------
                                ##### Repair xxl
                                click("1710936488595.png")
                                type("XXL_Parametrs_repair")
                                wait(3)
                                type(Key.ENTER)
                                wait(5)
                                type(Key.TAB)
                                type(pgm_dir)
                                type(Key.ENTER)
                                wait(2)
                                type(Key.ENTER)
                                #--------
                                ##### Convert xxl to scm via PCDrillCam
                                click("1710936488595.png")
                                wait(2)
                                type("pcdrillcam32")
                                wait(5)
                                type(Key.ENTER)
                                centerScreen = Region(677,332,571,391)
                                wait(15)
                                type(Key.ENTER)
                                type(Key.ENTER)
                                type(Key.ENTER)
                                type(Key.ALT + Key.SPACE + "n")
                                wait(2)
                                loadFileReg = Location(1296, 452)
                                loadFileReg.doubleClick()
                                wait(2)
                                selectReg = Region(1101,461,71,49)
                                selectReg.click("1714308592378.png")
                                wait(1)
                                type("p")
                                wait(1)
                                type(Key.RIGHT)
                                wait(1)
                                selectFileReg = Region(1022,434,185,193)
                                selectFileReg.doubleClick("1714309348808.png")
                                wait(1)
                                type(pgm_dir + "\\" + file_name + ".xxl")
                                type(Key.ENTER)
                                wait(2)
                                type(Key.TAB)
                                type(Key.TAB)
                                type(Key.TAB)
                                type(Key.TAB)
                                type(Key.ENTER)
                                fileReg = Region(1280,474,226,55)
                                fileReg.click(Location(1354, 507))
                                new_scx_dir = pgm_dir + '/scx'
                                if not os.path.exists(new_scx_dir):
                                    os.makedirs(new_scx_dir)
                                wait(1)
                                saveAsReg = Region(87,113,60,64)
                                saveAsReg.click("1714310489116.png")
                                wait(3)
                                type(Key.ALT + "n")
                                type(pgm_dir + "\\scx\\" + file_name)
                                wait(1)
                                type(Key.ENTER)
                                wait(1)
                                type(Key.F4, Key.ALT)
                                counter+=1
                                output.write(file_path + '\n')  #if success, add file to output log
                                wait(10)
                output.write(pgm_dir + " ========= " + str(counter) +"/" + str(dir_len) + " SCX Files Completed "  + '\n')



