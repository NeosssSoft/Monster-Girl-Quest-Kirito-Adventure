# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.
# - Este archivo se encuentra en el dominio público. Puede ser modificado
#   libremente como base para tus propias pantallas.

##############################################################################
# Say - Diálogo
#
# Screen that's used to display adv-mode dialogue.
# - Pantalla utilizada para presentar el diálogo en modo adv.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:

    # Defaults for side_image and two_window
    # - Valores por defecto de 'side_image' y 'two_window'
    default side_image = None
    default two_window = False

    # Decide if we want to use the one-window or two-window variant.
    # - Opta entre las variantes de una ventana o dos ventanas.
    if not two_window:

        # The one window variant.
        # - Una ventana.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        # - Dos ventanas.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    # - Si hay una imagen lateral, la presenta sobre el texto.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    # - Usa el menú de acceso rápido.
    use quick_menu


##############################################################################
# Choice - Elecciones
#
# Screen that's used to display in-game menus.
# - Pantalla utilizada para presentar los menus dentro del juego.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2 python:
    config.narrator_menu = True

    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = int(config.screen_width * 0.75)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.75)


##############################################################################
# Input - Entrada
#
# Screen that's used to display renpy.input()
# - Pantalla utilizada para la entrada de texto por parte del usuario.
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# - Pantalla utilizada para el diálogo y los menús en modo nvl.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        # - Presenta el diálogo.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        # - Presenta un menú, si lo hay.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu - Menú principal
#
# Screen that's used to display the main menu, when Ren'Py first starts
# - Pantalla utilizada para presentar el menú principal, cuando Ren'Py empieza
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu:

    # This ensures that any other menu screen is replaced.
    # - Esta linea asegura que las otras pantallas de menú son reemplazadas.
    tag menu

    # The background of the main menu.
    # - Fondo del menú principal.
    window:
        image "fondo.png"
        style "mm_root"

    # The main menu buttons.
    # - Botones del menú principal.
    frame:
        style_group "mm"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Nueva Partida") action Start() 
        textbutton _("Cargar Partida") action ShowMenu("load")
        textbutton _("Galeria") action ShowMenu("cg_gallery")
        textbutton _("Preferencias") action ShowMenu("preferences")
        textbutton _("Extras") action Start("extras")
        textbutton _("Ayuda") action Help()
        textbutton _("Salir") action Quit(confirm=False) 

init -2 python:

    # Make all the main menu buttons be the same size.
    # - Ajusta todos los botones del menú principal al mismo tamaño.
    style.mm_button.size_group = "mm"


##############################################################################
# Navigation - Navegación
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# - Pantalla incluida en otras pantallas para presentar las opciones de 
#   navegación y el fondo en los menús del juego.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:

    # The background of the game menu.
    # - Fondo de los menús del juego.
    window:
        style "gm_root"

    # The various buttons.
    # - Botones de navegación.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Atras") action Return()
        textbutton _("Preferencias") action ShowMenu("preferences")
        textbutton _("Guardar Juego") action ShowMenu("save")
        textbutton _("Cargar Juego") action ShowMenu("load")
        textbutton _("Menu Principal") action MainMenu()
        textbutton _("Ayuda") action Help()
        textbutton _("Salir") action Quit()

init -2 python:
    style.gm_nav_button.size_group = "gm_nav"


##############################################################################
# Save, Load - Guardar, Cargar
#
# Screens that allow the user to save and load the game.
# - Pantallas que permiten al usuario guardar y cargar las partidas.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.
# - Ya que guardar y cargar son muy similares, se combinan en una sola
#   pantalla, selector de archivo ('file_picker'). Esa se usa desde
#   simples pantallas de guardado y carga.

