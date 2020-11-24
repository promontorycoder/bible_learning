#! /usr/bin/env python3

# Import necessary python modules
import random
from random import randint

from tkinter import *

from PIL import ImageTk, Image

from pydub import AudioSegment
from pydub.playback import play

# Create program window
root = Tk()
root.title("Bible Quiz!")
root.geometry("900x800")
root.config(bg='gray90')
root.resizable(1, 1)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create global variables for score tracking
global correct
correct = 0
global total
total = 0


def songs_jesus_ransom_answer():
    
    # Reference global variables for score tracking
    global correct
    global total
    
    # Define action for correct answer
    if song_jesus_ransom_radio.get() == songs_jesus_ransom_titles[answer]:
        response = ("Correct! " + songs_jesus_ransom_titles[answer] + 
            " is Song Number " + answer + ".")
        correct += 1
    
    # Define action for incorrect answer
    else:
        response = ("Incorrect! " + songs_jesus_ransom_titles[answer] + 
            " is Song Number " + answer + ".")
    
    total += 1
            
    # Create score text for label
    r_score = "Score: " + str(correct) + " out of " + str(total)
    
    # Update labels with each answer        
    answer_label_songs_jesus_ransom.config(text=response)
    running_score_label.config(text=r_score)

    
def all_songs_answer():

    # Reference global variables for score tracking
    global correct
    global total
    
    if all_songs_radio.get() == all_songs_titles[answer]:
        response = ("Correct! " + all_songs_titles[answer] + 
            " is Song Number " + answer + ".")
        correct += 1    
        
    else:
        response = ("Incorrect! " + all_songs_titles[answer] + 
            " is Song Number " + answer + ".")
    
    total += 1
    
    # Create score text for label
    r_score = "Score: " + str(correct) + " out of " + str(total)
            
    answer_label_all_songs.config(text=response)
    running_score_label.config(text=r_score)


def songs_jah_answer():

    # Reference global variables for score tracking
    global correct
    global total
    
    if song_radio.get() == songs_jah_titles[answer]:
        response = ("Correct! " + songs_jah_titles[answer] + 
            " is Song Number " + answer + ".")
        correct += 1
        
    else:
        response = ("Incorrect! " + songs_jah_titles[answer] + 
            " is Song Number " + answer + ".")
            
    total += 1
    
    # Create score text for label
    r_score = "Score: " + str(correct) + " out of " + str(total)
            
    answer_label_songs_jah.config(text=response)
    running_score_label.config(text=r_score)


def bible_books_quiz_answer():

    global correct
    global total
    
    if bible_books_quiz_radio.get() == bible_books_quiz_titles[answer]:
        response = ("Correct! " + bible_books_quiz_titles[answer] + 
            " is Bible Book Number " + answer + ".")
        correct += 1
        
    else:
        response = ("Incorrect! " + bible_books_quiz_titles[answer] + 
            " is Bible Book Number " + answer + ".")
    
    total += 1
    
    # Create score text for label
    r_score = "Score: " + str(correct) + " out of " + str(total)
            
    answer_label_bible_books_quiz.config(text=response)
    running_score_label.config(text=r_score)


def bible_writers_answer():

    global correct
    global total
    
    if bible_writers_radio.get() == bible_writers_titles[answer]:
        response = ("Correct! " + bible_writers_titles[answer] + 
            " is the author of " + answer + ".")
        correct += 1
        
    else:
        response = ("Incorrect! " + bible_writers_titles[answer] + 
            " is the author of " + answer + ".")
    
    total += 1
    
    # Create score text for label
    r_score = "Score: " + str(correct) + " out of " + str(total)
            
    answer_label_bible_writers.config(text=response)
    running_score_label.config(text=r_score)


# Create function for handling scripture answers
def scrips_answer():
    
    # Reference global variables for score tracking
    global correct
    global total
    
    # Define action for correct answer
    if scrips_radio.get() == scrips_text[answer]:
        response = ("Correct! " + scrips_text[answer] +
                    " is the correct verse!")
        correct += 1
    
    # Define action for incorrect answer    
    else:
        response = ("Incorrect! " + scrips_text[answer] +
                    " is the correct verse!")
    total += 1
    
    # Create score text for label
    r_score = "Score: " + str(correct) + " out of " + str(total)
    
    # Update labels with each answer
    answer_label_scrips.config(text=response)
    running_score_label.config(text=r_score)


def songs_jah():
    
    # Hide previous frames
    hide_all_frames()
    songs_jah_frame.pack(fill="both", expand=1)
    
    # my_label = Label(songs_jah_frame, text="Songs About Jah").pack()
    
    global show_songs_jah
    show_songs_jah = Label(songs_jah_frame)
    show_songs_jah.pack(pady=15)
    
    global songs_jah_nums
    songs_jah_nums = [
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
        ]
        
    global songs_jah_titles
    songs_jah_titles = {
        '1':"Jehovah's Attributes",
        '2':"Jehovah Is Your Name",
        '3':"Our Strength, Our Hope, Our Confidence",
        '4':"Jehovah Is My Shepherd",
        '5':"God's Wondrous Works",
        '6':"The Heavens Declare God's Glory",
        '7':"Jehovah, Our Strength",
        '8':"Jehovah Is Our Refuge",
        '9':"Jehovah Is Our King",
        '10':"Praise Jehovah Our God!",
        '11':"Creation Praises God",
        '12':"Great God, Jehovah",
        }
        
    # Generate Random Number
    global rand_num
    rand_num = randint(0, len(songs_jah_nums)-1)
    
    global answer
    answer = songs_jah_nums[rand_num]
    
    # Create empty answer list and counter
    answer_list = []
    count = 1
    
    # Generate four random song numbers
    while count < 5:
        rand_num = randint(0, len(songs_jah_nums)-1)
        
        # If first selection, make it our answer
        if count == 1:
            answer = songs_jah_nums[rand_num]
            global song_label
            song_label = Label(songs_jah_frame, 
                text=("What is the title of Song Number " + 
                songs_jah_nums[rand_num] + "?"), 
                font="Helvetica 18 bold", fg='DarkOrchid4', bg='gray90')
            song_label.pack(pady=15)
            
        # Add first selection to our list
        answer_list.append(songs_jah_nums[rand_num])
        
        # Remove answer from list
        songs_jah_nums.remove(songs_jah_nums[rand_num])
        
        # Shuffle original list
        random.shuffle(songs_jah_nums)
        
        count += 1
    
    file_path = "music/"
    if len(answer) == 1:
        song_answer = '00' + str(answer)
        music_file = file_path + "sjjm_E_" + song_answer + ".mp3"
        # print(music_file)
        song = AudioSegment.from_mp3(music_file)
        ten_secs = song[:10000]
        play(ten_secs)
    elif len(answer) == 2:
        song_answer = '0' + str(answer)
        music_file = file_path + "sjjm_E_" + song_answer + ".mp3"
        # print(music_file)
        song = AudioSegment.from_mp3(music_file)
        ten_secs = song[:10000]
        play(ten_secs)
    else:
        music_file = file_path + "sjjm_E_" + answer + ".mp3"
        # print(music_file)
        song = AudioSegment.from_mp3(music_file)
        ten_secs = song[:10000]
        play(ten_secs)
    
    random.shuffle(answer_list)
    
    global song_radio
    song_radio = StringVar()
    song_radio.set(songs_jah_titles[answer_list[0]])
    
    song_radio_button1 = Radiobutton(songs_jah_frame, bg='gray90', 
        text=songs_jah_titles[answer_list[0]], variable=song_radio, 
        value=songs_jah_titles[answer_list[0]]).pack()

    song_radio_button1 = Radiobutton(songs_jah_frame, bg='gray90', 
        text=songs_jah_titles[answer_list[1]], variable=song_radio, 
        value=songs_jah_titles[answer_list[1]]).pack()
        
    song_radio_button1 = Radiobutton(songs_jah_frame, bg='gray90', 
        text=songs_jah_titles[answer_list[2]], variable=song_radio, 
        value=songs_jah_titles[answer_list[2]]).pack()
        
    song_radio_button1 = Radiobutton(songs_jah_frame, bg='gray90', 
        text=songs_jah_titles[answer_list[3]], variable=song_radio, 
        value=songs_jah_titles[answer_list[3]]).pack()                

    # Add a "next" button
    next_button = Button(songs_jah_frame, text="Next Song", command=songs_jah, 
        bg='gray90')
    next_button.pack(pady=15)
    
    # Create a button to answer
    song_answer_button = Button(songs_jah_frame, text="Answer",
        command=songs_jah_answer, bg='gray90')
    song_answer_button.pack(pady=15)
    
    # Add a button to clear the score if desired
    score_button = Button(songs_jah_frame, text="Clear Score", command=clscore, 
        bg='gray90')
    score_button.pack(pady=15)
    
    # Create answer label for correct / incorrect
    global answer_label_songs_jah
    answer_label_songs_jah = Label(songs_jah_frame, text="",
        font="Helvetica 20 bold", fg='DarkOrchid4', bg='gray90')
    answer_label_songs_jah.pack(pady=15)
    
    # Create score text for keeping track of score
    r_score_text = "Score: " + str(correct) + " out of " + str(total)
    
    # Create score label for keeping track of score
    global running_score_label
    running_score_label = Label(songs_jah_frame, text=r_score_text, 
        font="Helvetica 20 bold", fg='DarkOrchid4', bg='gray90')
    running_score_label.pack(pady=10)            


