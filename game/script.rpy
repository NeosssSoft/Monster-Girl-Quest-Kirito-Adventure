# You can place the script of your game in this file.
# - Puedes colocar el 'script' de tu juego en este archivo.

# Declare images below this line, using the image statement.
# - Declara imágenes bajo esta línea, usando 'image' como
#   en el ejemplo.
# eg. image eileen happy = "eileen_happy.png"
image fondo = "fondo.png"
image negro = "#000000"
image bg001 = "escenarios/bg001.bmp"
image iriasnormal = "personajes/irias.png"
image bg002 = "escenarios/bg002.bmp"
image bg003 = "escenarios/bg003.bmp"
image bg004 = "escenarios/bg004.bmp"
image cupido = "personajes/cupido.png"
image mai = "personajes/maliceizquierda.png"
image mad = "personajes/malicederecha.png"
image maa = "personajes/maliceasustada.png"
image man = "personajes/malicenormal.png"
image hentai = "cgs/censored.png"
image nada = "escenarios/nada.png"
image bosqueoscuro = "escenarios/bg005.bmp"
image cueva = "escenarios/bg006.bmp"
image chrome = "personajes/chromenormal.png"
image chromem = "personajes/chromemaxpower.png"
image logro1 = "logros/logro1.png"
image aliceh = "cgs/alicesincensura.png"
image bg007 = "escenarios/bg007.bmp"
image atardecer = "escenarios/cieloatardecer.bmp"
image logro2 = "logros/logro2.png"
image dia = "escenarios/dia.bmp"
image g = "personajes/gnomo.png"
image gs = "personajes/gnomesorprendida.png"
image puno = "efectos/002.bmp"
image galleta = "efectos/001.bmp"
image vsg = "efectos/vsg.png"
image punod = "efectos/punetazodestructor.png"
image sonico = "efectos/ataquesonico.png"
image hg = "cgs/gnomesincensura.png"
image hgc = "cgs/censoredG.png"
image hg2 = "cgs/gnomesincensura2.png"
image hg3 = "cgs/gnomesincensura3.png"
image hg4 = "cgs/gnomesincensura4.png"
image ex = "escenarios/extras.png"
image t = "escenarios/bgt.bmp"
image K = "personajes/Kreig.png"
image KB = "personajes/kreigB.png"
image KC = "personajes/KreigC.png"
                               
                                            
# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el 
#   ejemplo.
define k = Character("Kirito", color="#c8ffc8")
define I = Character("Irias", color="#c7ffc8")
define N = Character("Narrador", color="000000")
define A = Character("Alice", color="#c6ffc4")
define C = Character("Cupido",color="#c2ffc2")
define ch = Character("Chrome")
define G = Character("Gnomo")
define passworld = Character("passworld")
define K = Character("Kreig", color="c3ffc3")
 
 
init python: 
    style.default.font = ("fuente/georgia.ttf")

   
#Fades
define fadehold = Fade(0.5, 1.0, 0.5)

#Espacio de testeo

init -5 python:
    #custom bar -----------------------
    style.my_bar = Style(style.default)
    style.my_bar.xalign = 0.5
    style.my_bar.xmaximum = 315 # bar width
    style.my_bar.ymaximum = 30 # bar height
    style.my_bar.left_gutter = 5
    style.my_bar.right_gutter = 5
   
    # I have all my User Interface graphics stored in one file called ui.
    # To access them in my code, I put ui/ in front of all images in that file.
   
    style.my_bar.left_bar = Frame("ui/bar_full.png", 0, 0)
    style.my_bar.right_bar = Frame("ui/bar_empty.png", 0, 0)
    style.my_bar.hover_left_bar = Frame("ui/bar_hover.png", 0, 0)
   
    style.my_bar.thumb = "ui/thumb.png"
    style.my_bar.thumb_shadow = None
    style.my_bar.thumb_offset = 5


init python hide:
    for file in renpy.list_files():
        if file.startswith('bg') and file.endswith('.jpg'):
            name = file.replace('BG/','').replace('/', ' ').replace('.jpg','')
            renpy.image(name, Image(file))

init:
    image cg1 = "escenarios/bg001.bmp"
    image cg2 = "escenarios/bg002.bmp"
    image cg3 = "escenarios/bg003.bmp"
    image cg4 = "escenarios/bg004.bmp"
    image cg5 = "escenarios/bg006.bmp"
    image cg6 = "escenarios/bg007.bmp"
    image cg7 = "cg/alicesincensura.png"
    image cg8 = "escenarios/bg005.bmp"
    image cg9 = "cg/censored.png"
    image cg10 = "logros/logro1.png"

        
init python:
    #Logros y desbloqueables
    mp = MultiPersistent("demo.renpy.org")
    
    
init python:

    # Boton de H.
    if persistent.hentai is None:
        persistent.hentai = False
    
    
    
#Personajes Enamorables:

init -2 python:
    ## Character Irias --------------
   
    irias_love = 0 #The number of points she Starts with.
    max_love = 100  #The maximum points she can get.

init python:
    ## ------------ Love Points Activation Code-------------------
    #This controls when the love-points floater appears.
    show_irias=False

    ## ------------ Love Points Floating Meter --------------------
    def stats_overlay():               
       
        # ---Irias Love Bar -------
        if show_irias:
            ui.frame(
                xalign = 0.5, #centered
                ypos = 400,) #400 px Down from the Top
           
            ui.vbox(xalign = 0.5)
            ui.text ("Irias Puntos de Conquista: %d" %irias_love,
                xalign = 0.5)
            ui.bar(max_love, irias_love,
                style="my_bar")
           
            ui.close()
    config.overlay_functions.append(stats_overlay)
    

init python:
    ## ------------ Love Points Activation Code-------------------
    #This controls when the love-points floater appears.
    show_gnome=False

    ## ------------ Love Points Floating Meter --------------------
    def stats_overlay():               
       
        # --- Gnome Love Bar -------
        if show_gnome:
            ui.frame(
                xalign = 0.5, #centered
                ypos = 400,) #400 px Down from the Top
           
            ui.vbox(xalign = 0.5)
            ui.text ("Gnome Puntos de Conquista: %d" %gnome_love,
                xalign = 0.5)
            ui.bar(max_love, gnome_love,
                style="my_bar")
           
            ui.close()
    config.overlay_functions.append(stats_overlay)
        
        
# The game starts here.
# - El juego comienza aquí.
label start:
    #Dados
    $ d20 = renpy.random.randint(1, 20)
    $ d10 = renpy.random.randint(1, 10)
    $ d5 = renpy.random.randint(1, 5)
    $ d2 = renpy.random.randint(1, 2)
    $ d6 = renpy.random.randint(1, 6)
    
    #IA de los enemigos
    $IAA = renpy.random.randint(1, 3)
    $IAG = renpy.random.randint(1, 2)
    
    #Stats de los monstruos
    
    #Alice pequeña
    $ fuerzaA = 7
    $ vidaA = 26
    $ defensaA = 6
    $ danoA = 0
    
    #Gnome
    $ fuerzaG = 120
    $ vidaG = 432
    $ defensaG = 110
    $ danoG = 0
    

#Aqui se implementan las Stats del jugador
    $ puntos_fuerza = 0
    $ puntos_magia = 0
    $ puntos_vida = 10
    $ puntos_defensa = 0
    $ puntos_carisma = 0
    $ dano = 0
    $ puntos_fuerza_espejo = 0
    $ puntos_defensa_espejo = 0
    $ puntos_fuerza_espejo2 = 0
    $ puntos_defensa_espejo2 = 0
    $ puntos_vida_espejo = 0
    $ puntos_vida_espejo2 = 0
    
#Aqui se declaran los objetos y el dinero que tiene el jugador
    $ rupias = 100
    $ pociones_vida = 1
    $ pociones_magia = 1
    $ pociones_estados = 1
    $ bombas = 0
    $ regalos = 0
    
#Aqui se declaran las acciones de tiempo libre
    $ tiempo_libre01 = 0
    $ tiempo_libre02 = 0
    $ voluntad = 0
    
#Aqui se declaran los estados alterados
    $ presa = 0
    $ defender = 0
    
#Valor objetos
    $ bombasd = 7
    
    
# Grupo
    $ grupo = 0
    
# 1 = Gnome, 2 = Alice, 3 = Otro monstruo    
        
#Aqui empieza de verdad el juego


    show bg001
    $ renpy.music.play("musica/inicio.mp3")
    "La novela visual que esta apunto de jugar se encuentra en fase alpha por lo que la calidad en la versión final puede variar.."
    "Antes de comenzar a jugar debes saber que este juego ha sido echo de manera totalmente independiente, por lo que no tiene nada que ver con MGQ"
    "Por lo que esto es solamente y simplemente un fan game, dicho esto solo queda acomodar un par de opciones"
    "¿Deseas ver las escenas Hentai con censura o sin censura?"
    "Si luego cambias de opinion puedes volver a activar o quitar esta opcion desde el menu de opciones"
    menu:
        
        "Si quiero ver h":
            $ persistent.hentai = True
            jump irias
            
        "No, no quiero ver h":
            $ persistent.hentai = False
            jump irias
            
label irias:
    $ k = renpy.input("Nombre del jugador: \n{i}Usa Backspace para borrar el texto. \nPulsa Enter para confirmar{/i}",
"Kirito", length=20)
    $ k = k.strip()
        
    $ renpy.music.stop()
    scene negro with dissolve
    show text "Capitulo 1\nEl Comienzo de los Comienzos" with Pause(2.0)
                 
    scene cg1
    $ renpy.music.play("musica/irias.mp3")
    k "{i}Tal día como hoy fue el día en el que me convertí en el portador{/i}"
    k "{i}de un arma sin precedentes, un arma capaz de cambiar el rumbo de la historia.{/i}"
    k "{i}Ese arma es la espada de la diosa Irias.{/i}"
    k "{i}Un arma forjada con el poder de la diosa de la creación para acabar con los monstruos{/i}"
    k "{i}de este mundo. Desde aquel día jure que acabaría con todos los monstruos que se opusieran a Irias{/i}"
    show iriasnormal 
    k "{i}Por ello mi vida solo pertenece a la diosa Irias{/i}"
    I "Oh joven [k] es el momento de que emprendas tu viaje"
    I "Pero antes debo advertirte de los peligros que te esperan en tu viaje."
    I "Deberás luchar contra monstruos temibles que ansían pervertir a las pobres"
    I "e inocentes almas humanas, para entristecerme a mi, vuestra diosa."
    I "Jamas deberás sucumbir a las perversiones que esos demoníacos seres"
    I "intenten hacerte."
    I "Por ello te elegido a ti Kirito, tu seras mi caballero sagrado"
    I "que se encargara de erradicar de la faz de la tierra a esos seres."
    I "Para ayudarte en tu labor te he otorgado una espada forjada"
    I "con mi propia magia y ademas no solo eso también he despertado"
    I "un poco de tu poder latente, no puedo despertarlo por completo"
    I "ya que tu cuerpo no esta preparado para todo ese poder todavía."
    I "Para comenzar tu misión deberás dirigirte al templo de Ikarue"
    I "Que esta echo en mi honor, una vez allí veras tu destino"
    I "¿Lo has entendido todo Kirito?"
    N "En momentos así como jugador se te asignara la tarea de tomar una"
    N "decisión, según tus decisiones la historia cambiara."
    N "Así que se recomienda guardar muy a menudo, dado que una decisión mala podria acabar contigo."
    
    
    menu:
        
        "{b}Si lo he entendido todo{/b}":
            if persistent.logro1 is None:
                show logro1 at center with Pause(2.0)
                hide logro1
                $ show_irias=True
                pause 0.5
                $ irias_love+=10
                show expression Text("{color=ffffff}+10 Puntos de Amor{/color}",
                    size=50,
                    yalign=0.5, # Centers the text -- Toward Bottom.
                    xalign=0.5, # Centers the text -- Toward Right.
                    drop_shadow=(2, 2)) as text
                with dissolve
    
                $ show_irias=True
                $ renpy.pause()
                hide text with dissolve
                $ show_irias=False
                I "Me alegro Kirito, te deseo suerte en tu viaje"
                I "Se que estas predestinado a grandes cosas"
                $ renpy.music.stop()
                scene negro
                $ persistent.logro1 = True
                jump inicio
                
            else:
                $ show_irias=True
                pause 0.5
                $ irias_love+=10
                show expression Text("{color=ffffff}+10 Puntos de Amor{/color}",
                    size=50,
                    yalign=0.5, # Centers the text -- Toward Bottom.
                    xalign=0.5, # Centers the text -- Toward Right.
                    drop_shadow=(2, 2)) as text
                with dissolve
    
                $ show_irias=True
                $ renpy.pause()
                hide text with dissolve
                $ show_irias=False
                I "Me alegro Kirito, te deseo suerte en tu viaje"
                I "Se que estas predestinado a grandes cosas"
                $ renpy.music.stop()
                scene negro
                jump inicio 
                
        "{b}No, no lo he entendido Irias{/b}":
            I "¿¡¡COMO QUE NO LO HAS ENTENDIDO!!?"
            I "{b}Irias usa castigo eterno{/b}"
            N "Kirito pierde 10 puntos de vida"
            $ puntos_vida -=10
            if puntos_vida == 0:
                N "Kirito muere sin tener ninguna oportunidad para evitarlo"
                scene negro with dissolve
                show text "GAME OVER" with Pause(1.5)
                return
        
         
