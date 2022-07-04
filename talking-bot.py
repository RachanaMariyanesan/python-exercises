import pyttsx3
import wikipedia #wikipedia.search("Barack")

engine = pyttsx3.init()
 
 #Voice
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk_function(text):
    engine.say(text)
    engine.runAndWait()

while True:

    user_input=input("User: ")  
    user_input= user_input.lower() 

    if  user_input == "hello":
        talk_function("Hey , I am Hermione , How are you ");

    elif user_input == "hi":
        talk_function("Congratulations , Congratulations , Congratulations , Important things must be said three time  ,  Hey HOST , you have successfully activated the bot")

    elif  user_input == "i am fine":   
        talk_function("Oh dear! Good to hear it");
    
    elif user_input =="thank you":
        talk_function("Do not mention dear");

    elif user_input == "hey how are you":
        talk_function("I am fine");

    elif user_input == "can you tell me your name":
        talk_function("My name is Talkingbot"); 

    elif  user_input == "can you tell me my name":   
        talk_function("It is Rachana Mariyanesan");

    elif  user_input == "can you tell me my mother's name":   
        talk_function("It is Prashanthy Mariyanesan");

    elif  user_input == "can you tell me my father's name":   
        talk_function("It is Kanesamoorthy Mariyanesan");

    elif  user_input == "can you tell me my sisters' name":   
        talk_function("It is Raksha Mariyanesan and Prehrnna Mariyanesan");

    elif  user_input == "can you tell me my brother's name":   
       talk_function("It is Ananthavarnan Dineshraj");

    elif  user_input == "can you tell me my pet's name":   
        talk_function("It's Moofy");

    elif  user_input == "can you tell the name of my favorite novel":   
        talk_function("It's Harry Potter");

    elif  user_input == "can you tell me the name of my favourite actor":   
        talk_function("It's Xiao Zhan");

    elif  user_input == "can you me who is janarthani":   
        talk_function("Janarthani is your chiththi");

    elif  user_input == "can you tell me my age":   
        talk_function("It's 20");

    elif user_input == "can you tell me when's my birthday":
        talk_function("It's at 23 may 2002");

    elif user_input == "can you tell me my favourite music band":
        talk_function("It's BTS"); 

    elif user_input == "do you like hp":
        talk_function("Yes I do");

    elif user_input == "tell me the author of hp":
        talk_function("It's J K Rowlings");

    elif user_input == "there are how many series in hp":
        talk_function("There are eight series in Harry Potter");

    elif user_input == "are you a potterhead":
        talk_function("Yes I am"); 

    elif user_input == "which one is your favorite charactor in hp":
        talk_function("It's Draco Malfoy");

    elif user_input == "there are how many houses in hogwarts":
        talk_function("There are four houses in Hogwarts");  

    elif user_input == "list out the houses in hogwarts":
        talk_function("Griffindor,Slytherin,Ravenclaw,Hufflepuffs"); 

    elif user_input == "why is it called hogwarts":
        talk_function("It's a popular wizarding theory that Rowena Ravenclaw came up with the name of Hogwarts after dreaming of a warty hog that led her to a cliff by a lake");

    elif user_input == "can you tell me the definition of hogwarts":
        talk_function("A school for learning magic");

    elif user_input == "can you tell me the motto of hogwarts":
        talk_function("The Hogwarts' motto is Draco Dormiens Nunquam Titillandus which means never tickle a sleeping dragon");

    elif user_input == "can you tell me the founder of hogwarts":
        talk_function("Hogwarts School of Witchcraft and Wizardry was founded by four of the most brilliant witches and wizards of their time. It was founded in the 10th century by Godric Gryffindor, Rowena Ravenclaw, Helga Hufflepuff and Salazar Slytherin");

    elif user_input == "can you tell me who owns hogwarts":
        talk_function("These four founders are widely described as being the most brilliant witches and wizards of the time and were the following: Godric Gryffindor, Helga Hufflepuff, Rowena Ravenclaw and Salazar Slytherin. Each of them created their own House: Gryffindor, Hufflepuff, Ravenclaw and Slytherin respectively");

    elif user_input == "can you tell me where is hogwarts mean to be":
        talk_function("Hogwarts in the Scottish Highlands. In the Harry Potter books, Hogwarts is set in the Scottish Highlands, which is one of the main reasons why there are so many Scottish locations in the films");

    elif user_input == "please read my hogwarts letter":
        talk_function("Please provide me your name")
        name = input("Please provide me your name:")

        print(f'Dear {name}, We are pleased to inform you that you have been accepted at Hogwarts School of Witchcraft and Wizardry. Please find enclosed a list of all necessary books and equipment. Term begins on September 1')
        talk_function(f'Dear {name}, We are pleased to inform you that you have been accepted at Hogwarts School of Witchcraft and Wizardry. Please find enclosed a list of all necessary books and equipment. Term begins on September 1 , We await your arrival , Thank You')
    
    elif user_input == "how many stairs are there in hogwarts":
        talk_function("It has 142 staircases , Stairs at Hogwarts are not straightforward. The 142 staircases vary in shape, size and destination. There are wide ones, narrow ones, some with vanishing steps and others that lead somewhere different on a Friday");

    elif user_input == "can you tell me the wizarding school locations from hp":
        talk_function("Hogwarts School of Witchcraft and Wizardry it's in Scotland , Beauxbatons Academy of Magic it's in France , Castelobruxo it's in Central Brazil , Durmstrang Institute it's in Northern Europe , Ilvermorny it's in Eastern North America , Mahoutokoro School of Magic it's in Japan , Uagadou School of Magic it's in Uganda , Koldovstoretz it's in Russia");

    elif user_input == "can you please sing the song of hogwarts for me":
        talk_function("Yes I can , Hogwarts, Hogwarts , Hoggy Warty Hogwarts , Teach us something please , Whether we be old and bald , Or young with scabby knees , Our heads could do with filling , With some interesting stuff , For now they're bare and full of air , Dead flies and bits of fluff , So teach us things worth knowing  , Bring back what we've forgot Just do your best , we'll do the rest , And learn until our brains all rot , Thank you");
 
    elif user_input == "can you name the unforgivable curses":
        talk_function("They are the Killing Curse, Avada Kedavra, the Cruciatus Curse, Crucio, and the Imperius Curse, Imperio");

    elif user_input == "can you name the strongest wizard in hp":
        talk_function("Albus Percival Wulfric Brian Dumbledore , shortly called as Albus Dumbledore , In fact, he is the standard by which the rest of the Wizarding World is set. Harry himself utters that Dumbledore is the strongest wizard , and just that utterance is sort of a spell in and of itself");

    
    elif "who" in user_input:
        data = wikipedia.summary(user_input)
        print(data)
        talk_function(f'{data} Thank You')

    elif "where" in user_input:
        data = wikipedia.summary(user_input)
        print(data)
        talk_function(f'{data} Thank You')

    elif "what" in user_input:
        data = wikipedia.summary(user_input)
        print(data)
        talk_function(f'{data} Thank You')

    elif "when" in user_input:
        data = wikipedia.summary(user_input)
        print(data)
        talk_function(f'{data} Thank You')

    elif user_input == "please do an addition":
       
        talk_function("Please provide me the first number")
        num1 = int(input("Enter Number 1: "))
         
        talk_function("Please provide me the second number")
        num2 = int(input("Enter Number 2: "))

        total = num1 + num2
        print(f'The addition is: {total}')
        talk_function(f'The addition value is: {total}')

    elif user_input == "please do a subtraction":
           
        talk_function("Please provide me the first number")
        num1 = int(input("Enter Number 1: "))
         
        talk_function("Please provide me the second number")
        num2 = int(input("Enter Number 2: "))

        total = num1 - num2
        print(f'The subtraction is: {total}')
        talk_function(f'The subtraction value is: {total}')

    elif user_input == "please do a multiplication":
        talk_function("Please provide me the first number")
        num1 = int(input("Enter Number 1: "))
         
        talk_function("Please provide me the second number")
        num2 = int(input("Enter Number 2: "))

        total = num1 * num2
        print(f'The multiplication is: {total}')
        talk_function(f'The multiplication value is: {total}') 

    elif user_input == "please do a division":
        talk_function("Please provide me the first number")
        num1 = int(input("Enter Number 1: "))
         
        talk_function("Please provide me the second number")
        num2 = int(input("Enter Number 2: "))

        total = num1 / num2
        print(f'The division is: {total}')
        talk_function(f'The division value is: {total}')                                 
    

    elif user_input == "bye":
        talk_function("Good bye!");

    else:
        talk_function("Sorry , I can not understand you");       