def songs_jesus_ransom():
    
    # Hide previous frames
    hide_all_frames()
    songs_jesus_ransom_frame.pack(fill="both", expand=1)
    
    # my_label = Label(songs_jah_frame, text="Songs About Jah").pack()
    
    global show_songs_jesus_ransom
    show_songs_jesus_ransom = Label(songs_jesus_ransom_frame)
    show_songs_jesus_ransom.pack(pady=15)
    
    global songs_jesus_ransom_nums
    songs_jesus_ransom_nums = [
        '13', '14', '15', '16', '17', '18', '19', '20',
        ]
        
    global songs_jesus_ransom_titles
    songs_jesus_ransom_titles = {
        '13':"Christ Our Model",
        '14':"Praising Earth's New King",
        '15':"Praise Jehovah's Firstborn!",
        '16':"Praise Jah for His Son, the Anointed",
        '17':"I Want To",
        '18':"Grateful for the Ransom",
        '19':"The Lord's Evening Meal",
        '20':"You Gave Your Precious Son",
        }
        
    # Generate Random Number
    global rand_num
    rand_num = randint(0, len(songs_jesus_ransom_nums)-1)
    
    global answer
    answer = songs_jesus_ransom_nums[rand_num]
    
    # Create empty answer list and counter
    answer_list = []
    count = 1
    
    # Generate four random song numbers
    while count < 5:
        rand_num = randint(0, len(songs_jesus_ransom_nums)-1)
        
        # If first selection, make it our answer
        if count == 1:
            answer = songs_jesus_ransom_nums[rand_num]
            global song_label
            song_label = Label(songs_jesus_ransom_frame, 
                text=("What is the title of Song Number " + 
                songs_jesus_ransom_nums[rand_num] + "?"), 
                font="Helvetica 18 bold", fg='DarkOrchid4', bg='gray90')
            song_label.pack(pady=15)
            
        # Add first selection to our list
        answer_list.append(songs_jesus_ransom_nums[rand_num])
        
        # Remove answer from list
        songs_jesus_ransom_nums.remove(songs_jesus_ransom_nums[rand_num])
        
        # Shuffle original list
        random.shuffle(songs_jesus_ransom_nums)
        
        count += 1
    
    file_path = "music/"
    if len(answer) == 1:
        song_answer = '00' + str(answer)
        music_file = file_path + "sjjm_E_" + song_answer + ".mp3"
        # print(music_file)
        song = AudioSegment.from_mp3(music_file)
        ten_secs = song[:10000]
        play(ten_secs)
    elif len(answer) == 2:
        song_answer = '0' + str(answer)
        music_file = file_path + "sjjm_E_" + song_answer + ".mp3"
        # print(music_file)
        song = AudioSegment.from_mp3(music_file)
        ten_secs = song[:10000]
        play(ten_secs)
    else:
        music_file = file_path + "sjjm_E_" + answer + ".mp3"
        # print(music_file)
        song = AudioSegment.from_mp3(music_file)
        ten_secs = song[:10000]
        play(ten_secs)
        
    random.shuffle(answer_list)
    
    global song_jesus_ransom_radio
    song_jesus_ransom_radio = StringVar()
    song_jesus_ransom_radio.set(songs_jesus_ransom_titles[answer_list[0]])
    
    song_jesus_ransom_radio_button1 = Radiobutton(songs_jesus_ransom_frame, 
        bg='gray90', text=songs_jesus_ransom_titles[answer_list[0]], 
        variable=song_jesus_ransom_radio, 
        value=songs_jesus_ransom_titles[answer_list[0]]).pack()

    song_jesus_ransom_radio_button1 = Radiobutton(songs_jesus_ransom_frame, 
        bg='gray90', text=songs_jesus_ransom_titles[answer_list[1]], 
        variable=song_jesus_ransom_radio, 
        value=songs_jesus_ransom_titles[answer_list[1]]).pack()
        
    song_jesus_ransom_radio_button1 = Radiobutton(songs_jesus_ransom_frame, 
        bg='gray90', text=songs_jesus_ransom_titles[answer_list[2]], 
        variable=song_jesus_ransom_radio, 
        value=songs_jesus_ransom_titles[answer_list[2]]).pack()
        
    song_jesus_ransom_radio_button1 = Radiobutton(songs_jesus_ransom_frame, 
        bg='gray90', text=songs_jesus_ransom_titles[answer_list[3]], 
        variable=song_jesus_ransom_radio, 
        value=songs_jesus_ransom_titles[answer_list[3]]).pack()                

    # Add a "next" button
    next_button = Button(songs_jesus_ransom_frame, text="Next Song", 
        command=songs_jesus_ransom, bg='gray90')
    next_button.pack(pady=15)
    
    # Create a button to answer
    song_jesus_ransom_answer_button = Button(songs_jesus_ransom_frame, 
        text="Answer", command=songs_jesus_ransom_answer)
    song_jesus_ransom_answer_button.pack(pady=15)
    
    # Add a button to clear the score if desired
    score_button = Button(songs_jesus_ransom_frame, text="Clear Score", 
        command=clscore, bg='gray90')
    score_button.pack(pady=15)
    
    # Create answer label for correct / incorrect
    global answer_label_songs_jesus_ransom
    answer_label_songs_jesus_ransom = Label(songs_jesus_ransom_frame, text="",
        font="Helvetica 20 bold", fg='DarkOrchid4', bg='gray90')
    answer_label_songs_jesus_ransom.pack(pady=15)            
   
    # Create score text for keeping track of score
    r_score_text = "Score: " + str(correct) + " out of " + str(total)
    
    # Create score label for keeping track of score
    global running_score_label
    running_score_label = Label(songs_jesus_ransom_frame, text=r_score_text, 
        font="Helvetica 20 bold", fg='DarkOrchid4', bg='gray90')
    running_score_label.pack(pady=10) 