label inicio:
    $ renpy.music.play("musica/kiki2.mp3")
    scene bg002
    k "{i}Entonces me levante de la cama, estaba claro que aquello no había sido ningún sueño, era real{/i}"
    k "{i}Sobretodo por que aquella espada se encontraba justo delante de mis ojos, su mera presencia era capaz de intimidarme{/i}"
    k "{i}Entonces agarre la espada y la deje sobre la cama, acto seguido fui a vestirme. Mi aventura estaba apunto de comenzar{/i}"
    $ renpy.music.stop()
    $ renpy.music.play("musica/diasnormales.mp3")
    k "Bueno, hoy va a ser el gran día, ¿Quizás debería prepararme antes de partir?"
    N "Aveces dispondrás de tiempo libre entre la historia principal, pero tan solo podrás hacer 2 acciones en tu tiempo libre"
    N "Una vez se hayan acabado esas 2 acciones de tiempo libre volverás al marco principal de la historia, así que ten cuidado"
    N "con tus elecciones"
    
    menu:
        "{b}Ir de compras{/b}":
            k "Bien creo que seria un buen momento de comprar provisiones para mi viaje"
            if tiempo_libre01 >= 2:
                k "No, no debo hacerlo, ya he perdido demasiado tiempo aquí, es hora de que parta"
                jump destino
            else:
                $ tiempo_libre01 +=1
                jump compras01
            
        
        "{b}Entrenarse{/b}":
            k "Sera mejor que vaya a fortalecerme para poder plantar cara a los monstruos"
            if tiempo_libre01 >= 2:
                k "No, no debo hacerlo, ya he perdido demasiado tiempo aquí, es hora de que parta"
                jump destino
            else:
                $ tiempo_libre01 +=1
                jump entrenamiento01
            
        
        "{b}Partir hacia tu destino{/b}":
            k "Ya estoy listo para ir a mi destino"
            jump destino
        
label compras01:
    show bg003
    k "{i}Entonces partí hacia las tiendas de mi ciudad, ya que disponía de 100 rupias para gastar{/i}"
    k "¿Ahora la pregunta es... en que debería gastarlo?"
    
    menu:
        "{b}Pociones(10r){/b}":
            k "{i}Compre un par de pociones{/i}"
            N "Obtienes 1 poción de  {b}curación{/b}, 1 poción de {b}magia{/b}, 1 poción de {b}estados{/b}"
            N "Se te restan 10 rupias del inventario"
            $ rupias -=10
            jump acciones01
                       
        "{b}Armadura(15r){/b}":
            k "{i}Compre una armadura{/i}"
            N "Te equipas con armadura {b}normal{/b}"
            N "Tu {b}defensa{/b} aumenta en 5 puntos"
            N "Se te restan 15 {b}rupias{/b} del inventario"
            $ rupias -=15
            $ puntos_defensa +=5
            jump acciones01
        
        "{b}Bombas(15r){/b}":
            k "{i}Compre un par de bombas{/i}"
            N "Obtienes 2 {b}bombas{/b}"
            N "Se te restan 15 {b}rupias{/b} del inventario"
            $ bombas +=2
            $ rupias -=15
            jump acciones01
        
        "{b}Regalos(20r){/b}":
            k "{i}Compre un par de regalos{/i}"
            N "Obtienes 2 {b}regalos{/b}"
            N "Se te restan 20 {b}rupias{/b} del inventario"
            $ regalos +=2
            $ rupias -=20
            jump acciones01
            

label acciones01:
    
    k "¿Ahora que deberia hacer?"
    
    menu:
        "{b}Ir de compras{/b}":
            k "Bien, creo que seria un buen momento de comprar provisiones para mi viaje"
            if tiempo_libre01 >= 2:
                k "No, no debo hacerlo, ya he perdido demasiado tiempo aqui, es hora de que parta"
                jump destino
            else:
                $ tiempo_libre01 +=1
                jump compras01
        
        "{b}Entrenarte{/b}":
            k "Sera mejor que vaya a fortalecerme para poder plantar cara a los monstruos"
            if tiempo_libre01 >= 2:
                k "No, no debo hacerlo, ya he perdido demasiado tiempo aqui, es hora de que parta"
                jump destino
            else:
                $ tiempo_libre01 +=1
                jump entrenamiento01
        
        "{b}Partir hacia tu destino{/b}":
            k "Ya estoy listo para ir a mi destino"
            jump destino
            
label entrenamiento01:
    
    k "Bien creo que deberia fortalecer por completo mi cuerpo antes de aventurarme yo solo"
    N "Realizas un entrenamiento intensivo"
    N "Obtienes 5 puntos en {b}fuerza{/b}, obtienes 5 puntos en {b}magia{/b}, obtienes 5 puntos en {b}defensa{/b}, tu salud maxima aumenta en 12 puntos"
    $ puntos_fuerza +=5
    $ puntos_magia +=5
    $ puntos_vida +=12
    $ puntos_defensa +=5
    jump acciones01
    

label destino:
    k "Bien creo que ya estoy completamente preparado para partir hacia mi destino"
    N "Te comienzas a alejar del pueblo donde te has criado prácticamente durante toda tu vida"
    N "Sabes que fuera te esperaran retos, combates y aventuras pero aun así en lo mas adentro de tu ser sabes que que añoraras tu hogar"
    N "Aquí comienza tu aventura de ti depende lo que pase y como pase"
    jump camino01
    
label camino01:
    show bg004
    N "Comienzas a alejarte de tu pueblo natal, comienzas a caminar hacia el norte y te encuentras con dos carteles"
    N "En el primer cartel puedes leer (Ork Ville) y en el segundo (Bosque Oscuro) ambos caminos parecen dirigir hacia el templo de"
    N "Ikarue"
    N "Te paras a meditar durante unos segundos y eliges..."
    
    menu:
        "(Ork Ville)":
            k "{i}Tras meditarlo un par de segundos pensé que mi primer viaje debería ser a Ork Ville, por lo que partí hacia allí{/i}"
            jump caminoorkville
            
        "(Bosque Oscuro)":
            k "{i}Tras meditarlo un par de segundos pensé que mi primer viaje debería ser a Bosque Oscuro, por lo que partí hacia allí{/i}"
            jump bosqueoscuro
            

label caminoorkville:
    k "{i}Comencé a caminar hacia Ork Ville, jamas había estado antes en aquel sitio pero ya había escuchado alguna que otra historia{/i}"
    k "{i}de aquel sitio. Por lo que contaban las historias aquel lugar era en antaño un campamento de caballeros al servicio de Irias{/i}"
    k "{i}en aquel campamento se reunian todos los caballeros que la todopoderosa diosa Irias habia reclutado para la santa guerra.{/i}"
    k "{i}Tambien cuentan las historias que alli se libro la batalla definitiva contra la anterior reina monstruo.{/i}"
    k "{i}Por así decirlo es el ultimo bastión de defensa de la diosa Irias{/i}"
    k "{i}Poco mas que rumores y historias son lo que me vienen a mi cabeza cuando resuenan las palabras de Ork Ville{/i}"
    N "Escuchas un extraño grito femenino justo delante de ti"
    $ renpy.music.play("musica/battlestart.mp3")
    N "Tu cuerpo se pone tenso, parece que se prepara para lo que pueda venir..."
    N "Caminas apresuradamente hasta el origen y entonces ves a..."
    $ renpy.music.stop()
    $ renpy.music.play("musica/comi1.mp3")
    show mai at left
    show cupido at right
    N "Dos chicas monstruo, una cupido y una chica serpiente."
    N "Te asombras de ver a un monstruo al servicio de Irias en la tierra"
    N "Ves como la chica serpiente no para de moverse hacia un lado y otro sin parar de gritar"
    hide mai
    show mad at left
    N " "
    hide mad
    show mai at left
    N " "
    hide mai
    show mad at left
    N " "
    hide mad
    show mai at left
    N " "
    hide mai
    show mad at left
    N " "
    hide mad
    show mai at left
    N " "
    hide mai 
    show mad at left
    C "¡¡¿QUIERES PARAR DE GRITAR PUTA?!!"
    A "¡¡¡¿QUE?!!!"
    C "Tu asqueroso bailecito me esta poniendo de los nervios"
    A "¡¡Pero como has osado convertirme a mi!!"
    A "¡¡A MI!!"
    A "En este patético cuerpo enano"
    C "No tengo por que dar explicaciones a un ser de tu calaña"
    N "Parece que te ignoran..."
    A "{i}Derepente Alice clava su mirada en ti{/i}"
    A "¡¡EH, TU, HUMANO!!"
    A "¡¡Ayudameeeeeeeeeeeeeeeeeeeeeeeeeeeeeee!!"
    C "{i}Te mira{/i}"
    C "No hagas caso a esta puta alimaña, solo es una puta asquerosa que te querrá violar para satisfacer su puta hambre."
    k "{i}Entonces me pare a pensar en cuantas veces habia usado la palabra 'Puta' en la misma frase...{/i}"
    N "Te comienzas a preguntar por que ha empezado toda esta discursion"
    N "Por extraño que te parezca no sientes ni un ápice de miedo aun estando delante de uno de los seres a los que tu religión dicta que debes temer"
    k "¿Esto... por que no os calmáis un momento?"
    N "Ves como ambas te clavan la mirada fíjamente"
    N "Puedes apreciar como la monstruo serpiente parece haberse calmado"
    hide mad
    show man at left
    A "Mmmm, quizas visto desde este modo me pueda servir..."
    C "{i}Se gira hacia Alice{/i}"
    C "Bueno ya he perdido las ganas de acabar contigo, creo que en esa forma no molestaras a nadie en una temporada"
    A "Eso, huye zorra..."
    N "Ves como un velo sagrado cubre el cuerpo de cupido y esta desaparece"
    hide cupido
    hide man
    show man
    N "Te acabas de quedar solo delante de la chica serpiente"
    A "{i}Mira a su alrededor y se queda pensativa{/i}"
    N "Por lo que puedes ver parece que te esta ignorando"
    k "{i}¿Que deberia hacer?{/i}"
    
    menu:
        "{b}Huir{/b}":
            N "Huyes como alma que lleva el demonio"
            jump huirdealice
        
        "{b}Intentar hablar con ella{/b}":
            N "Te acercas a intentar dialogar con ella"
            jump intentarhablarconalice
        
        "{b}Ignorarla tu tambien{/b}":
            N "Pasas de ellas hasta el culo"
            jump ignoraralice
        
        "{b}Atacarla{/b}":
            N "Desenvainas tu espada y te lanzas como un loco al ataque"
            jump atacaralice
            

