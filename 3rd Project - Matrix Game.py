from os import system
from re import S
from tkinter import N
system("clear")

print('''

                    Bienvenido a la Barranquitrix
*******************************************************************************
               _________
              |MMMMMMMMM|                _
  ________    |MMMMMMMMM|              _|l|_
 |!!!!!!!_|___|MMMMMMMMM|             |lllll|
 |!!!!!!|=========|MMMMM|             |lllll|_______
 |!!!!!!|=========|MMMMM|            _|lllll|HHHHHHH|
 |!!!!!!|=========|MMMMM|   ________|lllllllll|HHHHH|
 |!!!!!!|=========|MMMMM|  |unununun|lllllllll|HHHHH|______
 |!!!!!!|=========|MMMMM|  |nunununu|lllllllll|HH|:::::::::|
 |!!!!!!|=========|MMM__|..|un__unun|lllllllll|HH|:::::::::|
 |!!!!!!|=======_=|M_( ')' );' .)unu|lllllllll|HH|:::::::::|
 |!!!_!!|======( )|(. ` ,) (_ ', )un|lllllllll|HH|:::::::::| ~~~
 |!!(.)!|===__(`.')_(_ ')_,)(. _)unu|lllllllll|HH|:__::::::|~~  ~~
 |!(.`')|==( .)' .)MMM|M|| |un|nunun|lllllllll|``|( ,)_::::| ~~~~ ~
  -(: _)|=(`. ')_)|---|- '  ``|`````|lll____ll|  (_; `'):::|~~~  ~~~
     |  |==(_'_)|=|    ______        ''/\   \'   |(_'_)::::|\~~~~__|)__
*******************************************************************************
''')

print("Wake up cole... te tiene cogío la matrix")
input("Sigue al chirrete... Knock Knock (Presiona enter so cachón)")
print ("")
pill = input('''Bueno papi, la vuelta está así...
Tomas la píldora azul (A)... Sigue mamando cacho, y camellando como si fueras a ser alguien en la vida... o, 
Tomas la píldora roja (R)... Y el viaje va a ser mejor que tirarse un bareto''' '\n')

print ("")

if pill == "A":
    print("Ábrete de esta verga so cachón")

else:
    print("Welcome to the jungle papi !")
    
    skills = input("Quieres aprender a tirá muñeca? S / N" '\n')
    if skills == "N":
        print ("Pa' que mondá te saliste... te hubieses quedado en esa verga.  Game Over por Marica")
    else:
        print ("En la juega perro")
        import time
        import sys
        print('''Cargando la información en esa mondá:
        Ten paciencia careverga que tu eres brutelio''')


        #animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
        animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

        for i in range(len(animation)):
            time.sleep(0.5)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()

        print("\n")

        print ("Tamos readys papi !")
        
        print ("")

        meke = input ("Tírala plena... vamos a darle meke a las máquinas? S / N" "\n")
        if meke == "N":
            print("Entonces masca chácara? pa' que aprendiste a tirá muñeca? (Game Over por cagao!)")

        else:
            print ('''Papiii llóraloooo... Eres el elegido!
.     .       .  .   . .   .   . .    +  .
  .     .  :     .    .. :. .___---------___.
       .  .   .    .  :.:. _".^ .^ ^.  '.. :"-_. .
    .  :       .  .  .:../:            . .^  :.:\.
        .   . :: +. :.:/: .   .    .        . . .:\
 .  :    .     . _ :::/:               .  ^ .  . .:\
  .. . .   . - : :.:./.                        .  .:\
  .      .     . :..|:                    .  .  ^. .:|
    .       . : : ..||        .                . . !:|
  .     . . . ::. ::\(                           . :)/
 .   .     : . : .:.|. ######              .#######::|
  :.. .  :-  : .:  ::|.#######           ..########:|
 .  .  .  ..  .  .. :\ ########          :######## :/
  .        .+ :: : -.:\ ########       . ########.:/
    .  .+   . . . . :.:\. #######       #######..:/
      :: . . . . ::.:..:.\           .   .   ..:/
   .   .   .  .. :  -::::.\.       | |     . .:/
      .  :  .  .  .-:.":.::.\             ..:/
 .      -.   . . . .: .:::.:.\.           .:/
.   .   .  :      : ....::_:..:\   ___.  :/
   .   .  .   .:. .. .  .: :.:.:\       :/
     +   .   .   : . ::. :.:. .:.|\  .:/|
     .         +   .  .  ...:: ..|  --.:|
.      . . .   .  .  . ... :..:.."(  ..)"
 .   .       .      :  .   .: ::/  .  .::\ ''')