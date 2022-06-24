from posixpath import split 
# Main Function definition
def main ():
    # Creating Data structure
    full_name = {
        'Name': 'Cameron Stone' 
    }
    print(full_name['Name'])

    student_id = {
        'ID':'10123156'
    }
    print(student_id['ID'])

    Favourite_games = {
        'Game': [
            'NHL',
            'Valorant',
            'Apex Legends',
        ]
    }
    # Removed print from here


    Standup_Specials = {
        'Title': [
            'Shane Gillis Live in Austin',
            'Mark Normand: Out To Lunch',
            "Bill Burr: I'm Sorry You Feel That Way",
        ],
        'Genre': [
            'Story-Telling',
            'Anecdotal',
        ]
    }
    # Adding another standup special to data structure
    def add_title_to_standup(Standup_Specials, new_title):
        Standup_Specials['Title'].append(new_title)
    def add_genre_to_standups(Standup_Specials, new_genre):
        Standup_Specials['Genre'].append(new_genre)

    new_title = ("Joe List: This Years Material")
    add_title_to_standup(Standup_Specials, new_title)
    new_genre = ('Topical')
    add_genre_to_standups(Standup_Specials, new_genre)    
        
    print(Standup_Specials['Title'])
    print(Standup_Specials['Genre'])
    
    # Adding more to favourite games & Sorting list
    def add_games_to_list(Favourite_games, new_game):
        Favourite_games['Game'].extend(new_game)

        for i,p in enumerate(Favourite_games['Game']):
            Favourite_games['Game'][i] = p.lower()
        Favourite_games['Game'].sort()

    new_game = {
            'CS:GO',
            'F1',
            'NBA 2k',
    }    

    add_games_to_list(Favourite_games, new_game)      
   
    
# Generating a function to print name and student id
    def print_greeting(full_name):
        greeting = f"My name is {full_name['Name']}, but you can call me Sir {full_name['Name'].split(' ')[0]}"
        print(greeting) 
    
    def print_id(student_id):
        ID = f"My student ID is {student_id['ID']}"
        print(ID)   
        
    print_greeting(full_name)
    print_id(student_id)
# Generating function to make bullet list of favourite games
    def print_games(Favourite_games):
        heading = f"My favourite games are"
        print(heading)
        print('-'*len(heading))

        for g in Favourite_games['Game']:
            print(f"-{g}")
        print()
    print_games(Favourite_games)

#Function to print comma separated list of standup genres
    for i, o in enumerate(Standup_Specials['Genre']):
        print(o['Genre'], end='')
        if i < len(Standup_Specials['Genre'])-1:
            print(', ', end='')
    print('.', end='\n\n')

    pass



#comma seperated listed of titles






# Main Function Call
main() 