label atacaralice:
    $ renpy.music.stop()
    $ renpy.music.play("musica/battle.mp3")
    N "Acabas de iniciar tu primera batalla, es hora de explicarte como funciona el sistema de combate"
    N "Tu posees unos atributos básicos que son: Fuerza,Magia,Vida y Defensa"
    N "Fuerza sirve para atacar a tus enemigos, levantar objetos, etc... Cuanto mas alto sea este parametro mas daño haras"
    N "Magia sirve para lanzar echizos pero todabia no sabes ninguno asi que esto se explicara mas adelante"
    N "Vida sirve para contar tus puntos vitales, cuando estos llegan a 0 en es igual a un combate GAME OVER"
    N "Defensa sirve para resistir daños, cuantos mas puntos tengas mas daño podras absorver sin perder vida"
    N "Durante cada asalto se te recordaran tus puntos en cada atributo y se te dispondran varias elecciones"
    N "Cada eleccion sera la accion que tomaras en tu turno"
    N "Para ganar la batalla deberas dejar sin puntos de vida a tu enemigo"
    N "Pero en todo momento desconoceras las stats de tu enemigo, ya que no tienes poderes magicos para saber como se siente tu enemigo"
    N "Al empezar una batalla se lanzara un dado de 1d2 si el resultado es 1 tu tienes iniciativa, si por el contrario sale 2 el asalto es de tu oponente"
    $ puntos_fuerza_espejo = puntos_fuerza
    $ puntos_defensa_espejo = puntos_defensa
    N "{b}COMIENZA LA BATALLA{/b}"
    
    N "[k]: Fuerza = [puntos_fuerza] , Vida = [puntos_vida] , Defensa = [puntos_defensa] "
    N "[k] Inventario: Pociones de Vida [pociones_vida] , Pociones de Magia [pociones_magia] , Pociones de Estados [pociones_estados] , Bombas [bombas] "
    N "Lanzamiento de Iniciativa"
    N "Resultado del dado [d2]"
    
    if d2 == 1:
        N "Comienzas tu"
        N "Elige tu accion"
        jump accionesprimercombatejugador                                
    else: 
        N "Comienza tu oponente [A]"
        jump accionesprimercombateIA
    
    
    
label accionesprimercombatejugador:
    
    $ vidapocion = 4
    N "[k]: Fuerza = [puntos_fuerza] , Vida = [puntos_vida] , Defensa = [puntos_defensa] "
    N "[k] Inventario: Pociones de Vida [pociones_vida] , Pociones de Magia [pociones_magia] , Pociones de Estados [pociones_estados] , Bombas [bombas] "
    
    menu:
        "{b}Ataque Fisico{/b}":
            if presa >= 1:
                "Una de tus piernas esta atrapada, no puedes realizar ningun movimiento de ataque"
                jump accionesprimercombatejugador
            else:
                N "Te lanzas a golpear con tu espada al monstruo [A]"
                $ renpy.sound.play("musica/hit.ogg")
                $ d5 = renpy.random.randint(1, 5)
                $ puntos_fuerza += d5
                $ puntos_fuerza -= defensaA
                $ dano += puntos_fuerza
                $ vidaA -= dano
                
                if vidaA <= 0:
                    A "Maldito humano.... eres demasiado fuerte"
                    N "Ves como la chica serpiente comienza a mirarte asustada"
                    $ puntos_fuerza = puntos_fuerza_espejo
                    $ puntos_defensa = puntos_defensa_espejo
                    $ dano = 0
                    jump ganar
                    
                else:
                    k "GYAAAAAH!!!"
                    N "Logras hacerle [dano] de daño"
                    pause (1.0)
                    $ puntos_fuerza = puntos_fuerza_espejo
                    $ puntos_defensa = puntos_defensa_espejo
                    $ dano = 0
                    $IAA = renpy.random.randint(1, 3)
                    jump accionesprimercombateIA
                
                
        "{b}Usar objeto{/b}":
            N "Buscas en tu inventario algun objeto"
            jump inventario
        "{b}Peticion{/b}":
            N "Quieres hacerle una peticion a [A]"
            jump peticionesAlice
        "{b}Rendirte{/b}":
            N "Te rindes"
            jump rendiciondeAlice
        "{b}Defender{/b}":
            N "Te colocas en una posicion defensiva"
            if defender == 0:
                $ defender += 1
                $ d5 = renpy.random.randint(1, 5)
                $ puntos_defensa += d5
                $IAA = renpy.random.randint(1, 3)
                jump accionesprimercombateIA
            else:
                N "Ya estas en una posicion defensiva"
                jump accionesprimercombatejugador
            N "Sientes como tu cuerpo se prepara para defenderse de un gran golpe, por lo que tu defensa aumenta en [puntos_defensa]"
            $IAA = renpy.random.randint(1, 3)
            jump accionesprimercombateIA
        "{b}Usar Habilidad{/b}":
            N "Todabia no tienes ninguna habilidad"
            jump accionesprimercombatejugador
        "{b}Usar Conjuro{/b}":
            N "Todabia no tienes ningun hechizo"
            jump accionesprimercombatejugador
        "{b}Forcejear{b}":
            $ d2 = renpy.random.randint(1, 2)
            if d2 == 1:
                "Consigues zafarte de la cola del monstruo, ahora puedes atacarle"
                $ presa = 0
                $IAA = renpy.random.randint(1, 3)
                jump accionesprimercombatejugador
            else:
                "No logras zafarte de la cola"
                $IAA = renpy.random.randint(1, 3)
                jump accionesprimercombateIA
            
                
label accionesprimercombateIA:
    if IAA == 1:
        A "{i}Usa su cola para golpearte en las piernas{/i}"
        $ renpy.sound.play("musica/hit.ogg")
        $ d5 = renpy.random.randint(1, 5)
        $ d5 += fuerzaA
        $ fuerzaA -= puntos_defensa
        if fuerzaA <= 0:
            "Logras resistir el golpe y no te causa ningun daño"
            $ fuerzaA = 7
            $ defensaA = 6
            $ danoA = 0
            jump accionesprimercombatejugador
        else:
            $ danoA += fuerzaA
            $ puntos_vida -= danoA
        if puntos_vida <= 0:
            N "Te hace un total de [danoA] de daño"
            N "Dejandote a [puntos_vida] puntos de vida"
            $ renpy.music.stop()
            $ renpy.music.play("musica/game_over.ogg")
            A "Necio humano, jamas podrias igualarme en poder aunque mi cuerpo haya menguado mis poderes no lo haran"
            A "Ahora preparate para ser violado hasta morir"
            N "Notas como tu cuerpo se ha debilitado por completo, apenas puedes mantenerte en pie"
            N "Sueltas tu espada y caes rendido, comienzas a notar como tu consciencia se desvanece poco a poco"
            A "No te duermas todabia... aun nos queda mucho juego"
            jump hentaiA
        else:
            N "Te hace un total de [danoA] de daño"
            N "Dejandote a [puntos_vida] puntos de vida"
            pause(1.5)
            $ fuerzaA = 7
            $ defensaA = 6
            $ danoA = 0
            N "Sientes un gran golpe justo a la altura de tus rodillas, te empieza a escocer un poco"
            jump accionesprimercombatejugador
        if vidaA <= 0:
            A "Maldito humano.... eres demasiado fuerte"
            N "Ves como la chica serpiente comienza a mirarte asustada"
            jump ganar
        else:
            jump accionesprimercombatejugador
            
    if IAA == 2:
        A "{i}Usa su cola para agarrarte una pierna{/i}"
        $ presa += 1
        $ renpy.sound.play("musica/presa.ogg")
        $ d5 = renpy.random.randint(1, 5)
        $ d5 += fuerzaA
        $ fuerzaA -= puntos_defensa
        if fuerzaA <= 0:
            "Logras resistir el golpe y no te causa ningun daño"
            "Pero ha agarrado tu pierna y aunque su cuerpo sea pequeño parece ser capaz de ejercer una gran fuerza con su cola"
            $ fuerzaA = 7
            $ defensaA = 6
            $ danoA = 0
            jump accionesprimercombatejugador
            
        else:
            $ danoA += fuerzaA
            pause(0.5)
            $ puntos_vida -= danoA
        if puntos_vida <= 0:
            $ renpy.music.stop()
            $ renpy.music.play("musica/game_over.ogg")
            A "Necio humano, jamas podrias igualarme en poder aunque mi cuerpo haya menguado mis poderes no lo haran"
            A "Ahora preparate para ser violado hasta morir"
            N "Notas como tu cuerpo se ha debilitado por completo, apenas puedes mantenerte en pie"
            N "Sueltas tu espada y caes rendido, comienzas a notar como tu consciencia se desvanece poco a poco"
            A "No te duermas todabia... aun nos queda mucho juego"
            jump hentaiA
        else:
            N "Te hace un total de [danoA] de daño"
            N "Dejandote a [puntos_vida] puntos de vida"
            N "Ves como una de tus piernas es sujetada con fuerza por la cola de Alice"
            N "Por extraño que parezca sientes como si tu pierna estuviera siendo aplastada por un tren y esto hace que apenas te puedas mover"
            N "Ves como su cuerpo aunque sea pequeño tiene una fuerza bastante elevada"
            pause(1.5)
            $ fuerzaA = 7
            $ defensaA = 6
            $ danoA = 0
            jump accionesprimercombatejugador
        if vidaA <= 0:
            A "Maldito humano.... eres demasiado fuerte"
            N "Ves como la chica serpiente comienza a mirarte asustada"
            jump ganar
        else:
            jump accionesprimercombatejugador
            
    if IAA == 3:
        A "{i}Se queda pensativa{/i}"
        N "Por lo que parece te esta ignorando por completo"
        k "{i}Quizas seria un buen momento para golpearla...{/i}"
        
        if vidaA <= 0:
            A "Maldito humano.... eres demasiado fuerte"
            N "Ves como la chica serpiente comienza a mirarte asustada"
            jump ganar
        else: 
            jump accionesprimercombatejugador
            
        if puntos_vida <= 0:
            $ renpy.music.stop()
            $ renpy.music.play("musica/game_over.ogg")
            A "Necio humano, jamas podrias igualarme en poder aunque mi cuerpo haya menguado mis poderes no lo haran"
            A "Ahora preparate para ser violado hasta morir"
            N "Notas como tu cuerpo se ha debilitado por completo, apenas puedes mantenerte en pie"
            N "Sueltas tu espada y caes rendido, comienzas a notar como tu consciencia se desvanece poco a poco"
            A "No te duermas todabia... aun nos queda mucho juego"
            jump hentaiA
        else:
            jump accionesprimercombatejugador
        
        