screen file_picker:

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        # - Los botones superiores permiten al usuario escoger entre
        #   páginas de archivos.
        hbox:
            style_group "file_picker_nav"

            textbutton _("Previo"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Siguiente"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5

        # Display a grid of file slots.
        # - Presenta una cuadrícula de espacios para archivos.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            # - Presenta diez espacios para archivos, numerados de 1 a 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                # - Cada espacio es un botón.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    # - Añade la captura de pantalla.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save:

    # This ensures that any other menu screen is replaced.
    # - Esta linea asegura que las otras pantallas de menú son reemplazadas.
    tag menu

    use navigation
    use file_picker

screen load:

    # This ensures that any other menu screen is replaced.
    # - Esta linea asegura que las otras pantallas de menú son reemplazadas.
    tag menu

    use navigation
    use file_picker

init -2 python:
    style.file_picker_frame = Style(style.menu_frame)

    style.file_picker_nav_button = Style(style.small_button)
    style.file_picker_nav_button_text = Style(style.small_button_text)

    style.file_picker_button = Style(style.large_button)
    style.file_picker_text = Style(style.large_button_text)



##############################################################################
# Preferences - Opciones
#
# Screen that allows the user to change the preferences.
# - Pantalla que permite al usuario cambiar las opciones.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences:

    tag menu

    # Include the navigation.
    # - Incluye la navegación.
    use navigation

    # Put the navigation columns in a three-wide grid.
    # - Coloca las columnas de navegación en una cuadrícula de anchura 3.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        # - Columna izquierda.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Ventana") action Preference("display", "window")
                textbutton _("Pantalla Completa") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Transiciones")
                textbutton _("Todas") action Preference("transitions", "all")
                textbutton _("Ningua") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Velocidad de Texto")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")
                
            frame:
                style_group "pref"
                has vbox
                
                label _("Hentai")
                textbutton _("Si") action SetField(persistent, "hentai", True)
                textbutton _("No") action SetField(persistent, "hentai", False)


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Mensajes Vistos") action Preference("skip", "seen")
                textbutton _("Todos Los Mensajes") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Comenzar Salto") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("Despues de las elecciones")
                textbutton _("Parar salto") action Preference("after choices", "stop")
                textbutton _("Seguir Salto") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Veloc. Auto-avance")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("Esperar a la Voz") action Preference("wait for voice", "toggle")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Volumen de Musica")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Volumen de los Sonidos")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Voice Volume")
                    bar value Preference("voice volume")

                    textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Test"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"

init -2 python:
    style.pref_frame.xfill = True
    style.pref_frame.xmargin = 5
    style.pref_frame.top_margin = 5

    style.pref_vbox.xfill = True

    style.pref_button.size_group = "pref"
    style.pref_button.xalign = 1.0

    style.pref_slider.xmaximum = 192
    style.pref_slider.xalign = 1.0

    style.soundtest_button.xalign = 1.0


##############################################################################
# Yes/No Prompt - Pregunta Sí/No
#
# Screen that asks the user a yes or no question.
# - Pantalla que pregunta al usuario una pregunta Sí/No.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Si") action yes_action
            textbutton _("No") action no_action

    # Right-click and escape answer "no".
    # - Clic derecho y escape responden "no".
    key "game_menu" action no_action

init -2 python:
    style.yesno_button.size_group = "yesno"
    style.yesno_label_text.text_align = 0.5
    style.yesno_label_text.layout = "subtitle"


##############################################################################
# Quick Menu - Menú de acceso rápido
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
# - Pantalla incluida por defecto en la pantalla de diálogo, que añade acceso
#   rápido a una serie de funciones útiles.
screen quick_menu:

    # Add an in-game quick menu.
    # - Añade un menú de acceso rápido interno al juego.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Atras") action Rollback()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Skip") action Skip()
        textbutton _("F.Skip") action Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')

init -2 python:
    style.quick_button.set_parent('default')
    style.quick_button.background = None
    style.quick_button.xpadding = 5

    style.quick_button_text.set_parent('default')
    style.quick_button_text.size = 12
    style.quick_button_text.idle_color = "#8888"
    style.quick_button_text.hover_color = "#ccc"
    style.quick_button_text.selected_idle_color = "#cc08"
    style.quick_button_text.selected_hover_color = "#cc0"
    style.quick_button_text.insensitive_color = "#4448"
    
    