def all_songs():
    
    # Hide previous frames
    hide_all_frames()
    all_songs_frame.pack(fill="both", expand=1)
    
    # my_label = Label(songs_jah_frame, text="Songs About Jah").pack()
    
    global show_all_songs
    show_all_songs = Label(all_songs_frame)
    show_all_songs.pack(pady=15)
    
    global all_songs_nums
    all_songs_nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
        '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', 
        '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', 
        '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', 
        '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', 
        '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', 
        '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', 
        '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', 
        '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', 
        '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', 
        '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', 
        '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', 
        '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', 
        '146', '147', '148', '149', '150', '151',
        ]
        
    global all_songs_titles
    all_songs_titles = {
        '1':"Jehovah's Attributes",
        '2':"Jehovah Is Your Name",
        '3':"Our Strength, Our Hope, Our Confidence",
        '4':"Jehovah Is My Shepherd",
        '5':"God's Wondrous Works",
        '6':"The Heavens Declare God's Glory",
        '7':"Jehovah, Our Strength",
        '8':"Jehovah Is Our Refuge",
        '9':"Jehovah Is Our King",
        '10':"Praise Jehovah Our God!",
        '11':"Creation Praises God",
        '12':"Great God, Jehovah",
        '13':"Christ Our Model",
        '14':"Praising Earth's New King",
        '15':"Praise Jehovah's Firstborn!",
        '16':"Praise Jah for His Son, the Anointed",
        '17':"I Want To",
        '18':"Grateful for the Ransom",
        '19':"The Lord's Evening Meal",
        '20':"You Gave Your Precious Son",
        '21':"Keep On Seeking First The Kingdom",
        '22':"The Kingdom Is in Place-Let It Come!", 
        '23':"Jehovah Begins His Rule", 
        '24':"Come to Jehovah's Mountain", 
        '25':"A Special Possession", 
        '26':"You Did It for Me", 
        '27':"The Revealing of God's Sons", 
        '28':"Gaining Jehovah's Friendship", 
        '29':"Living Up to Our Name", 
        '30':"My Father, My God and Friend", 
        '31':"Oh, Walk With God!", 
        '32':"Take Sides With Jehovah!", 
        '33':"Throw Your Burden on Jehovah", 
        '34':"Walking in Integrity", 
        '35':"Make Sure of the More Important Things", 
        '36':"We Guard Our Hearts", 
        '37':"Serving Jehovah Whole-Souled", 
        '38':"He Will Make You Strong", 
        '39':"Make a Good Name With God", 
        '40':"To Whom Do We Belong", 
        '41':"Please Hear My Prayer", 
        '42':"The Prayer of God's Servant", 
        '43':"A Prayer of Thanks", 
        '44':"A Prayer of the Lowly One", 
        '45':"The Meditation of My Heart", 
        '46':"We Thank You, Jehovah", 
        '47':"Pray to Jehovah Each Day", 
        '48':"Daily Walking With Jehovah", 
        '49':"Making Jehovah's Heart Glad", 
        '50':"My Prayer of Dedication", 
        '51':"To God We Are Dedicated", 
        '52':"Christian Dedication", 
        '53':"Preparing to Preach", 
        '54':"This Is the Way", 
        '55':"Fear Them Not!", 
        '56':"Make the Truth Your Own",
        '57':"Preaching to All Sorts of People", 
        '58':"Searching for Friends of Peace", 
        '59':"Praise Jah With Me", 
        '60':"It Means Their Life", 
        '61':"Forward You Witnesses!", 
        '62':"The New Song", 
        '63':"We're Jehovah's Witnesses!", 
        '64':"Sharing Joyfully in the Harvest", 
        '65':"Move Ahead!", 
        '66':"Declare the Good News", 
        '67':"Preach the Word", 
        '68':"Sowing Kingdom Seed", 
        '69':"Go Forward in Preaching the Kingdom", 
        '70':"Search Out Deserving Ones", 
        '71':"We Are Jehovah's Army!", 
        '72':"Making Known the Kingdom Truth", 
        '73':"Grand Us Boldness", 
        '74':"Join in the Kingdom Song!", 
        '75':"Here I Am! Send Me!", 
        '76':"How Does It Make You Feel?", 
        '77':"Light in a Darkened World", 
        '78':"Teaching the Word of God", 
        '79':"Teach Them to Stand Firm", 
        '80':"Taste and See That Jehovah Is Good", 
        '81':"The Life of a Pioneer", 
        '82':"Let Your Light Shine", 
        '83':"From House to House", 
        '84':"Reaching Out", 
        '85':"Welcome One Another", 
        '86':"We Must Be Taught", 
        '87':"Come! Be Refreshed", 
        '88':"Make Me Know Your Ways", 
        '89':"Listen, Obey, and Be Blessed", 
        '90':"Encourage One Another", 
        '91':"Our Labor of Love", 
        '92':"A Place Bearing Your Name", 
        '93':"Bless Our Meeting Together", 
        '94':"Grateful for God's Word", 
        '95':"The Light Gets Brighter", 
        '96':"God's Own Book - A Treasure", 
        '97':"Life Depends on God's Word", 
        '98':"The Scriptures - Inspired of God", 
        '99':"Myriads of Brothers", 
        '100':"Receive The With Hospitality", 
        '101':"Working Together in Unity", 
        '102':"Assist Those Who Are Weak", 
        '103':"Shepherds - Gifts in Men", 
        '104':"God's Gift of Holy Spirit", 
        '105':"God Is Love", 
        '106':"Cultivating the Quality of Love", 
        '107':"The Divine Pattern of Love", 
        '108':"God's Loyal Love", 
        '109':"Love Intensely From the Heart", 
        '110':"The Joy of Jehovah", 
        '111':"Our Reasons for Joy", 
        '112':"Jehovah, God of Peace", 
        '113':"Our Possession of Peace", 
        '114':"Exercise Patience", 
        '115':"Gratitude for Divine Patience", 
        '116':"The Power of Kindness", 
        '117':"The Quality of Goodness", 
        '118':"Give Us More Faith", 
        '119':"We Must Have Faith", 
        '120':"Imitate Christ's Mildness", 
        '121':"We Need Self-Control", 
        '122':"Be Steadfast, Immovable", 
        '123':"Loyally Submitting to Theocratic Order", 
        '124':"Ever Loyal", 
        '125':"Happy Are the Merciful", 
        '126':"Stay Awake, Stand Firm, Grow Mighty", 
        '127':"The Sort of Person I Should Be", 
        '128':"Enduring to the End", 
        '129':"We Will Keep Enduring", 
        '130':"Be Forgiving", 
        '131':"What God Has Yoked Together", 
        '132':"Now We Are One", 
        '133':"Worship Jehovah During Youth", 
        '134':"Children Are a Trust From God", 
        '135':"Jehovah's Warm Appeal: 'Be Wise, My Son'", 
        '136':"A Perfect Wage From Jehovah", 
        '137':"Faithful Women, Christian Sisters", 
        '138':"Beauty in Gray-Headedness", 
        '139':"See Yourself When All Is New", 
        '140':"Life Without End - At Last!", 
        '141':"The Miracle of Life", 
        '142':"Holding Fast to Our Hope", 
        '143':"Keep Working, Watching, and Waiting", 
        '144':"Keep Your Eyes on the Prize!", 
        '145':"God's Promise of Paradise", 
        '146':"Making All Things New", 
        '147':"Life Everlasting Is Promised", 
        '148':"Jehovah Provides Escape", 
        '149':"A Victory Song", 
        '150':"Seek God for Your Deliverance", 
        '151':"He Will Call",
        }
        
    # Generate Random Number
    global rand_num
    rand_num = randint(0, len(all_songs_nums)-1)
    
    global answer
    answer = all_songs_nums[rand_num]
    
    # Create empty answer list and counter
    answer_list = []
    count = 1
    
    # Generate four random song numbers
    while count < 5:
        rand_num = randint(0, len(all_songs_nums)-1)
        
        # If first selection, make it our answer
        if count == 1:
            answer = all_songs_nums[rand_num]
            global song_label
            song_label = Label(all_songs_frame, 
                text=("What is the title of Song Number " + 
                all_songs_nums[rand_num] + "?"), 
                font="Helvetica 18 bold", fg='DarkOrchid4', bg='gray90')
            song_label.pack(pady=15)
            
        # Add first selection to our list
        answer_list.append(all_songs_nums[rand_num])
        
        # Remove answer from list
        all_songs_nums.remove(all_songs_nums[rand_num])
        
        # Shuffle original list
        random.shuffle(all_songs_nums)
        
        count += 1
    
    # Play 10 second song segment for 'name that tune'    
    file_path = "music/"
    if len(answer) == 1:
        song_answer = '00' + str(answer)
        music_file = file_path + "sjjm_E_" + song_answer + ".mp3"
        # print(music_file)
        song = AudioSegment.from_mp3(music_file)
        ten_secs = song[:10000]
        play(ten_secs)
    elif len(answer) == 2:
        song_answer = '0' + str(answer)
        music_file = file_path + "sjjm_E_" + song_answer + ".mp3"
        # print(music_file)
        song = AudioSegment.from_mp3(music_file)
        ten_secs = song[:10000]
        play(ten_secs)
    else:
        music_file = file_path + "sjjm_E_" + answer + ".mp3"
        # print(music_file)
        song = AudioSegment.from_mp3(music_file)
        ten_secs = song[:10000]
        play(ten_secs)
            
    random.shuffle(answer_list)
        
    global all_songs_radio
    all_songs_radio = StringVar()
    all_songs_radio.set(all_songs_titles[answer_list[0]])
    
    all_songs_radio_button1 = Radiobutton(all_songs_frame, bg='gray90', 
        text=all_songs_titles[answer_list[0]], variable=all_songs_radio, 
        value=all_songs_titles[answer_list[0]]).pack()

    all_songs_radio_button1 = Radiobutton(all_songs_frame, bg='gray90', 
        text=all_songs_titles[answer_list[1]], variable=all_songs_radio, 
        value=all_songs_titles[answer_list[1]]).pack()
        
    all_songs_radio_button1 = Radiobutton(all_songs_frame, bg='gray90', 
        text=all_songs_titles[answer_list[2]], variable=all_songs_radio, 
        value=all_songs_titles[answer_list[2]]).pack()
        
    all_songs_radio_button1 = Radiobutton(all_songs_frame, bg='gray90', 
        text=all_songs_titles[answer_list[3]], variable=all_songs_radio, 
        value=all_songs_titles[answer_list[3]]).pack()                

    # Add a "next" button
    next_button = Button(all_songs_frame, text="Next Song", command=all_songs, 
        bg='gray90')
    next_button.pack(pady=15)
    
    # Create a button to answer
    all_songs_answer_button = Button(all_songs_frame, text="Answer",
        command=all_songs_answer, bg='gray90')
    all_songs_answer_button.pack(pady=15)
    
    # Add a button to clear the score if desired
    score_button = Button(all_songs_frame, text="Clear Score", command=clscore, 
        bg='gray90')
    score_button.pack(pady=15)
    
    # Create answer label for correct / incorrect
    global answer_label_all_songs
    answer_label_all_songs = Label(all_songs_frame, text="",
        font="Helvetica 20 bold", fg='DarkOrchid4', bg='gray90')
    answer_label_all_songs.pack(pady=15)
    
    # Create score text for keeping track of score
    r_score_text = "Score: " + str(correct) + " out of " + str(total)
    
    # Create score label for keeping track of score
    global running_score_label
    running_score_label = Label(all_songs_frame, text=r_score_text, 
        font="Helvetica 20 bold", fg='DarkOrchid4', bg='gray90')
    running_score_label.pack(pady=10)