label ganar:
    $ renpy.music.stop()
    $ renpy.music.play("musica/finalattack.mp3")
    A "Tu... tu, tu no eres humano!!"
    N "Derepente notas como tu cuerpo comienza a exhalar desmesuradamente vapor"
    A "Se nota que tu poder es increible... pero no seras capaz de mantener ese ritmo durante mucho mas tiempo"
    k "{i}No entiendo que le pasa a mi cuerpo... me noto mas veloz, mas fuerte, capaz de acabar con ella en decimas de segundo.{/i}"
    k "{i}Pero al mismo tiempo me doy cuenta de que las energias de mi cuerpo se comienzan a desvanecer rapidamente{/i}"
    A "{i}Su rostro comienza a mostrar una expresion de satisfaccion{/i}"
    A "¿Sabes una cosa? podemos jugarnos esto a una ultima carta... Podria darte mi mejor golpe y tu el tuyo"
    A "El que quede en pie gana!! gagagagagagagagagaga"
    $ renpy.music.stop()
    $ renpy.music.play("musica/end.mp3")
    A "{i}Comienza a generar una bola de energia en la palma de su mano{/i}"
    k "{i}Esto es... ahora o nunca. Se que puedo ganar, esta energia que hay brotando ahora mismo dentro de mi cuerpo debe ser el poder{/i}"
    k "{i}de Irias corriendo por mis venas. Si no consigo derrotar a este monstruo no sere capaz de volver a mirarme a mi mismo al espejo de nuevo{/i}"
    N "Agarras con fuerza tu espada"
    N "Ves como el monstruo viene a una velocidad increiblemente vertiginosa hacia ti, tal que parece un camion a punto de arrollarte sin piedad"
    N "Tu no eres menos, comienzas a igualar su velocidad, ambos pareceis el destello de un relampago con una fuerza atronadora"
    A "RASENGAN!!! ({b}Narrador:{/b} No me hago responsable de cualquier plagio....)"
    $ renpy.sound.play("musica/hit.ogg")
    N "Tu espada choca contra la palma de Alice produciendo un ruido tan ensordecedor que no te extrañaria que se hubiera escuchado en todo el mundo"
    N "Acto seguido se crea una gran onda expansiva que a su vez es seguida de una increible luz cegadora"
    $ d2 = renpy.random.randint(1, 2)
    jump desempate
    
label desempate:
    if d2 == 1:
        show nada
        pause (0.2)
        hide man
        show bg004
        N "Tras el choque ves como la chica monstruo a desaparecido"
        N "Comienzas a mirar en todas las direcciones, pero no la ves"
        k "{i}Eso significa que la he mandado a tomar por culo? Ojala que asi sea...{/i}"
        N "Notas como tu cuerpo se cae al suelo sin que puedas remediarlo, inmediatamente despues te quedas incosciente"
        "Felicidades has llegado al final de la demo y has logrado derrotar a la mismisima mini Alice, sientete orgulloso"
        return
    if d2 == 2:
        N "Tras el choque ves como la espada que te fue legada por Irias sale disparada hacia el cielo"
        A "Para ser un humano posees demasiado poder, no puedo permitir que un humano como tu derroche su potencial sirviendo una diosa falsa"
        A "De ahora en adelante {b}YO SERE TU DIOSA{/b}"
        N "Tu cuerpo comienza a dejar de responderte, tus piernas te fallan y caes arrodillado delante de la chica monstruo"
        A "{i}Se saca una cuerda y te la ata al cuello{/i}"
        A "De ahora en adelante sere tu ama y me serviras solamente a mi"
        "Felicidades has llegado al final de la demo y has logrado acabar siendo el perro de Alice, sientete orgulloso joven guerrero"
        return
        
label hentaiA:
    hide man
    if persistent.hentai == False:
        show hentai
        "Felicidades has llegado al final de la demo y has logrado acabar siendo violasacrado por Alice para el resto de tus dias..."
    else:
        show aliceh
        "Felicidades has llegado al final de la demo y has logrado acabar siendo violasacrado por Alice para el resto de tus dias..."
        
    return
        
    
    
label huirdealice:
    hide man
    $ renpy.music.stop()
    $ renpy.sound.play("musica/escape.ogg")
    N "Logras escapar de Alice sin que se diese cuenta, aunque no parece que tampoco te estaba haciendo mucho caso"
    "Hasta aqui llega la demo, es una lastima que no hayas intentado pelear con Alice..."
    return
                                                                                                                                  
            
label intentarhablarconalice:
    N "Te acercas para intentar hablar con Alice"
    A "Misera rata humana, te enseñare a no acercarte a un ser como yo!!"
    k "{i}¿Pero que mierdas he echo yo? es como si en esta demo estuviera destinado a luchar contra Alice...{/i}"
    jump atacaralice
    
        
label ignoraralice:
    show nada
    N "Ambos entrais en un bucle de auto ignorancia tal que acabais olvidando la existencia de todo"
    "Fin de la demo"
    return
    
label peticionesAlice:
    N "Todabia no has desbloqueado ninguna peticion"
    N "Para desbloquear una peticion has de haber sido violado por otro monstruo con anterioridad"
    jump accionesprimercombatejugador
    
label rendiciondeAlice:
    N "Tiras tu espada al suelo en señal de derrota, esperando asi que tu adversaria sea piadosa"
    $ renpy.music.stop()
    $ renpy.music.play("musica/game_over.ogg")
    A "Necio humano, jamas podrias igualarme en poder aunque mi cuerpo haya menguado mis poderes no lo haran"
    A "Ahora preparate para ser violado hasta morir"
    N "No tienes mas opcion que hacerle caso, por extraño que parezca comienzas a pensar que quizas no sea un mal final para tu aventura..."
    jump hentaiA
    
label inventario:
    N "Recuerda que actualmente tienes Pociones de Vida [pociones_vida] , Pociones de Magia [pociones_magia] , Pociones de Estados [pociones_estados] , Bombas [bombas]"
    N "Pero ahora mismo solo puedes usar 2 objetos"
    
    menu:
        "{b}Pociones de vida{/b}":
            if pociones_vida <= 0:
                N "No te quedan pociones"
                jump accionesprimercombatejugador
            else:
                $ pociones_vida -= 1
                N "Gastas una pocion"
            if puntos_vida < 22:
                $ puntos_vida += vidapocion
                N "Obtienes 4 puntos mas de vida"
                $IAA = renpy.random.randint(1, 3)
                jump accionesprimercombateIA
            if puntos_vida >= 22:
                N "Restableces por completo tu vida"
                $ puntos_vida = 22
                $IAA = renpy.random.randint(1, 3)
                jump accionesprimercombateIA
           
            
        "{b}Bombas{/b}":
            if bombas <= 0:
                N "No te quedan bombas"
                jump accionesprimercombatejugador
            else:
                $ bombas -= 1
                N "Gastas una bomba"
                $ vidaA -= bombasd
                N "Causandole 7 puntos de daño directos"
                $IAA = renpy.random.randint(1, 3)
                jump accionesprimercombateIA
        
label bosqueoscuro:
    $ renpy.music.stop()
    $ renpy.music.play("musica/kazan.mp3")
    show bosqueoscuro
    N "Comienzas a caminar hacia bosque oscuro, antes de que te puedas dar cuenta ya estas metido del todo en el bosque"
    k "{i}Creo que ya entiendo por que lo llaman bosque oscuro...{/i}"
    k "{i}Si te fijas bien conforme mas adentro estas de este bosque los arboles son cada vez mas y mas grandes{/i}"
    k "{i}Tanto que las hojas de sus arboles son lo suficientemente grandes como para impedir que un solo rayo de sol pase atraves de ellos{/i}"
    k "{i}La verdad es que pocas historias o rumores he llegado a escuchar de este sitio{/i}"
    k "{i}Por lo que se este bosque antes era poblado por un grupo de elfos que se dedicaban a vivir su vida pacificamente aqui{/i}"
    k "{i}Y un dia la diosa Irias decidio mandar a un grupo de caballeros para hacer que se fueran del bosque, no se si hubo o no motivos para hacer aquello{/i}"
    k "{i}Pero la diosa Irias es nuestra creadora y no debemos desafiar su voluntad.{/i}"
    k "{i}Por ejemplo la diosa Irias ha decidido que yo sea su proximo caballero sagrado que liderara la ultima gran guerra contra la reina monstruo{/i}"
    k "{i}me guste o no, es la mision que mi creadora me ha encomendado...{/i}"
    N "Despues de un buen rato de haber estado caminando te encuentras con una cueva en la que comienzas a escuchar a alguien hablando"
    N "No llegas a entender las palabras que oyes ya que parecen simples murmullos sin sentido, pero decides ir a investigar que son"
    N "dado que no has encontrado otro camino mas a seguir"
    pause(0.5)
    show cueva
    $ renpy.music.stop()
    $ renpy.music.play("musica/dungeon1.mp3")
    N "Logras llegar al origen de los murmullos, pero te llevas una sorpresa"
    show chrome
    N "Ves el cuerpo sin vida de un hombre que lleva una armadura de caballero con la insignia de la diosa Irias al lado de una chica pequeña"
    N "Que tiene un aspecto bastante extraño, casi dirias que es alguna especie de enfermera de mala muerte"
    ch "¿Idiota, esto es lo mejor que esa furcia de Irias puede mandarme?"
    ch "Para ser uno de los soldados de sus mejores filas no tenia ni un apice de poder latente"
    ch "Si reportara esto a la reina monstruo seguro que se partiria en dos de la risa, hahaahahaha"
    k "{i}¿Que diablos es? si ha vencido a un caballero de Irias experimentado, yo solo debo ser una estupida mota de polvo para ella ahora mismo...{/i}"
    ch "{i}Se gira hacia ti{/i}"
    ch "kukukuku, que gracioso. Un mortal que se ha perdido y esta en el sitio que menos debia en el momento que no debia"
    ch "Hoy me siento piadosa, asi que podemos hacer un trato, kukukuku"
    ch "Tu te bajas los pantalones y yo te pateo el culo sin descanso hasta que te quedes incosciente, para que yo luego pueda jugar con todos tus organos"
    ch "kukukuku, que me dices ?"
    k "{i}Deveras que voy siquiera a plantearme esto?{/i}"
    
    menu:
        "{b}Cedes a que te paten{/b}":
            $ renpy.music.stop()
            $ renpy.music.play("musica/comi1.mp3")
            k "{i}Sinceramente despues de ver el cuerpo sin vida de un caballero de irias destrozado y ella se muestra como si nada{/i}"
            k "{i}Entonces como siquiera yo puedo plantarle cara... se que mi destino sera horroso... pero almenos vivire todo lo que pueda{/i}"
            k "Acepto tu trato..."
            ch "kukukuku, la verdad es que esperaba que te saliera almenos un poco de heroicidad por tu parte. Pero bueno..."
            ch "ME DIVERTIRE !!!"
            N "Te bajas los pantalones y miras fijamente a la pared rezando que acabe esto lo antes posible"
            ch "{i}Te suelta una patada increiblemente fuerte en tu trasero, tanto que seguramente te haya dejado la marca de su zapato en el{/i}"
            $ renpy.sound.play("musica/hit.ogg")
            N "Tus nalgas se ponen rojizas como el fuego, intentas contener las lagrimas con todas tus fuerzas"
            $ renpy.sound.play("musica/hit.ogg")
            ch "TE PONE EH!!?"
            $ renpy.sound.play("musica/hit.ogg")
            $ renpy.sound.play("musica/hit.ogg")
            $ renpy.sound.play("musica/hit.ogg")
            $ renpy.sound.play("musica/hit.ogg")
            $ renpy.sound.play("musica/hit.ogg")
            $ renpy.sound.play("musica/hit.ogg")
            $ renpy.sound.play("musica/hit.ogg")
            $ renpy.sound.play("musica/hit.ogg")
            $ renpy.sound.play("musica/hit.ogg")
            $ renpy.sound.play("musica/hit.ogg")
            $ renpy.sound.play("musica/hit.ogg")
            $ renpy.sound.play("musica/hit.ogg")
            $ renpy.sound.play("musica/hit.ogg")
            $ renpy.sound.play("musica/hit.ogg")
            scene negro with dissolve
            hide chrome
            show text "Varias horas despues" with Pause(1.5)
            show cueva
            show chrome
            N "Notas como ya no dispones de aquello a lo que llamabas antes 'culo' "
            k "Aaaaaaaaa..."
            ch "Interesante, unas nalgas realmente interesantes, kukukuku"
            ch "Creo que ya se conque voy a experimentar primero mientras estes incosciente, hahahahahaa"
            k "Pero que cojones??"
            N "Ves como te desplomas al suelo quedandote incosciente, debido al enorme escozor que sientes en tus potentosas nalgas"
            ch "Ya me habia extrañado a mi que te mantuvieras tanto tiempo en pie sin culo, kukukuku"
            hide chrome
            scene negro with dissolve
            show text "GAME OVER" with Pause(1.5)
            return
            
        
        "{b}Te niegas rotundamente{/b}":
            k "{i}Soy el elegido por Irias para ser un sagrado caballero y jamas deberia siquiera temer a un monstruo{/i}"
            k "Eh tu!!, ¿Que te hace pensar que podrias vencerme tu a mi?"
            ch "Mmm veo que tienes agallas, ademas noto algo de poder en tu interior que comienza a despertarse"
            ch "El mero echo de que no me temas significa que hay algo poderoso en ti"
            ch "Pero no eres capaz de darte cuenta de ello.... kukuku"
            ch "Ya se que voy a hacer!"
            ch "Te injectare mi nueva inyeccion potenciadora"
            ch "Supongo que tu cuerpo alcanzara todo su poder, pero al mismo tiempo te estaras muriendo por dentro"
            ch "Bien jugaremos a si, kukukukukuku"
            k "Eh?"
            N "Antes de que puedas siquiera reaccionar te lanza una jeringa que se clava en tu pecho"
            k "Aaaaaaah!!"
            ch "No tardaras en notar los efectos... Asi podre ver que tipo de poder guardas en tu interior humano"
            N "Notas como los musculos de tus brazos y piernas se comienzan a tensar"
            N "Tu cuerpo comienza a exhalar vapor por todas partes"
            N "Te echas las manos a la cabeza intentado mantener el control de tu ser"
            N "Comienzas a recordar las palabras de Irias"
            hide chrome
            scene bg001 with dissolve
            show iriasnormal
            I "Jamas deberas sucumbir a las perversiones que esos demoniacos seres querran hacerte"
            pause(0.5)
            hide iriasnormal
            scene cueva with dissolve
            show chrome
            ch "Oh, el {b}bhabhao{/b}..."
            ch "Esa gran habilidad heredada unicamente de la linea sucesoria de la reina monstruo"
            ch "Pero noto como tu poder esta algo degenerado"
            ch "Como pensaba, los poderes latentes no se pueden traspasar a cuerpos humanos completamente"
            ch "Es algo interesante, kukukuku"
            ch "Como regalo de despedida yo tambien te enseñare mi poder latente"
            ch "Si sobrevives, quiero que cuentes a todos los humanos de este planeta"
            ch "Que su destrucción es algo que esta muy proximo"
            hide chrome
            show chromem
            ch "Este es mi poder, el poder de una shinigami"
            ch "Soy capaz de controlar a las almas a mi voluntad"
            ch "Para que hagan lo que yo quiera"
            N "Ves como tu consciencia se desvanece poco a poco sin que tu puedas hacer algo para remediarlo"
            N "Pero sabes que recordaras este momento para el resto de tu vida"
            hide chromem
            scene negro with dissolve
            show text "Un par de horas despues" with Pause(1.5)
            jump despuesdechrome
            
