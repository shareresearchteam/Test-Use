#TTS stuff 
# I had do use these commands to download the espeak
# sudo dpkg --configure -a     <- used that because the next two didnt work at first
# sudo apt update 
# sudo apt install espeak

import os 

voice = "en-us"   #Language/voice control 
speed = 150          #Speech speed    
#response_file = "response.wav"   #output to wav -> not tested 
 
def TTS_from_file(file_path):
    with open(file_path, "r") as file:
        text = file.read()
    os.system(f"espeak -v{voice} -s{speed} '{text}'")
    #os.system(f"'espeak -v{voice} -s{speed} '{text}' -w {response_file}")   #I think this makes the response a wav file but havent tested it yet


TTS_from_file("sample_text.txt") # replace with response.txt when in use