def bible_books_quiz():
    
    # Hide previous frames
    hide_all_frames()
    bible_books_quiz_frame.pack(fill="both", expand=1)
    
        
    global show_bible_books_quiz
    show_bible_books_quiz = Label(bible_books_quiz_frame)
    show_bible_books_quiz.pack(pady=15)
    
    global bible_books_quiz_nums
    bible_books_quiz_nums = [
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', 
    '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', 
    '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', 
    '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', 
    '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', 
    '63', '64', '65', '66'
    ]
        
    global bible_books_quiz_titles
    bible_books_quiz_titles = {
    '1': 'Genesis', '2': 'Exodus', '3': 'Leviticus', '4': 'Numbers', 
    '5': 'Deuteronomy', '6': 'Joshua', '7': 'Judges', '8': 'Ruth', 
    '9': '1 Samuel', '10': '2 Samuel', 
    '11': '1 Kings', '12': '2 Kings', '13': '1 Chronicles', '14': '2 Chronicles', 
    '15': 'Ezra', '16': 'Nehemiah', '17': 'Esther', '18': 'Job', '19': 'Psalms', 
    '20': 'Proverbs', '21': 'Ecclesiastes', '22': 'Song of Solomon', 
    '23': 'Isaiah', '24': 'Jeremiah', '25': 'Lamentations', '26': 'Ezekiel', 
    '27': 'Daniel', '28': 'Hosea', '29': 'Joel', '30': 'Amos', 
    '31': 'Obadiah', '32': 'Jonah', '33': 'Micah', '34': 'Nahum', 
    '35': 'Habakkuk', '36': 'Zephaniah', '37': 'Haggai', '38': 'Zechariah', 
    '39': 'Malachi', '40': 'Matthew', '41': 'Mark', '42': 'Luke', '43': 'John', 
    '44': 'Acts', '45': 'Romans', '46': '1 Corinthians', '47': '2 Corinthians', 
    '48': 'Galatians', '49': 'Ephesians', '50': 'Philippians', '51': 'Colossians',
    '52': '1 Thessalonians', '53': '2 Thessalonians', '54': '1 Timothy', 
    '55': '2 Timothy', '56': 'Titus', '57': 'Philemon', '58': 'Hebrews', 
    '59': 'James', '60': '1 Peter', '61': '2 Peter', '62': '1 John', 
    '63': '2 John', '64': '3 John', '65': 'Jude', '66': 'Revelation', 
    }
        
    # Generate Random Number
    global rand_num
    rand_num = randint(0, len(bible_books_quiz_nums)-1)
    
    global answer
    answer = bible_books_quiz_nums[rand_num]
    
    # Create empty answer list and counter
    answer_list = []
    count = 1
    
    # Generate four random bible book numbers
    while count < 5:
        rand_num = randint(0, len(bible_books_quiz_nums)-1)
        
        # If first selection, make it our answer
        if count == 1:
            answer = bible_books_quiz_nums[rand_num]
            global bible_books_quiz_label
            bible_books_quiz_label = Label(bible_books_quiz_frame, 
                text=("What is the title of Bible Book Number " + 
                bible_books_quiz_nums[rand_num] + "?"), 
                font="Helvetica 18 bold", fg='DarkOrchid4', bg='gray90')
            bible_books_quiz_label.pack(pady=15)
            
        # Add first selection to our list
        answer_list.append(bible_books_quiz_nums[rand_num])
        
        # Remove answer from list
        bible_books_quiz_nums.remove(bible_books_quiz_nums[rand_num])
        
        # Shuffle original list
        random.shuffle(bible_books_quiz_nums)
        
        count += 1
        
    random.shuffle(answer_list)
    
    global bible_books_quiz_radio
    bible_books_quiz_radio = StringVar()
    bible_books_quiz_radio.set(bible_books_quiz_titles[answer_list[0]])
    
    bible_books_quiz_radio_button1 = Radiobutton(bible_books_quiz_frame,
        text=bible_books_quiz_titles[answer_list[0]], bg='gray90', 
        variable=bible_books_quiz_radio, 
         value=bible_books_quiz_titles[answer_list[0]]).pack()

    bible_books_quiz_radio_button1 = Radiobutton(bible_books_quiz_frame, 
        text=bible_books_quiz_titles[answer_list[1]], bg='gray90', 
        variable=bible_books_quiz_radio, 
         value=bible_books_quiz_titles[answer_list[1]]).pack()
        
    bible_books_quiz_radio_button1 = Radiobutton(bible_books_quiz_frame, 
        text=bible_books_quiz_titles[answer_list[2]], bg='gray90', 
        variable=bible_books_quiz_radio, 
         value=bible_books_quiz_titles[answer_list[2]]).pack()
        
    bible_books_quiz_radio_button1 = Radiobutton(bible_books_quiz_frame, 
        text=bible_books_quiz_titles[answer_list[3]], bg='gray90', 
        variable=bible_books_quiz_radio, 
         value=bible_books_quiz_titles[answer_list[3]]).pack()               

    # Add a "pass" or "next" button
    next_button = Button(bible_books_quiz_frame, text="Next Book", 
        command=bible_books_quiz)
    next_button.pack(pady=15)
    
    # Create a button to answer
    bible_books_quiz_answer_button = Button(bible_books_quiz_frame, 
        text="Answer", command=bible_books_quiz_answer)
    bible_books_quiz_answer_button.pack(pady=15)
    
    # Add a button to clear the score if desired
    score_button = Button(bible_books_quiz_frame, text="Clear Score", 
        command=clscore, bg='gray90')
    score_button.pack(pady=15)
    
    # Create answer label for correct / incorrect
    global answer_label_bible_books_quiz
    answer_label_bible_books_quiz = Label(bible_books_quiz_frame, text="",
        font="Helvetica 20 bold", fg='DarkOrchid4', bg='gray90')
    answer_label_bible_books_quiz.pack(pady=15)
    
    # Create score text for keeping track of score
    r_score_text = "Score: " + str(correct) + " out of " + str(total)
    
    # Create score label for keeping track of score
    global running_score_label
    running_score_label = Label(bible_books_quiz_frame, text=r_score_text, 
        font="Helvetica 20 bold", fg='DarkOrchid4', bg='gray90')
    running_score_label.pack(pady=10)