label despuesdechrome:
    scene cueva with Pixellate(2, 5)
    N "Comienzas a abrir tus ojos lentamente, notas como todo tu cuerpo te pesa."
    N "Te comienzas a sentir como si un tren te hubiera pasado por encima."
    k "Arghh... al final despues de todo esa chica era demasiado poderosa para mi.."
    k "Gracias a Irias que sigo vivo"
    k "{i}Ojala no me vuelva a encontrar con un monstruo tan poderoso de nuevo..{/i}"
    N "Comienzas a ver luz al final de la cueva, por lo que sin pensartelo avanzas hacia ella poco apoco"
    N "Tus heridas son bastante serias por lo que puedes sentir, te estan dificultando la movilidad."
    N "Intentas poner tus manos sobre ellas esperando poder asi aliviar un poco tu dolor"
    N "Conforme avanzas la luz se va haciendo mas y mas grande hasta que derepente acabas logrando salir de a cueva"
    scene bg007 with fadehold
    N "Ante ti se puede ver un sendero, parece que estas casi al final de tu travesia hacia el templo de Ikarue"
    k "{i}Con estas heridas me sera imposible avanzar mas, creo que deberia descansar aqui un rato...{/i}"
    N "Te vas a un lado del camino y sacas un par de vendas y desinfectante que llevabas en tu mochila"
    N "Tratas tus heridas como puedes, ya que no eres ningun doctor ni dispones de conocimientos sobre primeros auxilios"
    k "{i}Parece que ya no llegare hoy al templo de Ikarue... Sera mejor que me prepare para pasar la noche{/i}"
    scene atardecer with dissolve
    $ renpy.music.stop()
    $ renpy.music.play("musica/findeldia.mp3")
    k "Hoy ha sido un dia realmente duro la verdad..."
    k "No pense que en mi primer viaje la cosa se pusiese tan complicada como se a puesto"
    k "No puedo parar de preguntarme... ¿A que demonios se referia conque la destruccion de los humanos es algo que esta muy proximo?"
    k "Y no solo eso, tambien me aterra saber que es ese poder que llamo bhabhao..."
    k "Quizas mañana consiga algunas respuestas en el templo de Ikarue"
    $ renpy.music.stop()
    scene negro with dissolve
    play sound "musica/ending.mp3"
    show text "Resultados Del Capitulo 1\nEl Comienzo de los Comienzos" with Pause(2.0)
    show text "Elegiste ir a {b}Bosque Oscuro{/b}\nNo cediste ante {b}Chrome{/b}\nDescubriste el {b}Bhabhao{/b}" with Pause(5.0)
    show text "Capitulo 2\nUn templo, un dios y un mesisas" with Pause(2.0)
    jump capitulo2b
    
    
label capitulo2b:
    if persistent.logro2 is None:
        show logro2 with Pause(2.0)
        hide logro2
        $ persistent.logro2 = True
        $ renpy.music.play("musica/diasnormales.mp3")
        scene dia with dissolve
        N "Notas como los primeros rayos de luz del sol entran por tus ojos"
        N "Te comienzas a sentir como nuevo, parece que todas las heridas que tenias han desaparecido"
        k "Buaaah, que bien he dormido."
        scene bg007 with dissolve
        N "Comienzas a desayunar, hoy vas a continuar la ultima parte del camino que te queda para llegar al templo"
        k "Bien, como parece que me he levantado pronto creo que puedo gastar un poco de ese tiempo en algo 'constructivo'"
        k "Oh quizas deberia de partir ya y no perder mas tiempo"
        
        menu:
            "Dar una vuelta por ahi":
                k "Visto lo visto, creo que lo mejor que puedo hacer es simplemente dar una vuelta por la zona a ver si hay algo interesante"
                $ tiempo_libre02 += 1
                jump darunavuelta
            
            "Fortalecerte":
                k "Despues de mi derrota a manos de esa cria, quiero volverme mas fuerte para asi poder patearle ese mini trasero respingon que tiene"
                $ tiempo_libre02 +=1
                jump fortalecerte
            
            "Intentar practicar esgrima":
                k "Creo que deberia mejorar mi tecnica con la espada, igual y todo consigo aprender a desollar culos ajenos"
                $ tiempo_libre02 +=1
                jump esgrima
            
            
            
            "Salir de caza":
                k "No creo que sea mala idea intentar cazar algo, por probar..."
                $ tiempo_libre02 +=1
                jump caza
            
            
            "Partir hacia el templo Ikarue":
                k "Sera mejor que parta ya al templo y no pierda mas el tiempo"
                $ tiempo_libre02 += 1
                jump ikarue
        
    else:
        $ renpy.music.play("musica/diasnormales.mp3")
        N "Notas como los primeros rayos de luz del sol entran por tus ojos"
        N "Te comienzas a sentir como nuevo, parece que todas las heridas que tenias han desaparecido"
        k "Buaaah, que bien he dormido."
        scene bg007 with dissolve
        N "Comienzas a desayunar, hoy vas a continuar la ultima parte del camino que te queda para llegar al templo"
        k "Bien, como parece que me he levantado pronto creo que puedo gastar un poco de ese tiempo en algo 'constructivo'"
        k "Oh quizas deberia de partir ya y no perder mas tiempo"
        
        menu:
            "Dar una vuelta por ahi":
                k "Visto lo visto, creo que lo mejor que puedo hacer es simplemente dar una vuelta por la zona a ver si hay algo interesante"
                $ tiempo_libre02 += 1
                jump darunavuelta
            
            "Fortalecerte":
                k "Despues de mi derrota a manos de esa cria, quiero volverme mas fuerte para asi poder patearle ese mini trasero respingón que tiene"
                $ tiempo_libre02 +=1
                jump fortalecerte
            
            "Intentar practicar esgrima":
                k "Creo que deberia mejorar mi tecnica con la espada, igual y todo consigo aprender a desollar culos ajenos"
                $ tiempo_libre02 +=1
                jump esgrima
            
            
            
            "Salir de caza":
                k "No creo que sea mala idea intentar cazar algo, por probar..."
                $ tiempo_libre02 +=1
                jump caza
            
            
            "Partir hacia el templo Ikarue":
                k "Sera mejor que parta ya al templo y no pierda mas el tiempo"
                jump ikarue
                
label fortalecerte:
    $ renpy.music.stop()
    $ renpy.music.play("musica/comi1.mp3")
    N "Comienzas a hacer flexiones"
    k "1.... 2.... 3.... 6.000.... 10.000..."
    k "Okay.. no cuela"
    k "Bueno... de algo ha debido de servir"
    N "Tu {b}defensa{/b} aumenta en 3 puntos"
    $ puntos_defensa += 3
    k "Bueno a otra cosa mariposa!"
    $ renpy.music.stop()
    $ renpy.music.play("musica/diasnormales.mp3")
    jump opcionesb
    
label esgrima:
    N "Te colocas enfrente de el tronco de un arbol muerto y desenvainas tu espada"
    k "Bien, veamos si puedo cortarlo"
    N "Comienzas a lanzar golpes con tu espada en el tronco del arbol"
    k "Gyaaa!"
    $ renpy.sound.play("musica/hit.ogg")
    k "Tengo que ser mejor, Gyaaa!!"
    $ renpy.sound.play("musica/hit.ogg")
    k "Mas"
    $ renpy.sound.play("musica/hit.ogg")
    k "Solo un poquito mas"
    $ renpy.sound.play("musica/hit.ogg")
    k "Vamos... EL GOLPE DE GRACIA!!"
    $ renpy.sound.play("musica/hit.ogg")
    N "Logras partir el tronco del arbol"
    k "Siiiii, lo logre!!"
    N "Tu {b}Fuerza{/b} aumenta en 5 puntos"
    $ puntos_fuerza += 5
    jump opcionesb
    
    
