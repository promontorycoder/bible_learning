bible_learning.py

Program name: Bible Quiz
Program Creator: promontorycoder

Purpose of Program: 
    Scripture and song learning quiz for JW's
            
    Creator used to help with python and tkinter learning.

Credits:
    JW.ORG        

________________________________________________________________________________

REQUIREMENTS FOR UBUNTU 20.04
________________________________________________________________________________

python3
    sudo apt-get install -y python3
    
tkinter
    sudo apt-get install -y python3-tk
    
pydub
    pip3 install pydub
    
PIL
    pip3 install Pillow 

________________________________________________________________________________

GIT CLONE LINK
________________________________________________________________________________

# To git clone into the repository folder, enter the following command into 
# Terminal after navigating from within Terminal to the folder you'd like the
# program folder to be cloned to.

git clone https://github.com/promontorycoder/bible_learning.git
________________________________________________________________________________

INSTALLATION INSTRUCTIONS FOR UBUNTU 20.04
________________________________________________________________________________

Step 1: Acquire program files
    Copy files via git clone or other method to chosen install folder

Step 2: Make program files executable
    Open gnome-terminal and navigate to folder with downloaded program files
    Enter the following commands into gnome-terminal:
        chmod +x bible_learning.py
        chmod +x bible_learning.sh
        chmod +x bible_learning.desktop
        
Step 3: Edit files to reflect your directory structure
    Open bible_learning.sh into text editor and change line 2 file path to match
    your file structure
    Save and exit file
    
    Open bible_learning_start.desktop into text editor and change lines 5, 6 and
    7 to match your file structure
    Save and exit file
    
Step 4: Install tkinter, pydub and Pillow if you do not already have them 
        installed:
            Open gnome-terminal and execute the following commands:
            sudo apt-get install -y python3-tk
            pip3 install pydub
            pip3 install Pillow
        
Step 5: Copy .desktop file to /usr/share/applications
        Open gnome-terminal and enter the following command:
            sudo cp bible_learning.desktop /usr/share/applications