def bible_writers():
    
    # Hide previous frames
    hide_all_frames()
    bible_writers_frame.pack(fill="both", expand=1)
    
        
    global show_bible_writers
    show_bible_writers = Label(bible_writers_frame)
    show_bible_writers.pack(pady=15)
    
    global bible_writers_nums
    bible_writers_nums = [
    'Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy', 'Joshua', 
    'Judges', 'Ruth', '1 Samuel', '2 Samuel', '1 Kings', '2 Kings', 
    '1 Chronicles', '2 Chronicles', 'Ezra', 'Nehemiah', 'Esther', 'Job', 
    'Psalms', 'Proverbs', 'Ecclesiastes', 'Song of Solomon', 'Isaiah', 
    'Jeremiah', 'Lamentations', 'Ezekiel', 'Daniel', 'Hosea', 'Joel', 
    'Amos', 'Obadiah', 'Jonah', 'Micah', 'Nahum', 'Habakkuk', 'Zephaniah',
    'Haggai', 'Zechariah', 'Malachi', 'Matthew', 'Mark', 'Luke', 'John', 'Acts',
    'Romans', '1 Corinthians', '2 Corinthians', 'Galatians', 'Ephesians', 
    'Philippians', 'Colossians', '1 Thessalonians', '2 Thessalonians', 
    '1 Timothy', '2 Timothy', 'Titus', 'Philemon', 'Hebrews', 'James', 
    '1 Peter', '2 Peter', '1 John', '2 John', '3 John', 'Jude', 'Revelation',
    ]
        
    global bible_writers_titles
    bible_writers_titles = {
    'Genesis': "Moses", 
    'Exodus': "Moses", 
    'Leviticus': "Moses", 
    'Numbers': "Moses",
    'Deuteronomy': "Moses", 
    'Joshua': "Joshua", 
    'Judges': "Samuel", 
    'Ruth': "Samuel", 
    '1 Samuel': "Samuel, Gad, Nathan", 
    '2 Samuel':  "Gad, Nathan", 
    '1 Kings': "Jeremiah", 
    '2 Kings': "Jeremiah", 
    '1 Chronicles': "Ezra", 
    '2 Chronicles': "Ezra", 
    'Ezra': "Ezra", 
    'Nehemiah': "Nehemiah", 
    'Esther': "Mordecai", 
    'Job': "Moses", 
    'Psalms': "David and Others", 
    'Proverbs': "Solomon, Agur, Lemuel", 
    'Ecclesiastes': "Solomon", 
    'Song of Solomon': "Solomon", 
    'Isaiah': "Isaiah", 
    'Jeremiah': "Jeremiah", 
    'Lamentations': "Jeremiah", 
    'Ezekiel': "Ezekiel", 
    'Daniel': "Daniel", 
    'Hosea': "Hosea", 
    'Joel': "Joel", 
    'Amos': "Amos", 
    'Obadiah': "Obadiah", 
    'Jonah': "Jonah", 
    'Micah': "Micah", 
    'Nahum': "Nahum", 
    'Habakkuk': "Habakkuk", 
    'Zephaniah': "Zephaniah", 
    'Haggai': "Haggai", 
    'Zechariah': "Zechariah", 
    'Malachi': "Malachi", 
    'Matthew': "Matthew", 
    'Mark': "Mark", 
    'Luke': "Luke", 
    'John': "Apostle John", 
    'Acts': "Luke", 
    'Romans': "Paul", 
    '1 Corinthians': "Paul", 
    '2 Corinthians': "Paul", 
    'Galatians': "Paul", 
    'Ephesians': "Paul", 
    'Philippians': "Paul", 
    'Colossians': "Paul",
    '1 Thessalonians': "Paul", 
    '2 Thessalonians': "Paul", 
    '1 Timothy': "Paul", 
    '2 Timothy': "Paul", 
    'Titus': "Paul", 
    'Philemon': "Paul", 
    'Hebrews': "Paul", 
    'James': "James, Jesus' Brother", 
    '1 Peter': "Peter", 
    '2 Peter': "Peter", 
    '1 John': "Apostle John", 
    '2 John': "Apostle John", 
    '3 John': "Apostle John", 
    'Jude': "Jude, Jesus Brother", 
    'Revelation': "Apostle John", 
    }
        
    # Generate Random Number
    global rand_num
    rand_num = randint(0, len(bible_writers_nums)-1)
    
    global answer
    answer = bible_writers_nums[rand_num]
    
    # Create empty answer list and counter
    answer_list = []
    count = 1
    
    # Generate four random bible book numbers
    while count < 5:
        rand_num = randint(0, len(bible_writers_nums)-1)
        
        # If first selection, make it our answer
        if count == 1:
            answer = bible_writers_nums[rand_num]
            global bible_writers_label
            bible_writers_label = Label(bible_writers_frame, 
                text=("Who is the author of this book: " + 
                bible_writers_nums[rand_num] + "?"), 
                font="Helvetica 18 bold", fg='DarkOrchid4', bg='gray90')
            bible_writers_label.pack(pady=15)
            
        # Add first selection to our list
        answer_list.append(bible_writers_nums[rand_num])
        
        # Remove answer from list
        bible_writers_nums.remove(bible_writers_nums[rand_num])
        
        # Shuffle original list
        random.shuffle(bible_writers_nums)
        
        count += 1
        
    random.shuffle(answer_list)
    
    global bible_writers_radio
    bible_writers_radio = StringVar()
    bible_writers_radio.set(bible_writers_titles[answer_list[0]])
    
    bible_writers_radio_button1 = Radiobutton(bible_writers_frame, 
        text=bible_writers_titles[answer_list[0]], bg='gray90', 
        variable=bible_writers_radio, 
         value=bible_writers_titles[answer_list[0]]).pack()

    bible_writers_radio_button2 = Radiobutton(bible_writers_frame, 
        text=bible_writers_titles[answer_list[1]], bg='gray90', 
        variable=bible_writers_radio, 
         value=bible_writers_titles[answer_list[1]]).pack()
        
    bible_writers_radio_button3 = Radiobutton(bible_writers_frame, 
        text=bible_writers_titles[answer_list[2]], bg='gray90', 
        variable=bible_writers_radio, 
         value=bible_writers_titles[answer_list[2]]).pack()
        
    bible_writers_radio_button4 = Radiobutton(bible_writers_frame, 
        text=bible_writers_titles[answer_list[3]], bg='gray90', 
        variable=bible_writers_radio, 
         value=bible_writers_titles[answer_list[3]]).pack()               

    # Add a "pass" or "next" button
    next_button = Button(bible_writers_frame, text="Next Book", bg='gray90', 
        command=bible_writers)
    next_button.pack(pady=15)
    
    # Create a button to answer
    bible_writers_answer_button = Button(bible_writers_frame, bg='gray90', 
        text="Answer", command=bible_writers_answer)
    bible_writers_answer_button.pack(pady=15)
    
    # Add a button to clear the score if desired
    score_button = Button(bible_writers_frame, text="Clear Score", 
        command=clscore, bg='gray90')
    score_button.pack(pady=15)
    
    # Create answer label for correct / incorrect
    global answer_label_bible_writers
    answer_label_bible_writers = Label(bible_writers_frame, text="",
        font="Helvetica 18", bg='gray90', fg='DarkOrchid4')
    answer_label_bible_writers.pack(pady=15)
    
    # Create score text for keeping track of score
    r_score_text = "Score: " + str(correct) + " out of " + str(total)
    
    # Create score label for keeping track of score
    global running_score_label
    running_score_label = Label(bible_writers_frame, text=r_score_text, 
        font="Helvetica 20 bold", fg='DarkOrchid4', bg='gray90')
    running_score_label.pack(pady=10)
    