label caza: 
    N "Comienzas a andar en busca de una presa a la que cazar"
    N "Pasa un tiempo, pero no logras encontrar nada"
    jump opcionesb
    
   
label opcionesb:
    k "{i}¿Y ahora que deberia hacer?{/i}"
    
    menu:
        "Dar una vuelta por ahi":
            if tiempo_libre02 >= 2:
                k "No, ya no tengo tiempo que perder. Debo llegar ya al templo de Ikarue"
                jump ikarue
            else:
                k "Visto lo visto, creo que lo mejor que puedo hacer es simplemente dar una vuelta por la zona a ver si hay algo interesante"
                $ tiempo_libre02 += 1
                jump darunavuelta
                
        "Fortalecerte":
            if tiempo_libre02 >= 2:
                k "No, ya no tengo tiempo que perder. Debo llegar ya al templo de Ikarue"
                jump ikarue
                    
            else:    
                k "Despues de mi derrota a manos de esa cria, quiero volverme mas fuerte para asi poder patearle ese mini trasero respingón que tiene"
                $ tiempo_libre02 +=1
                jump fortalecerte
            
        "Intentar practicar esgrima":
            if tiempo_libre02 >= 2:
                k "No, ya no tengo tiempo que perder. Debo llegar ya al templo de Ikarue"
                jump ikarue
                    
            else:
                k "Creo que deberia mejorar mi tecnica con la espada, igual y todo consigo aprender a desollar culos ajenos"
                $ tiempo_libre02 +=1
                jump esgrima
            
            
            
        "Salir de caza":
            if tiempo_libre02 >= 2:
                k "No, ya no tengo tiempo que perder. Debo llegar ya al templo de Ikarue"
                jump ikarue
                    
            else:
                k "No creo que sea mala idea intentar cazar algo, por probar..."
                $ tiempo_libre02 +=1
                jump caza
            
            
        "Partir hacia el templo Ikarue":
            k "Sera mejor que parta ya al templo y no pierda mas el tiempo"
            jump ikarue
    
                
                
label darunavuelta:
    N "Comienzas a caminar sin rumbo por la zona"
    N "Antes de continuar con la partida, seria un buen momento para explicarte este tipo de accion"
    N "Cuando activas una accion con un contexto 'aleatorio' comenzara un evento aleatorio"
    N "Hay alrededor de 6 variables en esta ocasion especifica"
    N "Asi que siempre puedes re-jugar esta opcion para observar los cambios, dicho esto que continue la partida!"
    N "Hasta que te encuentras derepente..."
    $ d6 = renpy.random.randint(1, 1)
    if d6 == 1:
        N "Con una chica gnomo"
        show g
        G "Hola estupido humano!"
        G "Se ha perdido?"
        G "Los humanos sois una panda de atontaos, siempre que me encuentro con uno es por que se ha perdido el mu´tonto"
        k "{i}Por que narices todos los monstruos con los que me encuentro en mi viaje me desprecian por que soy humano?{/i}"
        k "Esto... No, simplemente estaba dando una vuelta"
        G "Eres el primer humano que conozco que hace semejantes tonterias, perdese por gusto...."
        k "Sabes, para ser tan pequeña lo unico que salen de tu boca son insultos y palabrotas"
        G "Gilipollas! soy un gnomo y tengo 120 años"
        k "Pero que cojones?"
        G "Bueno humano, ¿Que vas a hacer?, ¿Correr como una gallina?, ¿Gritar sin parar como una niñita?"
        G "Nose, simplemente digo lo que suelen hacer los de tu raza cuando ven a una de la mia"
        k "{i}La verdad es que no se que voy ha hacer...{/i}"
        
        menu:
            "Atacarla":
                k "{i}Esta visto y comprobado que los monstruos son todos iguales, asi que acabare con ella de inmediato{/i}"
                N "Desenvainas tu espada y te lanzas al combate"
                $ renpy.music.play("musica/iniciovs.mp3")
                jump combategnomo
                
            "Gritar como una niña":
                k "{i}Sinceramente nose por que voy a hacer esto, pero lo voy a hacer{/i}"
                k "Kyaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                N "Ves como la chica gnomo se comienza a alejar poco a poco"
                hide g
                show gs
                G "Dios, que patetico...."
                G "Me das verguenza ajena humano!!"
                G "Me largo de aqui antes de que alguien me ve contigo"
                N "Ves como la chica gnomo se da media vuelta y se va"
                k "Yeah!!, [k] wins!!"
                N "Levantas tus manos al aire en señal de victoria"
                jump opcionesb
                
            "Huir":
                k "{i}Si es como aquella mini chica, entonces se cumplira la regla de la mala hostia viene en frascos pequeños...{/i}"
                k "{i}Sera mejor que me largue antes de que intente patearme el culo{/i}"
                N "Comienzas a huir"
                G "Adios señor volao!"
                jump opcionesb
                
            "Pedirle que sea tu amiga":
                k "{i}Quien sabe igual y todo cuela...{/i}"
                k "Esto... Quisieras ser mi amiga, chica monstruo!?"
                G "{i}Se queda totalmente inmovil, casi como si fuera una estatua{/i}"
                G "Vale"
                N "Gnome se ha unido a tu grupo"
                $ grupo += 1
                k "{i}Solo puedo decir una cosa... no me lo esperaba sinceramente{/i}"
                jump opcionesantesdeikarue
                

label combategnomo:
    G "Realmente patetico"
    k "Eso ya lo veremos!"
    hide g
    show vsg
    N "{b}COMIENZA LA BATALLA{/b}"
    $ renpy.music.stop()
    $ renpy.music.play("musica/boss1.mp3")
    hide vsg
    show g
    $ puntos_fuerza_espejo = puntos_fuerza
    $ puntos_defensa_espejo = puntos_defensa
    $ puntos_vida_espejo = puntos_vida
    N "[k]: Fuerza = [puntos_fuerza] , Vida = [puntos_vida] , Defensa = [puntos_defensa] "
    N "[k] Inventario: Pociones de Vida [pociones_vida] , Pociones de Magia [pociones_magia] , Pociones de Estados [pociones_estados] , Bombas [bombas] "
    N "Lanzamiento de Iniciativa"
    $ d2 = renpy.random.randint(1, 2)
    N "Resultado del dado [d2]"
    
    if d2 == 1:
        N "Comienzas tu"
        N "Elige una acción"
        jump accionescombategnome
    else:
        N "Comienza tu oponente [G]"
        jump accionescombategnomeia
        
label accionescombategnome:
    $ defender = 0
    $ puntos_defensa_espejo = puntos_defensa
    $ vidapocion = 4
    N "[k]: Fuerza = [puntos_fuerza] , Vida = [puntos_vida] , Defensa = [puntos_defensa] "
    N "[k] Inventario: Pociones de Vida [pociones_vida] , Pociones de Magia [pociones_magia] , Pociones de Estados [pociones_estados] , Bombas [bombas] "
    
    menu:
        "{b}Ataque Fisico{/b}":
            N "Usas tu espada para golpear a [G]"
            $ renpy.sound.play("musica/hit.ogg")
            $ d5 = renpy.random.randint(1, 5)
            $ puntos_fuerza += d5
            $ puntos_fuerza -= defensaG
            $ dano += puntos_fuerza
            $ vidaG -= dano
            $ d3 = renpy.random.randint(1,3)
            if vidaG <= 0:
                G "Whoaaaa!!, señor humano es usted muy fuerte"
                $ puntos_fuerza = puntos_fuerza_espejo
                $ puntos_defensa = puntos_defensa_espejo
                $ dano = 0
                jump ganarG
                
            else:
                if d3 == 1:
                    k "Gyaaah!"
                    N "Logras hacerle [dano] de dano"
                    pause (1.0)
                    $ puntos_fuerza = puntos_fuerza_espejo
                    $ puntos_defensa = puntos_defensa_espejo
                    $ dano = 0
                    $IAG = renpy.random.randint(1, 3)
                    jump accionescombategnomeia
                if d3 == 2:
                    k "Este es tu fin chica Gnomo!!"
                    N "Logras hacerle [dano] de dano"
                    pause (1.0)
                    $ puntos_fuerza = puntos_fuerza_espejo
                    $ puntos_defensa = puntos_defensa_espejo
                    $ dano = 0
                    $IAG = renpy.random.randint(1, 3)
                    jump accionescombategnomeia
                if d3 == 3:
                    k "Whaaaaa!!!"
                    N "Logras hacerle [dano] de dano"
                    pause (1.0)
                    $ puntos_fuerza = puntos_fuerza_espejo
                    $ puntos_defensa = puntos_defensa_espejo
                    $ dano = 0
                    $IAG = renpy.random.randint(1, 3)
                    jump accionescombategnomeia
        
        
        "{b}Usar objeto{/b}":
            N "Buscas en tu inventario algun objeto"
            jump inventario
        
        "{b}Peticion{/b}":
            N "Todabia no conoces ninguna peticion"
            jump accionescombategnome
      
        "{b}Rendirte{/b}":
            N "Te rindes"
            jump rendiciondegnomo
        
        "{b}Defender{/b}":
            N "Te colocas en una posicion defensiva"
            if defender == 0:
                $ defender += 1
                $ d5 = renpy.random.randint(1, 5)
                $ puntos_defensa += d5
                $IAG = renpy.random.randint(1, 3)
                jump accionescombategnomeia
            else:
                N "Ya estas en una posicion defensiva"
                jump accionescombategnomeia
        
        "{b}Usar Habilidad{/b}":
            N "Todabia no conoces ninguna habilidad"
            jump accionescombategnome
            
        
        "{b}Usar Conjuro{/b}":
            N "Todabia no conoces ningun conjuro"
            jump accionescombategnomeia
        
        
        
