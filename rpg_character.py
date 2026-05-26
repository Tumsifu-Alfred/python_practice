
full_dot = '●'
empty_dot = '○'

def create_character(charactername,strength,intelligence,charisma):
    #charactername=input('charactername:')
    #strength=input('strength:')
    #intelligence=input('intelligence:')
    #charisma=input('charisma:')
    if not isinstance(charactername,str):
        return 'The character name should be a string'
    if charactername=='':
        return 'The character should have a name'
    if len(charactername)>10:
        return 'The character name is too long'
    if ' ' in charactername:
        return 'The character name should not contain spaces'
    if not isinstance(strength,int) or not isinstance(intelligence,int) or not isinstance(charisma,int):
        return 'All stats should be integers'

    if strength<1 or intelligence<1 or charisma<1:
        return 'All stats should be no less than 1' 
    
    if strength>4 or intelligence>4 or charisma>4:
        return 'All stats should be no more than 4'

    sum=strength+intelligence+charisma
    if sum<7 or sum>7:
        return 'The character should start with 7 points'

    return(f'{charactername}\nSTR {full_dot*strength}{empty_dot*(10-strength)}\nINT {full_dot*intelligence}{empty_dot*(10-intelligence)}\nCHA {full_dot*charisma}{empty_dot*(10-charisma)}')

print(create_character('kamala',4, 2, 1))

#in function only one first return is printed out if there are multiple returns used
#so it's best to use only one return keyword to output everything in the function