#!/usr/bin/python

# change the color of the dice by changing the text at the beginning of the print statements
# \033[1;30m (Black)
# \033[1;31m (Red)
# \033[1;32m (Green)
# \033[1;33m (Yellow)
# \033[1;34m (Blue)
# \033[1;35m (Purple)

# for additional formating options, see: https://stackabuse.com/how-to-print-colored-text-in-python/

def d4(value: int) -> None:
    print("""\033[1;32m
          ;;
        ,;  ;,
       ,;    ;,
      ,;      ;,
     ,;        ;,
    ,;          ;, 
   ,;            ;,
  ,;              ;,
 ,;                ;, 
,;        {}         ;,
::::::::::::::::::::::
    """.format(value))

def d6(value: int) -> None:
    print("""\033[1;32m
 ::::::::::::::
 ::          ::  
 ::          ::
 ::    {}     ::
 ::          ::
 ::          ::                
 :::::::::::::: 

    """.format(value))


def d20(value: int) -> None:
    # account for single and double digit numbers moving parts of the dice
    if value > 9:
        print("""\033[1;32m             
            ,:::,
       ,,,:;  :  ;:,,, 
   ,,,:       :       :,,, 
,,;...........:...........;,,
; ;          ;';          ; ;
;  ;        ;   ;        ;  ;
;   ;      ;     ;      ;   ;
;    ;    ;       ;    ;    ;
;     ;  ;   {}    ;  ;     ;
;      ;:...........:;      ;
;     , ;           ; ,     ;
;   ,'   ;         ;   ',   ;
'';'      ;       ;      ';''
   ''';    ;     ;    ;'''         
       ''':;;   ;;:'''
            ':::' 
    """.format(value))
        
    else: 
        print("""\033[1;32m             
            ,:::,
       ,,,:;  :  ;:,,, 
   ,,,:       :       :,,, 
,,;...........:...........;,,
; ;          ;';          ; ;
;  ;        ;   ;        ;  ;
;   ;      ;     ;      ;   ;
;    ;    ;       ;    ;    ;
;     ;  ;    {}    ;  ;     ;
;      ;:...........:;      ;
;     , ;           ; ,     ;
;   ,'   ;         ;   ',   ;
'';'      ;       ;      ';''
   ''';    ;     ;    ;'''         
       ''':;;   ;;:'''
            ':::' 
    """.format(value))