label accionescombategnomeia:
    $ d3 = renpy.random.randint(1, 3)
    if d3 == 1:
        G "Empezemos a divertirnos humano!!"
        $IAG = renpy.random.randint(1, 2)
    if d3 == 2:
        N "Ves como la chica Gnomo comienza a lanzar puñetazos al aire como una boxeadora profesional"
        G "Voy a quebrar todos tus huesos!!"
        $IAG = renpy.random.randint(1, 2)
    if d3 == 3:
        N "La chica gnomo clava su mirada en ti"
        G "¿Cuantas costillas tendre que romperle señor humano para que entienda la diferencia entre monstruo y humano?"
        $IAG = renpy.random.randint(1, 2)
    if IAG == 1:
        N "Ves como el puño de la chica Gnomo comienza a tener una aura rojiza a su alrededor"
        N "No terminas de comprender que es, pero sientes que ese puño no es normal"
        G "ROUND FIGHT!!"
        G "{i}Lanza un puñetazo destructor{/i}"
        show punod
        $ renpy.sound.play("musica/bom1.ogg")
        show puno with Pause(0.5)
        hide punod
        hide puno
        $ d5 = renpy.random.randint(1, 5)
        $ d5 += fuerzaG
        $ fuerzaG -= puntos_defensa
        if fuerzaG <= 0:
            "Logras resistir el golpe y no te causa ningun daño"
            $ fuerzaG = 120
            $ defensaG = 323
            $ danoG = 0
            jump accionescombategnome
        else:
            $ danoG += fuerzaG
            $ puntos_vida -= danoG
        if puntos_vida <= 0:
            N "Te hace un total de [danoG] de dano"
            N "Dejandote a [puntos_vida] puntos de vida"
            N "Tu nariz comienza a sangrar fuertemente, por lo que comienzas sientes crees que te la has roto"
            N "Poco a poco el dolor se va extendiendo mas y mas, hasta recorrer por completo tu cuerpo"
            N "Sientes como si todos tus huesos quisieran salir despegados hasta el cielo"
            k "¿Que demonios eres tu? {i}Escupes sangre{/i}"
            G "¿Gnome se ha vuelto a pasar jugando a las luchas con los humanos? ¿huhu?"
            G "Los humanos sois juguetes que se rompen con facilidad"
            k "¿Ju-Juguetes?, aaahh"
            N "Te comienzas a sentir mareado, sientes como el golpe te esta dificultando respirar"
            G "Bueno, si no sirves para jugar a luchas. Serviras para otras cosas jijijijiji"
            k "{i}¿A que demonios se referira?{/i}"
            G "Dulces sueños, humano"
            N "Antes de que puedas reaccionar [G] se lanza encima tuya, tirandote al suelo"
            G "{i}Se comienza a sacar muñecos{/i}"
            k "{i}¿Es este mi fin?, mi cuerpo no me responde, la espada legendaria no es capaz de dañar a este monstruo...{/i}"
            k "{i}Espera un momento... aun podria salvarme... si lograse despertar de nuevo aquel poder...{/i}"
            k "{i}¿Deberia siquiera intentarlo?{/i}"
            N "Es el momento de explicar las tiradas de salvacion"
            N "Aveces cuando has sido derrotado en un combate o estas en un combate realmente dificil puedes intentar hacer una tirada de salvacion"
            N "Las tiradas de salvacion vendrian a ser una eleccion limite."
            N "Se lanzara 1d2 aleatorio, si su resultado es 1 obtendras una ultima oportunidad de ganar"
            N "Pero si encambio sale 2, perderas definitivamente el combate."
            N "No recibes ninguna penalización por negarte a hacerlo, asi que es recomendable intentarlo de todas maneras."
            $ fuerzaG = 120
            $ defensaG = 110
            $ danoG = 0
            $ vidaG = 432
            jump voluntad
            
        else:
            N "Te hace un total de [danoG] de dano"
            N "Dejandote a [puntos_vida] puntos de vida"
            pause(1.5)
            $ fuerzaG = 120
            $ defensaG = 110
            $ danoG = 0
            $ d2 = random.randint(1, 4)
        if d2 == 1:
            G "¿Has sobrevivido a mi golpe?"
            G "Milagroso!!"
            jump accionescombategnome2
        if d2 == 2:
            G "Parece que eres mas resistente de lo que pense, humano"
            G "Eso es bueno, asi me divertire quebrando esa resistencia!!!"
            jump accionescombategnome2
            
        
    if IAG == 2:
        N "Ves como la chica [G] desaparece durante un momento de tus ojos "
        $ renpy.sound.play("musica/desaparece.ogg")
        hide g
        show sonico
        N "Antes de que puedas reaccionar comienzas a sentir un monton de golpes por todo tu cuerpo"
        hide sonico
        show galleta with Pause(0.5)
        $ renpy.sound.play("musica/hit.ogg")
        $ renpy.sound.play("musica/hit.ogg")
        $ renpy.sound.play("musica/hit.ogg")
        $ renpy.sound.play("musica/hit.ogg")
        hide galleta
        show g
        $ d5 = renpy.random.randint(1, 5)
        $ d5 += fuerzaG
        $ fuerzaG -= puntos_defensa
        if fuerzaG <= 0:
            "Logras resistir el golpe y no te causa ningun daño"
            $ fuerzaG = 120
            $ defensaG = 110
            $ danoG = 0
            jump accionescombategnome
        else:
            $ danoG += fuerzaG
            $ puntos_vida -= danoG
        if puntos_vida <= 0:
            N "Te hace un total de [danoG] de dano"
            N "Dejandote a [puntos_vida] puntos de vida"
            N "Tu nariz comienza a sangrar fuertemente, por lo que crees que te la has roto"
            N "Poco a poco el dolor se va extendiendo mas y mas, hasta recorrer por completo tu cuerpo"
            N "Sientes como si todos tus huesos quisieran salir despegados hasta el cielo"
            k "¿Que demonios eres tu? {i}Escupes sangre{/i}"
            G "¿Gnome se ha vuelto a pasar jugando a las luchas con los humanos? ¿huhu?"
            G "Los humanos sois juguetes que se rompen con facilidad"
            k "¿Ju-Juguetes?, aaahh"
            N "Te comienzas a sentir mareado, sientes como el golpe te esta dificultando respirar"
            G "Bueno, si no sirves para jugar a luchas. Serviras para otras cosas jijijijiji"
            k "{i}¿A que demonios se referira?{/i}"
            G "Dulces sueños, humano"
            N "Antes de que puedas reaccionar [G] se lanza encima tuya, tirandote al suelo"
            G "{i}Se comienza a sacar muñecos{/i}"
            k "{i}¿Es este mi fin?, mi cuerpo no me responde, la espada legendaria no es capaz de dañar a este monstruo...{/i}"
            k "{i}Espera un momento... aun podria salvarme... si lograse despertar de nuevo aquel poder...{/i}"
            k "{i}¿Deberia siquiera intentarlo?{/i}"
            N "Es el momento de explicar las tiradas de salvacion"
            N "Aveces cuando has sido derrotado en un combate o estas en un combate realmente dificil puedes intentar hacer una tirada de salvacion"
            N "Las tiradas de salvacion vendrian a ser una eleccion limite."
            N "Se lanzara 1d2 aleatorio, si su resultado es 1 obtendras una ultima oportunidad de ganar"
            N "Pero si encambio sale 2, perderas definitivamente el combate."
            N "No recibes ninguna penalización por negarte a hacerlo, asi que es recomendable intentarlo de todas maneras."
            $ fuerzaG = 120
            $ defensaG = 110
            $ danoG = 0
            $ vidaG = 423
            jump voluntad
        else:
            N "Te hace un total de [danoG] de dano"
            N "Dejandote a [puntos_vida] puntos de vida"
            pause(1.5)
            $ fuerzaG = 120
            $ defensaG = 110
            $ danoG = 0
            G "¿Has sobrevivido a mi golpe?"
            G "Milagroso!!"
            jump accionescombategnome
        
        
label voluntad:
    if voluntad == 0:
        menu:
            "{b}Intentar despertar el Bhabhao{/b}":
                k "{i}Si lograse despertar ahora ese poder... podria acabar con esta chica monstruo. Debo intentarlo{/i}"
                N "Cierras tus ojos intentando concentrarte en las sensacciones que sentiste en tu encuentro con Chrome"
                $ voluntad += 1
                $ puntos_fuerza = puntos_fuerza_espejo
                $ puntos_defensa = puntos_defensa_espejo
                $ puntos_vida = puntos_vida_espejo
                $ puntos_fuerza_espejo = 0
                $ puntos_defensa_espejo = 0
                $ puntos_vida_espejo = 0
                $ d2 = renpy.random.randint(1, 2)
                if d2 == 1:
                    N "Notas como todo tu cuerpo comienza a exhalar vapor"
                    N "Tus musculos comienzan a tensarse, tu corazon comienza a latir cada vez mas y mas rapido"
                    N "Aprietas con fuerza tus nudillos, estas apunto de alcanzar el estado completo de Bhabhao"
                    N "Abres tus ojos y empujas con tus manos a [G], quitandola de encima tuya"
                    G "¿Que diablos eres humano?"
                    G "Mmmm, comienzo a sentir que tu poder es capaz de igualar al mio"
                    G "Juega una vez mas conmigo jueguete, y divirtamonos hasta el final!!"
                    N "Agarras con fuerza tu espada, te sientes en un estado de extasis. Ahora sientes que tienes las fuerzas necesarias para partir por la mitad el mundo si fuese necesario"
                    k "Menos hablar y mas luchar gnomo"
                    jump combatefinalgnome
                if d2 == 2:
                    N "Te empeñas en intentar sentir las mismas emociones que cuando Chrome te ataco, pero no eres capaz de lograrlo"
                    N "Notas como tu cuerpo se comienza a debilitar poco a poco"
                    N "Gnome comienza a moverse compulsivamente encima tuya"
                    k "{i}No... puedo... hacer... nada...{/i}"
                    jump hentaiG            
            "{b}Ceder a [G]{/b}":
                k "{i}No merece la pena intentar nada mas.. he sido derrotado... jamas llegare al templo{/i}"
                jump hentaiG
    if voluntad == 1:
        k "No... ya no puedo, ya gaste mi ultima oportunidad para luchar contra la chica gnomo"
        k "Mi cuerpo se ha quemado... Ya no puedo continuar luchando este es mi fin..."
        G "No, todabia no es tu fin humano"
        G "Ahora jugare con tu cuerpo, ya veras como sera divertido"
        jump hentaiG
        
           
label combatefinalgnome:
    N "COMIENZA EL COMBATE"
    N "Tus habilidades aumentan {b}19{/b} veces mas"
    $ puntos_fuerza_espejo = puntos_fuerza
    $ puntos_defensa_espejo = puntos_defensa
    $ puntos_vida_espejo = puntos_vida
    $ puntos_fuerza *= 19
    $ puntos_defensa *= 19
    $ puntos_vida *= 19
    $ puntos_fuerza_espejo2 = puntos_fuerza
    $ puntos_defensa_espejo2 = puntos_defensa
    $ puntos_vida_espejo2 = puntos_vida
    N "[k]: Fuerza = [puntos_fuerza] , Vida = [puntos_vida] , Defensa = [puntos_defensa] "
    N "[k] Inventario: Pociones de Vida [pociones_vida] , Pociones de Magia [pociones_magia] , Pociones de Estados [pociones_estados] , Bombas [bombas] "
    G "Veamos si ahora no te rompes con tanta facilidad juguete"
    k "Esta vez te detendre!!"
    N "Lanzamiento de iniciativa"
    $ d2 = renpy.random.randint(1, 2)
    
    if d2 == 1:
        N "Comienzas tu"
        N "Elige una acción"
        jump accionescombategnome2
        
    else:
        N "Comienza tu oponente [G]"
        jump accionescombategnomeia
        
    
    