# Create function to pull scriptures from list at random with text images
def scrips():
    
    # Hide previous frames
    hide_all_frames()
    scrips_frame.pack(fill="both", expand=1)
    
    # Create global variables for labels referenced by other functions   
    global show_scrips
    show_scrips = Label(scrips_frame)
    show_scrips.pack(pady=15)
    
    # Create global list of scripture file names
    global scrips_files
    scrips_files = [
        '1cor1528', '2pet121', 'gal65', 'isa428', 'matt2414', 'prov356', 'rev2134',
        '1john31920', 'gen11', 'jas113', 'matt2478', 'ps1003', 'rom1013',
        '1john38', '2tim316', 'gen2218', 'jas15', 'matt251112', 'ps113', 'rom120',
        '1john519', 'acts83031', 'gen315', 'job267', 'matt281920', 'ps2218',
        'rom1620', '1pet57', 'dan244', 'heb102425', 'job3410', 'matt610',
        'ps8318', '1thess213', 'dan71', 'heb34', 'josh18', 'micah52',
        'rev1115', '1tim_3_1-5', 'eccl17', 'isa4022', 'luke2111', 'neh88', 'rev129',
        '1tim415', 'ex244', 'isa4026', 'mark137', 'prov1320', 'rev202',
        'prov_14_30', 'acts_20_35', 'eph_5_33', 'eccl_5_10', 'jas_1_19',
        'isa_33_24', 'isa_35_5', 'john_5_28_29', 'deut_32_4', 'jer_32_17',
        'rom_11_33', '1john_4_8', 'matt_15_32', 'luke_24_19', 'luke_22_27',
        'titus_1_4', 'matt_28_5_6', 'luke_24_51', 'acts_2_32', '1cor_15_4-6',
        'psalm_91_9_11', 'psalm_103_20', 'rev_19_10', 'isa_25_8', 'ezek_33_11',
        'rom_6_23', 'isa_55_11', 'eccl_8_9', 'rom_5_12', '2pet_3_9', 'gen_3_1',
        'gen_3_4', 'gen_3_5', 'matt_20_28', '1cor_15_26', 'col_1_14', 'psalm_72_8',
        'dan_7_14', 'matt_28_18', 'psalm_37_10', 'psalm_72_16', 'rev_5_10',
        'isa_9_7', 'matt_13_19', 'luke_17_20_21', 'isa_30_15', 'psalm_13_2',
        '1john_4_7', 'rev_7_10', 'rom_12_10', 'acts_24_15', '1cor_15_55',
        '1cor_15_29', 'prov_24_16', 'psalm_34_18', 'psalm_55_22', 'heb_13_5',
        '2cor_13_11', 'prov_4_25', '2cor_3_3', '1tim_4_16', 'zech_4_6', 'luke_2_52',
        'luke_5_10', 'eccl_11_6', '2chron_14_6', 'psalm_68_11', '1tim_6_20',
        'eccl_5_8', 'heb_11_10', 'micah_6_8', '1cor_12_12', '1cor_12_21',
        'rom_12_3', '2tim_3_14', '2cor_12_10', '3john_4', 'psalm_135_13',
        'psalm_86_11_12', 'ezek_34_11', 'mal_3_7', 'dan_11_40', 'dan_11_45',
        'psalm_40_5', '2cor_4_18', 'joel_1_6', 'john_4_35', 'john_7_24',
        'john_15_15', '2tim_4_7', 'acts_8_36', '1peter_3_21', '1peter_1_22',
        'matt_6_9', '1john_4_19', 'rom_14_19', 'psalm_94_19', 'col_4_11',
        'psalm_136_23', 'rom_8_16', 'zech_8_23', 'mark_6_31', 'lev_5_10',
        'psalm_9_10', 'psalm_127_3', 'prov_17_17', 'phil_4_13', 'eph_6_16',
        '2cor_8_11', '1cor_15_58', 'psalm_31_23', 'phil_2_13', 'nah_1_2',
        'psalm_138_6', 'rev_16_16', 'heb_12_9', 'matt_11_28', 'rev_7_9',
        '2cor_4_16', 'phil_1_9', 'heb_6_10', '2tim_3_12', 'acts_4_19_20',
        '1cor_9_22', 'col_2_8', '2cor_10_5', '1sam_1_15', '1pet_3_8',
        'gal_6_2', '2cor_1_3-4', '1cor_3_19', 'phil_1_10', '2tim_4_5', 'phil_4_7',
        '1john_4_6', 'eph_6_12', 'acts_8_38', 'matt_17_5', 'mark_6_34', 'job_27_5',
        'zeph_2_3', 'col_3_15', 'psalm_33_5', 'isa_41_10', 'psalm_22_22',
        'prov_4_23', 'matt_26_26-28', '1cor_11_26', 'luke_23_43', 'mark_10_9',
        'psalm_103_5', 'psalm_16_11', 'prov_23_23', 'psalm_86_11', 'rom_12_2',
        'zech_8_16', 'psalm_119_159-160', 'matt_23_10', 'psalm_131_2', 'john_4_34',
        '1cor_8_1', 'psalm_144_15', 'psalm_103_14', 'psalm_41_1', 'prov_18_13',
        '1cor_3_9', 'psalm_123_1', 'deut_10_20', 'psalm_33_12', 
        'john_17_20-21', 'psalm_119_99', 'matt_5_16', 'luke_8_15', 'john_15_8',
        '2cor_2_11', 'eph_6_11', 'john_8_36', '2cor_3_17', 'prov_16_3',
        'acts_22_16', '1pet_4_9', 'heb_12_6', 'prov_8_32-33', 'ezek_14_14',
        'prov_28_5', 'rom_15_5', 'gal_5_16', 'isa_40_31', 'psalm_133_1',
        '1chron_29_13', 'mal_3_18', 'john_11_11', '1cor_15_45', '2tim_3_15',
        'phil_2_12', 'psalm_147_1', 'psalm_34_22', 'zech_7_9',
    ]

    # Create global list of scripture titles to match names
    global scrips_text
    scrips_text = {
        '1cor1528': "1 Corinthians 15:28", '2pet121': "2 Peter 1:21",
        'gal65': "Galatians 6:5", 'isa428': "Isaiah  42:8",
        'matt2414': "Matthew 24:14", 'prov356': "Proverbs 3:5, 6",
        'rev2134': "Revelation 21:3, 4", '1john31920': "1 John 3:19, 20",
        'gen11': "Genesis 1:1", 'jas113': "James 1:13",
        'matt2478': "Matthew 24:7, 8", 'ps1003': "Psalm 100:3",
        'rom1013': "Romans 10:13", '1john38': "1 John 3:8",
        '2tim316': "2 Timothy 3:16", 'gen2218': "Genesis 22:18",
        'jas15': "James 1:5", 'matt251112': "Matthew 25:11, 12",
        'ps113': "Psalm 1:1-3", 'rom120': "Romans 1:20",
        '1john519': "1 John 5:19", 'acts83031': "Acts 8:30, 31",
        'gen315': "Genesis 3:15", 'job267': "Job 26:7",
        'matt281920': "Matthew 28:19, 20", 'ps2218': "Psalm 22:18",
        'rom1620': "Romans 16:20", '1pet57': "1 Peter 5:8",
        'dan244': "Daniel 2:44", 'heb102425': "Hebrews 10:24, 25",
        'job3410': "Job 34:10", 'matt610': "Matthew 6:10",
        'ps8318': "Psalm 83:19",
        '1thess213': "1 Thessalonians 2:13", 'dan71': "Daniel 7:1",
        'heb34': "Hebrews 3:4", 'josh18': "Joshua 1:8", 'micah52': "Micah 5:2",
        'rev1115': "Revelation 11:15", '1tim_3_1-5': "1 Timothy 3:1-5",
        'eccl17': "Ecclesiastes 1:7", 'isa4022': "Isaiah 40:22",
        'luke2111': "Luke 21:11", 'neh88': "Nehemiah 8:8",
        'rev129': "Revelation 12:9", '1tim415': "1 Timothy 4:15",
        'ex244': "Exodus 24:4", 'isa4026': "Isaiah 40:26", 'mark137': "Mark 13:7",
        'prov1320': "Proverbs 13:20", 'rev202': "Revelation 20:2",
        'prov_14_30': "Proverbs 14:30", 'acts_20_35': "Acts 20:35",
        'eph_5_33': "Ephesians 5:33", 'eccl_5_10': "Ecclesiastes 5:10",
        'jas_1_19': "James 1:19", 'isa_33_24': "Isaiah 33:24",
        'isa_35_5': "Isaiah 35:5", 'john_5_28_29': "John 5:28, 29",
        'deut_32_4': "Deuteronomy 32:4", 'jer_32_17': "Jeremiah 32:17",
        'rom_11_33': "Romans 11:33", '1john_4_8': "1 John 4:8",
        'matt_15_32': "Matthew 15:32", 'luke_24_19': "Luke 24:19",
        'luke_22_27': "Luke 22:27", 'titus_1_4': "Titus 1:4",
        'matt_28_5_6': "Matthew 28:5, 6", 'luke_24_51': "Luke 24:51",
        'acts_2_32': "Acts 2:32", '1cor_15_4-6': "1 Corinthians 15:4-6",
        'psalm_91_9_11': "Psalm 91:9, 11", 'psalm_103_20': "Psalm 103:20",
        'rev_19_10': "Revelation 19:10", 'isa_25_8': "Isaiah 25:8",
        'ezek_33_11': "Ezekiel 33:11", 'rom_6_23': "Romans 6:23",
        'isa_55_11': "Isaiah 55:11", 'eccl_8_9': "Ecclesiastes 8:9",
        'rom_5_12': "Romans 5:12", '2pet_3_9': "2 Peter 3:9",
        'gen_3_1': "Genesis 3:1", 'gen_3_4': "Genesis 3:4",
        'gen_3_5': "Genesis 3:5", 'matt_20_28': "Matthew 20:28",
        '1cor_15_26': "1 Corinthians 15:26", 'col_1_14': "Colossians 1:14",
        'psalm_72_8': "Psalm 72:8", 'dan_7_14': "Daniel 7:14",
        'matt_28_18': "Matthew 28:18", 'psalm_37_10': "Psalm 37:10",
        'psalm_72_16': "Psalm 72:16", 'rev_5_10': "Revelation 5:10",
        'isa_9_7': "Isaiah 9:7", 'matt_13_19': "Matthew 13:19",
        'luke_17_20_21': "Luke 17:20, 21", 'isa_30_15': "Isaiah 30:15",
        'psalm_13_2': "Psalm 13:2", '1john_4_7': "1 John 4:7",
        'rev_7_10': "Revelation 7:10", 'rom_12_10': "Romans 12:10",
        'acts_24_15': "Acts 24:15", '1cor_15_55': "1 Corinthians 15:55",
        '1cor_15_29': "1 Corinthians 15:29", 'prov_24_16': "Proverbs 24:16",
        'psalm_34_18': "Psalm 34:18", 'psalm_55_22': "Psalm 55:22",
        'heb_13_5': "Hebrews 13:5", '2cor_13_11': "2 Corinthians 13:11",
        'prov_4_25': "Proverbs 4:25", '2cor_3_3': "2 Corinthians 3:3",
        '1tim_4_16': "1 Timothy 4:16", 'zech_4_6': "Zechariah 4:6",
        'luke_2_52': "Luke 2:52", 'luke_5_10': "Luke 5:10",
        'eccl_11_6': "Ecclesiastes 11:6", '2chron_14_6': "2 Chronicles 14:6",
        'psalm_68_11': "Psalm 68:11", '1tim_6_20': "1 Timothy 6:20",
        'eccl_5_8': "Ecclesiastes 5:8", 'heb_11_10': "Hebrews 11:10",
        'micah_6_8': "Micah 6:8", '1cor_12_12': "1 Corinthians 12:12",
        '1cor_12_21': "1 Corinthians 12:21", 'rom_12_3': "Romans 12:3",
        '2tim_3_14': "2 Timothy 3:14", '2cor_12_10': "2 Corinthians 12:10",
        '3john_4': "3 John: 4", 'psalm_135_13': "Psalm 135:13",
        'psalm_86_11_12': "Psalm 86:11, 12", 'ezek_34_11': "Ezekiel 34:11",
        'mal_3_7': "Malachi 3:7", 'dan_11_40': "Daniel 11:40",
        'dan_11_45': "Daniel 11:45", 'psalm_40_5': "Psalm 40:5",
        '2cor_4_18': "2 Corinthians 4:18", 'joel_1_6': "Joel 1:6",
        'john_4_35': "John 4:35", 'john_7_24': "John 7:24",
        'john_15_15': "John 15:15", '2tim_4_7': "2 Timothy 4:7",
        'acts_8_36': "Acts 8:36", '1peter_3_21': "1 Peter 3:21",
        '1peter_1_22': "1 Peter 1:22", 'matt_6_9': "Matthew 6:9",
        '1john_4_19': "1 John 4:19", 'rom_14_19': "Romans 14:19",
        'psalm_94_19': "Psalm 94:19", 'col_4_11': "Colossians 4:11",
        'psalm_136_23': "Psalm 136:23", 'rom_8_16': "Romans 8:16",
        'zech_8_23': "Zechariah 8:23", 'mark_6_31': "Mark 6:31",
        'lev_5_10': "Leviticus 5:10", 'psalm_9_10': "Psalm 9:10",
        'psalm_127_3': "Psalm 127:3", 'prov_17_17': "Proverbs 17:17",
        'phil_4_13': "Philippians 4:13", 'eph_6_16': "Ephesians 6:16",
        '2cor_8_11': "2 Corinthians 8:11", '1cor_15_58': "1 Corinthians 15:58",
        'psalm_31_23': "Psalm 31:23", 'phil_2_13': "Philippians 2:13",
        'nah_1_2': "Nahum 1:2", 'psalm_138_6': "Psalm 138:6",
        'rev_16_16': "Revelation 16:16", 'heb_12_9': "Hebrews 12:9",
        'matt_11_28': "Matthew 11:28", 'rev_7_9': "Revelation 7:9",
        '2cor_4_16': "2 Corinthians 4:16", 'phil_1_9': "Philippians 1:9",
        'heb_6_10': "Hebrews 6:10", '2tim_3_12': "2 Timothy 3:12",
        'acts_4_19_20': "Acts 4:19, 20", '1cor_9_22': "1 Corinthians 9:22",
        'col_2_8': "Colossians 2:8", '2cor_10_5': "2 Corinthians 10:5",
        '1sam_1_15': "1 Samuel 1:15", '1pet_3_8': "1 Peter 3:8",
        'gal_6_2': "Galatians 6:2", '2cor_1_3-4': "2 Corinthians 1:3, 4",
        '1cor_3_19': "1 Corinthians 3:19", 'phil_1_10': "Philippians 1:10",
        '2tim_4_5': "2 Timothy 4:5", 'phil_4_7': "Philippians 4:7",
        '1john_4_6': "1 John 4:6", 'eph_6_12': "Ephesians 6:12",
        'acts_8_38': "Acts 8:38", 'matt_17_5': "Matthew 17:5",
        'mark_6_34': "Mark 6:34", 'job_27_5': "Job 27:5",
        'zeph_2_3': "Zephaniah 2:3", 'col_3_15': "Colossians 3:15",
        'psalm_33_5': "Psalm 33:5", 'isa_41_10': "Isaiah 41:10",
        'psalm_22_22': "Psalm 22:22", 'prov_4_23': "Proverbs 4:23",
        'matt_26_26-28': "Matthew 26:26-28", '1cor_11_26': "1 Corinthians 11:26",
        'luke_23_43': "Luke 23:43", 'mark_10_9': "Mark 10:9",
        'psalm_103_5': "Psalm 103:5", 'psalm_16_11': "Psalm 16:11",
        'prov_23_23': "Proverbs 23:23", 'psalm_86_11': "Psalm 86:11",
        'rom_12_2': "Romans 12:2", 'zech_8_16': "Zechariah 8:16",
        'psalm_119_159-160': "Psalm 119:159-160", 'matt_23_10': "Matthew 23:10",
        'psalm_131_2': "Psalm 131:2", 'john_4_34': "John 4:34",
        '1cor_8_1': "1 Corinthians 8:1", 'psalm_144_15': "Psalm 144:15",
        'psalm_103_14': "Psalm 103:14", 'psalm_41_1': "Psalm 41:1",
        'prov_18_13': "Proverbs 18:13", '1cor_3_9': "1 Corinthians 3:9",
        'psalm_123_1': "Psalm 123:1", 'deut_10_20': "Deuteronomy 10:20",
        'psalm_33_12': "Psalm 33:12", 
        'john_17_20-21': "John 17:20, 21", 'psalm_119_99': "Psalm 119:99",
        'matt_5_16': "Matthew 5:16", 'luke_8_15': "Luke 8:15",
        'john_15_8': "John 15:8", '2cor_2_11': "2 Corinthians 2:11",
        'eph_6_11': "Ephesians 6:11", 'john_8_36': "John 8:36",
        '2cor_3_17': "2 Corinthians 3:17", 'prov_16_3': "Proverbs 16:3",
        'acts_22_16': "Acts 22:16", '1pet_4_9': "1 Peter 4:9",
        'heb_12_6': "Hebrews 12:6", 'prov_8_32-33': "Proverbs 8:32-33",
        'ezek_14_14': "Ezekiel 14:14", 'prov_28_5': "Proverbs 28:5",
        'rom_15_5': "Romans 15:5", 'gal_5_16': "Galatians 5:16",
        'isa_40_31': "Isaiah 40:31", 'psalm_133_1': "Psalm 133:1",
        '1chron_29_13': "1 Chronicles 29:13", 'mal_3_18': "Malachi 3:18",
        'john_11_11': "John 11:11", '1cor_15_45': "1 Corinthians 15:45",
        '2tim_3_15': "2 Timothy 3:15", 'phil_2_12': "Philippians 2:12",
        'psalm_147_1': "Psalm 147:1", 'psalm_34_22': "Psalm 34:22",
        'zech_7_9': "Zechariah 7:9",
    }

    # Generate Random Number
    global rand_num
    rand_num = randint(0, len(scrips_files) - 1)

    # Create global variable to keep and track answers
    global answer
    answer = scrips_files[rand_num]

    # Create empty answer list and counter
    answer_list = []
    count = 1

    # Generate four random scripture numbers
    while count < 5:
        rand_num = randint(0, len(scrips_files) - 1)

        # If first selection, make it our answer
        if count == 1:
            answer = scrips_files[rand_num]
            global scrip_image
            scrip = "images/" + scrips_files[rand_num] + ".png"
            scrip_image = ImageTk.PhotoImage(Image.open(scrip))
            show_scrips.config(image=scrip_image)

        # Add first selection to our list
        answer_list.append(scrips_files[rand_num])

        # Remove answer from list
        scrips_files.remove(scrips_files[rand_num])

        # Shuffle original list
        random.shuffle(scrips_files)

        count += 1
    
    # Re-Shuffle list for randomy randomness
    random.shuffle(answer_list)

    # Create tkinter radio buttons for possible answers chosen at random above
    global scrips_radio
    scrips_radio = StringVar()
    scrips_radio.set(scrips_text[answer_list[0]])

    scrips_radio_button1 = Radiobutton(scrips_frame, bg='gray90', 
        text=scrips_text[answer_list[0]], variable=scrips_radio,
        value=scrips_text[answer_list[0]]).pack()

    scrips_radio_button2 = Radiobutton(scrips_frame, bg='gray90', 
        text=scrips_text[answer_list[1]], variable=scrips_radio, 
        value=scrips_text[answer_list[1]]).pack()

    scrips_radio_button3 = Radiobutton(scrips_frame, bg='gray90', 
        text=scrips_text[answer_list[2]], variable=scrips_radio, 
        value=scrips_text[answer_list[2]]).pack()

    scrips_radio_button4 = Radiobutton(scrips_frame, bg='gray90', 
        text=scrips_text[answer_list[3]], variable=scrips_radio, 
        value=scrips_text[answer_list[3]]).pack()

    # Add a "next" button
    next_button = Button(scrips_frame, text="Next Scripture", command=scrips, 
        bg='gray90')
    next_button.pack(pady=15)

    # Create a button to trigger answer function
    scrips_answer_button = Button(scrips_frame, text="Answer", 
        command=scrips_answer, bg='gray90')
    scrips_answer_button.pack(pady=15)
    
    # Add a button to clear the score if desired
    score_button = Button(scrips_frame, text="Clear Score", command=clscore, 
        bg='gray90')
    score_button.pack(pady=15)
    

    # Create answer label for correct / incorrect answers
    global answer_label_scrips
    answer_label_scrips = Label(scrips_frame, text="", 
        font="Helvetica 20 bold", fg='DarkOrchid4', bg='gray90')
    answer_label_scrips.pack(pady=15)

    # Create score text for keeping track of score
    r_score_text = "Score: " + str(correct) + " out of " + str(total)
    
    # Create score label for keeping track of score
    global running_score_label
    running_score_label = Label(scrips_frame, text=r_score_text, 
        font="Helvetica 20 bold", fg='DarkOrchid4', bg='gray90')
    running_score_label.pack(pady=10) 