###
init python:
    #Galleries settings - start
    #list the CG gallery images here:
    gallery_cg_items = ["cg1", "cg2", "cg3", "cg4", "cg5", "cg6", "cg7", "cg8", "cg9", "cg10"]
    #list the BG gallery images here (if a BG includes several variations, such as night version, include only one variation here):
    gallery_bg_items = ["bg kitchen", "bg road"]
    #how many rows and columns in the gallery screens?
    gal_rows = 3
    gal_cols = 3
    #thumbnail size in pixels:
    thumbnail_x = 200
    thumbnail_y = 150
    #the setting above (267x150) will work well with 16:9 screen ratio. Make sure to adjust it, if your are using 4:3 or something else.
    #Galleries settings - end
   
    gal_cells = gal_rows * gal_cols   
    g_cg = Gallery()
    for gal_item in gallery_cg_items:
        g_cg.button(gal_item + " butt")
        g_cg.image(gal_item)
        g_cg.unlock(gal_item)
    g_cg.transition = fade
    cg_page=0

    g_bg = Gallery()
    for gal_item in gallery_bg_items:
        g_bg.button(gal_item + " butt")
        g_bg.image(gal_item)
        g_bg.unlock(gal_item)
        #if BGs have variations, such as night version, uncomment the lines below and include the code for each BG with variations
        #if gal_item == "bg001":
            #g_bg.image("bg001")
            #g_bg.unlock("bg001")
    g_bg.transition = fade
    bg_page=0

init +1 python:
    #Here we create the thumbnails. We create a grayscale thumbnail image for BGs, but we use a special "locked" image for CGs to prevent spoilers.
    for gal_item in gallery_cg_items:
        renpy.image (gal_item + " butt", im.Scale(ImageReference(gal_item), thumbnail_x, thumbnail_y))
   
   
       
screen cg_gallery:
    tag menu
    use navigation
    frame background None xpos 10:
        grid gal_rows gal_cols:
            ypos 10
            $ i = 0
            $ next_cg_page = cg_page + 1           
            if next_cg_page > int(len(gallery_cg_items)/gal_cells):
                $ next_cg_page = 0
            for gal_item in gallery_cg_items:
                $ i += 1
                if i <= (cg_page+1)*gal_cells and i>cg_page*gal_cells:
                    add g_cg.make_button(gal_item + " butt", gal_item + " butt",  im.Scale("gallocked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
            for j in range(i, (cg_page+1)*gal_cells): #we need this to fully fill the grid
                null
        frame:
            yalign 0.97
            vbox:
                if len(gallery_cg_items)>gal_cells:
                    textbutton _("Siguiente Pagina") action [SetVariable('cg_page', next_cg_page), ShowMenu("cg_gallery")]

screen bg_gallery:
#The BG gallery screen is more or less copy pasted from the CG screen above, I only changed "make_button" to include a grayscale thumbnail for locked items
    tag menu
    use navigation
    frame background None xpos 10:
        grid gal_rows gal_cols:
            ypos 10
            $ i = 0
            $ next_bg_page = bg_page + 1
            if next_bg_page > int(len(gallery_bg_items)/gal_cells):
                $ next_bg_page = 0
            for gal_item in gallery_bg_items:
                $ i += 1
                if i <= (bg_page+1)*gal_cells and i>bg_page*gal_cells:
                    add g_bg.make_button(gal_item + " butt", gal_item + " butt", gal_item + " butt dis", xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
            for j in range(i, (bg_page+1)*gal_cells):
                null
        frame:
            yalign 0.97
            vbox:
                if len(gallery_bg_items)>gal_cells:
                    textbutton _("Next Page") action [SetVariable('bg_page', next_bg_page), ShowMenu("bg_gallery")]
