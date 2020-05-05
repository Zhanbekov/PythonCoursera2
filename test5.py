def greet(lang) :  #GREET is a function name
    if lang == 'es' : #LANG (parameter) = variable which we use in the function definition
        print("Hola")
    elif lang == 'fr' :
        print('Bonjour')
    else :
        print('Hello')

greet ('en')
greet ('es')
greet ('fr')