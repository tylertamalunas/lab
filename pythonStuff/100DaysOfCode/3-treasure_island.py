print("""
                       _
                ;`',
                `,  `,
                 ',   ;   ,,-""==..,
                  \    ','          \
          ,-""'-., ;    '    __.-="-.;
        ," ,,_    "V      _."
       ;,'   ''-,          "=--,_
              ,-''    _  _       `,
             /   ,.-+(_)(_)�--.,   ;
            ,'  /   ; (_)       `\ ,
            ; ,/    ;._.;         ;
            !,'     ;   ;
            V'      ;   ;
                    ;._.;
                    ;   ;
                    ;   ;        ~
     ~              ;._.;
               ~    ;   ;
                   .�   `.                ~
             __,.--;.___.;--.,___
       _,,-""      ;     ;       ""-,,_
   .-��            ;     ;             ``-.
  ",              �       `               ,"        ~
    "-_                                _-"
~       ``----..,_          __,,..bmw-�
                  ```''''���                  ~
                              ~
             ~
      """)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("You are standing on the beach, do yo ugo left or right?\n")
if direction != 'left':
    print("You stepped in quicksand, and got swallowed up.")
elif direction == 'left':
    swim_or_wait = input("You stand in front of a lake. Do you swim across, or wait for a raft?\n")
    if swim_or_wait != 'wait':
        print("You got eaten by a swarm of Saltwater Alligators.")
    elif swim_or_wait == 'wait':
        print("You arrive on the other side unharmed. There is a house with 3 doors.")
        door = input("Red, yellow, or blue. Which door do you choose?\n")
        if door == 'red':
            print("You were burned alive.")
        elif door == 'yellow':
            print("You found the treasure!")
        else:
            print("You got eaten by a Giraffe.")