label accionescombategnome2:
    $ renpy.music.stop()
    $ renpy.music.play("musica/voluntad.mp3")
    $ defender = 0
    $ puntos_defensa_espejo2 = puntos_defensa
    $ vidapocion = 4
    N "[k]: Fuerza = [puntos_fuerza] , Vida = [puntos_vida] , Defensa = [puntos_defensa] "
    N "[k] Inventario: Pociones de Vida [pociones_vida] , Pociones de Magia [pociones_magia] , Pociones de Estados [pociones_estados] , Bombas [bombas] "
    
    menu:
        "{b}Ataque Fisico{/b}":
            N "Usas tu espada para golpear a [G]"
            $ renpy.sound.play("musica/hit.ogg")
            $ d5 = renpy.random.randint(1, 5)
            $ puntos_fuerza += d5
            $ puntos_fuerza -= defensaG
            $ dano += puntos_fuerza
            $ vidaG -= dano
            $ d3 = renpy.random.randint(1,3)
            if vidaG <= 0:
                G "Whoaaaa!!, señor humano es usted muy fuerte"
                $ puntos_fuerza = puntos_fuerza_espejo2
                $ puntos_defensa = puntos_defensa_espejo2
                $ dano = 0
                jump ganarG
                
            else:
                if d3 == 1:
                    k "Gyaaah!"
                    N "Logras hacerle [dano] de dano"
                    pause (1.0)
                    $ puntos_fuerza = puntos_fuerza_espejo2
                    $ puntos_defensa = puntos_defensa_espejo2
                    $ dano = 0
                    $IAG = renpy.random.randint(1, 3)
                    jump accionescombategnomeia
                if d3 == 2:
                    k "Este es tu fin chica Gnomo!!"
                    N "Logras hacerle [dano] de dano"
                    pause (1.0)
                    $ puntos_fuerza = puntos_fuerza_espejo2
                    $ puntos_defensa = puntos_defensa_espejo2
                    $ dano = 0
                    $IAG = renpy.random.randint(1, 3)
                    jump accionescombategnomeia
                if d3 == 3:
                    k "Whaaaaa!!!"
                    N "Logras hacerle [dano] de dano"
                    pause (1.0)
                    $ puntos_fuerza = puntos_fuerza_espejo2
                    $ puntos_defensa = puntos_defensa_espejo2
                    $ dano = 0
                    $IAG = renpy.random.randint(1, 3)
                    jump accionescombategnomeia
        
        
        "{b}Usar objeto{/b}":
            N "Buscas en tu inventario algun objeto"
            jump inventario
        
        "{b}Peticion{/b}":
            N "Todabia no conoces ninguna peticion"
            jump accionescombategnome2
      
        "{b}Rendirte{/b}":
            N "Te rindes"
            jump rendiciondegnomo
        
        "{b}Defender{/b}":
            N "Te colocas en una posicion defensiva"
            if defender == 0:
                $ defender += 1
                $ d5 = renpy.random.randint(1, 5)
                $ puntos_defensa += d5
                $IAG = renpy.random.randint(1, 3)
                jump accionescombategnomeia
            else:
                N "Ya estas en una posicion defensiva"
                jump accionescombategnomeia
        
        "{b}Usar Habilidad{/b}":
            N "Todabia no conoces ninguna habilidad"
            jump accionescombategnome2
            
        
        "{b}Usar Conjuro{/b}":
            N "Todabia no conoces ningun conjuro"
            jump accionescombategnome2
    
    
                
    
                   
        
               
label hentaiG:     
    N "Los muñecos de Gnome comienzan a atrapar tus miembros, imposibilitandote de esta manera que puedas moverte"
    G "{i}Comienza a desnudarse{/i}"
    k "{i}No tengo mas fuerzas... tan solo me queda ceder..{/i}"
    hide g
    G "{i}Sonrie{/i} Parece que te niegas a admitir que te gusta"
    
    if persistent.hentai == True:
        $ renpy.music.stop()
        $ renpy.music.play("musica/game_over.ogg")
        show hg
        G "Tu pene esta erecto, tan solo disfruta de mi cuerpo y no opongas resistencia"
        G "Sera mejor asi señor humano, por que pienso dejarlo seco"
        k "Ahhh, Ahhh, Ahhh"
        N "Sientes como el extasis recorre todo tu cuerpo, comienzas a ceder ante los movimientos de [G]"
        G "Ves humano, en el fondo de tu ser eres un deprabado. Por mucho que sigas a esa estupida religion"
        G "En el fondo, ansias complacer tus instintos mas basicos. Disfruta, disfruta del placer que te estoy otorgando humano"
        G "{i}Comienza a arremeter con mas fuerza sobre tu pelvis{/i}"
        k "Ahhh, si sigues asi... yo... yo.. me desvanecere"
        G "Eso es lo que quiero humano, dame toda tu energia. No te quedes ni una sola gota dentro de ti"
        hide hg
        show hg2
        k "{i}Noto como mi esperma comienza a fluir sin cesar, ya no me queda voluntad para negarme...{/i}"
        N "Comienzas a mostrar una sonrisa en tu rostro"
        $ renpy.sound.play("musica/semen.ogg")
        hide hg2
        show hg3
        k "AAAAAAAAAAAHHHHh!!!!"
        $ renpy.sound.play("musica/semen.ogg")
        $ renpy.sound.play("musica/semen.ogg")
        hide hg3
        show hg4
        G "Mmmmm, ¿has lanzado tanto semen y aun continuas con vida?"
        G "{i}Muestra una sonrisa bastante deprabada{/i}"
        G "Me gusta y encima parece que tienes aguante para mas. Sigamos hasta tu ultimo aliento!!"
        N "Acabaste convertido en un siervo de [G], tu viaje acabo aqui y jamas llegaste al templo de Ikarue"
        N "Aun asi, no crees que convertirte en el siervo de [G] sea mala forma de acabar tu viaje"
        N "Game Over"
        return
        
        
        
        
        
    else:
        $ renpy.music.stop()
        $ renpy.music.play("game_over.ogg")
        show hgc
        k "{i}Noto como mis fuerzas se comienzan a desvanecer, ella arremete con fuerza contra mi pelvis sin que pueda frenarla{/i}"
        N "Tus ojos comienzan a cerrarse lentamente... Tu final ya ha llegado"
        N "De ahora en adelante seras un exclavo de [G] hasta el fin de tus dias"
        N "Jamas llegaras al templo de Ikarue, ni mucho menos serviras a las ordenes de la diosa Irias"
        N "Tu corto viaje acabo aqui"
        N "GAME OVER"
        return
                                                                                                                                   
    

label rendiciondegnomo:
    
    $ renpy.music.stop()
    $ renpy.music.play("game_over.ogg")
    N "Tiras tus armas al suelo en señal de rendición"
    k "{i}No tengo ninguna oportunidad con un monstruo como ella... sera mejor que me rinda{/i}"
    G "Eres un juguete aburrido {i}incha los mofletes{/i}"
    G "Pero bueno, ahora te sacare tu energia"
    G "{i}Se saca unos muñecos y se pone encima tuya{/i}"
    jump hentaiG

  
  
label ikarue:
    $ renpy.music.stop()
    $ renpy.music.play("musica/preparate.mp3")
    k "Por fin, ya estoy en marcha hacia mi destino. Se que ha habido algunas dificultades en mi camino hasta ahora, pero si no comienzo"
    k "a ser mas fuerte que esas dificultades jamas lograre cumplir mi sueño"
    k "Por ello quiero prometerme a mi mismo, que apartir de aqui, de ahora en adelante no volvere a ser derrotado por nadie."
    k "Pase lo que pase, sea quien sea, debo ser capaz de volverme mas fuerte cuando la situacion lo requiera."
    k "Esto no es un juego y no hay segundas oportunidades, estoy totalmente preparado."
    k "Asi que sea cual sea mi proximo rival, pienso vencerlo!!!"
    N "Continuas caminado durante varias horas hasta que por fin llegas al templo de Ikarue"
    scene t
    k "Ya he llegado, ya he llegado!!"
    k "{i}Si, la verdad es que debo de parecer un crio gritando como un loco por haber llegado hasta aqui, pero me da igual. Lo he logrado!!{/i}"
    N "Antes de que puedas hacer nada un hombre te agarra de tu brazo izquierdo con mucha fuerza"
    N "No eres capaz de girarte para poder ver quien es, pero escuchas su voz"
    K "¿Se puede saber quien a dejado suelto a un crio por el templo?"
    k "{i}¿Quien diablos es este tipo?, me esta agarrando con mucha fuerza y no estoy de humor para estas tonterias{/i}"
    N " Te suelta y te empuja hacia adelante"
    show K
    K "Bien dado que nadie parece responder por ti niño, me lo explicaras tu"
    K "¿Que narices haces aqui?"
    k "Para empezar no soy ningun niño, segundo me llamo [k] y voy a ser el proximo caballero sagrado de la diosa Irias"
    hide K
    show KB
    hide KB
    show K
    K "Crios...."
    K "{i}Resopla{/i}"
    K "Mira este no es sitio para crios que quieren jugar a ser heroes"
    K "Estoy bastante falto de tiempo para poder lidiar con un crio como tu ahora mismo, ¿asi que por que no das media vuelta y vuelves a tu casita?"
    k "{i}Demonios... ¿como puedo convencer a este tipejo de que soy un elegido de Irias?{/i}"
    
    menu:
        "Enseñarle la espada":
            k "{i}Ya esta, si le enseño mi espada seguro que me acabara creyendo{/i}"
            N "Desenvainas tu espada"
            k "Veamos señor soy demasiado atontado como para no ver la verdad delante de mis ojos. ¿Un crio llevaria una espada como esta?"
            hide K
            show KC
            hide KC
            show K
            K "Tch......"
            K "He visto mocosos con muchisimo ego en mi vida que portaban espadas tan grandes como edificios"
            K "Quizas sea cierto que esa espada no parece normal"
            K "Pero me apuesto lo que quieras a que no tienes ni la mas minima idea de su poder"
            k "¿Y tu que narices sabras ?"
            k "{i}Este tio me esta sacando realmente dequicio, estoy tan cerca de cumplir mi objetivo y tiene que estar aqui mareando la perdíz{/i}"
            K "Venga, te dare una misera oportunidad por que me recuerdas a mi juventud"
            K "Dame tu mejor golpe con esa espada y entonces decidire si eres apto o no"
            k "{i}¿Deverdad este tio quiere que le golpe con mi espada? ¿Sabe que si hago eso podria matarlo?"
            K "¿Aque estas esperando?"
            K "No voy a defenderme de el, esta es tu oportunidad chaval"
            k "Intentare hacerte demasiado daño viejales!"
            hide K
            show KC
            K "¡¡¡¡¿¿¿AQUIEN NARICES ESTAS LLAMANDO VIEJALES???!!!!"
            hide KC
            show K
            N "Coges carrerilla y saltas encima de [K] a golpearle"
            k "Gyaaaaaaaaaah"
            $ renpy.sound.play("musica/hit.ogg")
            N "Ves como le has golpeado de lleno en el torso, pero no has logrado hacerle ningun tipo de daño. Incluso sus ropas estan completamente intactas"
            K "Pues como decia, que no tienes ni idea del poder de tu arma ni mucho menos sabes luchar"
            k "¿Pe-Pero, como es posible que mi ataque no te haya echo nada?"
            K "Veras, explicarte eso seria algo largo y aburrido. Y como veras ya te dije antes que no tengo mucho tiempo para tonterias"
            K "La verdad es que me has entretenido un rato, asi que por eso te dejare que te quedes por aqui."
            K "Pero si te vuelvo a ver en mi camino te echare a patadas de aqui. ¿Entendido?"
            k "Esto.. Si...."
            K "Bien, adios"
            hide K
            k "{i}¿Que diablos acaba de pasar?, bueno sera mejor que me de prisa y vaya a hablar con el clerigo del templo. Seguro que el me entiende{/i}"
            k "{i}Y ya puestos, quizas me de algunas respuestas{/i}"
        
        "Intentar despertar tu poder":
            "NADA"
    
  
    
label extras:
    show ex
                                                                    
    $ passworld = renpy.input("Inserte la Contraseña: \n{i}Usa Backspace para borrar el texto. \nPulsa Enter para confirmar{/i}",
"Nada", length=20)
    $ passworld = passworld.strip()
    
    if passworld == "CHETOS!":
        N "La contraseña es correcta"
        
    else:
        N "La contraseña es incorrecta"
    
    
            
        
        

    
        



    return