# Create function for clearing the score
def clscore():
    
    # Reference global variables for score tracking
    global correct
    global total
    correct = 0
    total = 0  
    
    # Create score text and update label
    score_text = "Score: " + str(correct) + " out of " + str(total)
    running_score_label.config(text=score_text)


# Create function to hide all previous frames
def hide_all_frames():
    # Loop through and destroy all children in previous frames
    for widget in master_frame.winfo_children():
        widget.destroy()
        
    for widget in songs_jah_frame.winfo_children():
        widget.destroy()
        
    for widget in songs_jesus_ransom_frame.winfo_children():
        widget.destroy()
        
    for widget in all_songs_frame.winfo_children():
        widget.destroy()
        
    for widget in bible_books_quiz_frame.winfo_children():
        widget.destroy()
        
    for widget in bible_writers_frame.winfo_children():
        widget.destroy()
        
    for widget in scrips_frame.winfo_children():
        widget.destroy()       
        
            
    master_frame.pack_forget()
    songs_jah_frame.pack_forget()
    songs_jesus_ransom_frame.pack_forget()
    all_songs_frame.pack_forget()
    bible_books_quiz_frame.pack_forget()
    bible_writers_frame.pack_forget()
    scrips_frame.pack_forget()
        

# Create Bible Quiz Master Menu Items
master_menu = Menu(my_menu)
my_menu.add_cascade(label="Main Menu", menu=master_menu)
master_menu.add_command(label="Clear Window", command=hide_all_frames)
master_menu.add_separator()
master_menu.add_command(label="Exit", command=root.quit)

# Create Bible Quiz Scripture Menu Items
scrip_menu = Menu(my_menu)
my_menu.add_cascade(label="Scriptures", menu=scrip_menu)
scrip_menu.add_command(label="Bible Books and Numbers", 
    command=bible_books_quiz)
scrip_menu.add_command(label="Bible Books and Writers",
    command=bible_writers)
scrip_menu.add_command(label="Scriptural Texts", command=scrips)


song_menu = Menu(my_menu)
my_menu.add_cascade(label="Songs", menu=song_menu)
song_menu.add_command(label="Songs About Jehovah", command=songs_jah)
song_menu.add_command(label="Songs About Jesus Ransom", 
    command=songs_jesus_ransom)
song_menu.add_command(label="All Kingdom Songs",
    command=all_songs)


# Create Frames
master_frame = Frame(root, width=800, height=800, bg='gray90')

bible_books_quiz_frame = Frame(root, width=800, height=800, bg='gray90')
bible_writers_frame = Frame(root, width=800, height=800, bg='gray90')
scrips_frame = Frame(root, width=800, height=800, bg='gray90')

songs_jah_frame = Frame(root, width=800, height=800, bg='gray90')
songs_jesus_ransom_frame = Frame(root, width=800, height=800, bg='gray90')
all_songs_frame = Frame(root, width=800, height=800, bg='gray90')


# Allow main program to run
root.mainloop()
