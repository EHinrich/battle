
init -1 python:
    import math

init python:
    class Player:

        def __init__(self, character, name, unit_type, image, image_attacked, image_healing, attack = 10, health = 100, currenthp = 100, Xpos = 60, Ypos = 500, amount = 1, defense = 5, speed = 1, strong_attack_turn = 0, count_ice_arrow = 3, ice_arrow_used = False, healing = 10):
            self.c = character
            self.name = name
            self.attack = attack
            self.unit_type = unit_type
            self.image = image
            self.image_attacked = image_attacked
            self.image_healing = image_healing
            self.health = health
            self.currenthp = currenthp
            self.Xpos = Xpos
            self.Ypos = Ypos
            self.amount = amount
            self.defense = defense
            self.speed = speed
            self.strong_attack_turn = strong_attack_turn
            self.count_ice_arrow = count_ice_arrow
            self.ice_arrow_used = ice_arrow_used
            self.healing = healing

    class Enemy:

        def __init__(self, character, name, unit_type, image, image_attacked, attack = 10, health = 100, currenthp = 100, Xpos = 1685, Ypos = 560, e = [], amount = 1, defense = 5, speed = 1, count_ice_arrow = 3):
            self.c = character
            self.name = name
            self.attack = attack
            self.image_attacked = image_attacked
            self.unit_type = unit_type
            self.image = image
            self.health = health
            self.currenthp = currenthp
            self.Xpos = Xpos
            self.Ypos = Ypos
            self.e = e
            self.amount = amount
            self.defense = defense
            self.speed = speed
            self.count_ice_arrow = count_ice_arrow


default space_Y = 175
default space_X = 175
default error = 50
default x = 12
default y = 6
default attacked = "_attacked"
default field_space_x = 100
default field_space_y = 10
default field_space_menu = 200
default description_space_x = 400
default description_space_y = 200

######################
default attack_factor = 2
default attack_factor_ice_arrow = 1
default count_ice_arrow = 0
######################

screen field:
    add "images/map.jpg"
    #frame:
        #ypos 0
        #xpos 1835
    #frame:
        #ypos 0
        #xpos -1828
    frame:
        xpos 0
        ypos -1055
    frame:
        xpos 0
        ypos 893

transform player_active(Xpos, Ypos, player_image):
    player_image
    ypos Ypos
    xpos Xpos
    linear 1.5 ypos Ypos + 20
    linear 1.5 ypos Ypos
    repeat

transform enemy_active(Xpos, Ypos, enemy_image):
    enemy_image
    ypos Ypos
    xpos Xpos
    linear 1.5 ypos Ypos + 20
    linear 1.5 ypos Ypos
    repeat

screen enemy_active_screen(enemy, enemy_list):
    for enemy_tmp in enemy_list:
        if enemy_tmp != enemy:
            add enemy_tmp.image xpos enemy_tmp.Xpos ypos enemy_tmp.Ypos
        else:
            add enemy_active(enemy.Xpos, enemy.Ypos, enemy.image)
        bar:
            value enemy_tmp.currenthp 
            range enemy_tmp.health 
            xpos enemy_tmp.Xpos - 10
            xmaximum 150
            ypos enemy_tmp.Ypos + 125
            ysize 30
        text "{size=20}{color=#000}HP: [enemy_tmp.currenthp]/[enemy_tmp.health]{/color}{/size}" xpos enemy_tmp.Xpos ypos enemy_tmp.Ypos + 130
        frame:
            text str(enemy_tmp.amount) xalign 0.5 yalign 0.5
            xpos enemy_tmp.Xpos - 35
            ypos enemy_tmp.Ypos + 115


screen player(player_list):
    for player in player_list:
        if player_list.index(player) == 0:
            add player_active(player.Xpos, player.Ypos, player.image) 
        else:
            add player.image xpos player.Xpos ypos player.Ypos
        bar:
            value player.currenthp
            range player.health
            xpos player.Xpos - 10
            #ypos player.Ypos + 115
            xmaximum 150
            ypos player.Ypos + 125
            ysize 30
            #left_bar Frame(im.Twocolor("_theme_diamond/dslider_full.png", "#41d307", "#41d307"), 12, 0)
            #right_bar Frame(im.Twocolor("_theme_diamond/dslider_empty.png", "#41d307", "#41d307"), 12, 0)
        text "{size=20}{color=#000}HP: [player.currenthp]/[player.health]{/color}{/size}" xpos player.Xpos ypos player.Ypos + 130
        frame:
            text str(player.amount) xalign 0.5 yalign 0.5
            xpos player.Xpos - 35
            ypos player.Ypos + 115

screen player_healing_current(player_list):
    for player in player_list:
        if player_list.index(player) == 0:
            add player.image_healing xpos player.Xpos ypos player.Ypos 
        else:
            add player.image xpos player.Xpos ypos player.Ypos
        bar:
            value player.currenthp
            range player.health
            xpos player.Xpos - 10
            xmaximum 150
            ypos player.Ypos + 125
            ysize 30
        text "{size=20}{color=#000}HP: [player.currenthp]/[player.health]{/color}{/size}" xpos player.Xpos ypos player.Ypos + 130
        frame:
            text str(player.amount) xalign 0.5 yalign 0.5
            xpos player.Xpos - 35
            ypos player.Ypos + 115

screen player_inactive:
    for player in player_list:
        add player.image xpos player.Xpos ypos player.Ypos
        bar:
            value player.currenthp
            range player.health
            xpos player.Xpos - 10
            xmaximum 150
            ypos player.Ypos + 125
            ysize 30
        text "{size=20}{color=#000}HP: [player.currenthp]/[player.health]{/color}{/size}" xpos player.Xpos ypos player.Ypos + 130
        frame:
            text str(player.amount) xalign 0.5 yalign 0.5
            xpos player.Xpos - 35
            ypos player.Ypos + 115


screen player_attacked(player):
    for player_tmp in player_list:
        if player_tmp == player:
            add player.image_attacked xpos player.Xpos ypos player.Ypos-10
        else:
            add player_tmp.image xpos player_tmp.Xpos ypos player_tmp.Ypos
        bar:
            value player_tmp.currenthp
            range player_tmp.health
            xpos player_tmp.Xpos -10
            xmaximum 150
            ypos player_tmp.Ypos + 125
            ysize 30
        text "{size=20}{color=#000}HP: [player_tmp.currenthp]/[player_tmp.health]{/color}{/size}" xpos player_tmp.Xpos ypos player_tmp.Ypos + 130
        frame:
            text str(player_tmp.amount) xalign 0.5 yalign 0.5
            xpos player_tmp.Xpos - 35
            ypos player_tmp.Ypos + 115


screen enemy(enemy_list):
    for enemy in enemy_list:
        add enemy.image xpos enemy.Xpos ypos enemy.Ypos
        bar:
            value enemy.currenthp 
            range enemy.health 
            xpos enemy.Xpos - 10
            xmaximum 150
            ypos enemy.Ypos + 125
            ysize 30
        text "{size=20}{color=#000}HP: [enemy.currenthp]/[enemy.health]{/color}{/size}" xpos enemy.Xpos ypos enemy.Ypos + 130
        frame:
            text str(enemy.amount) xalign 0.5 yalign 0.5
            xpos enemy.Xpos - 35
            ypos enemy.Ypos + 115


screen enemy_attacked(current_name):
    for enemy_tmp in enemy_list:
        if enemy_tmp.name == current_name:
            if strong_attack == True:
                if player.attack*player.amount > enemy_tmp.defense:
                    on "show" action SetField(enemy_tmp, "currenthp", enemy_tmp.currenthp-player.attack*player.amount*attack_factor+enemy_tmp.defense)
                    if enemy_tmp.currenthp-player.attack*player.amount*attack_factor+enemy_tmp.defense <= 0 and enemy_tmp.amount > 0:
                        on "show" action [SetField(enemy_tmp, "currenthp", enemy_tmp.health), SetField(enemy_tmp, "amount", enemy_tmp.amount - 1)]
                add enemy_tmp.image_attacked xpos enemy_tmp.Xpos ypos enemy_tmp.Ypos-10
                on "show" action SetField(player, "strong_attack_turn", player.strong_attack_turn+1)
            else:
                if player.attack*player.amount > enemy_tmp.defense:
                    on "show" action SetField(enemy_tmp, "currenthp", enemy_tmp.currenthp-player.attack*player.amount+enemy_tmp.defense)
                    if enemy_tmp.currenthp-player.attack*player.amount+enemy_tmp.defense <= 0 and enemy_tmp.amount > 0:
                        on "show" action [SetField(enemy_tmp, "currenthp", enemy_tmp.health), SetField(enemy_tmp, "amount", enemy_tmp.amount - 1)]
                add enemy_tmp.image_attacked xpos enemy_tmp.Xpos ypos enemy_tmp.Ypos-10
            if strong_attack_2 == True:
                on "show" action SetField(player, "strong_attack_turn", player.strong_attack_turn+1)
            if ice_arrow == True:
                if enemy_tmp.unit_type == "warrior":
                    on "show" action SetField(enemy_tmp, "e", [[enemy_tmp.Xpos + space_X, enemy_tmp.Ypos], [enemy_tmp.Xpos - space_X, enemy_tmp.Ypos], [enemy_tmp.Xpos, enemy_tmp.Ypos + space_Y], [enemy_tmp.Xpos, enemy_tmp.Ypos - space_Y], [enemy_tmp.Xpos + space_X, enemy_tmp.Ypos + space_Y],
                    [enemy_tmp.Xpos + space_X, enemy_tmp.Ypos - space_Y], [enemy_tmp.Xpos - space_X, enemy_tmp.Ypos - space_Y], [enemy_tmp.Xpos - space_X, enemy_tmp.Ypos + space_Y]])
                if enemy_tmp.unit_type == "wizard":
                    on "show" action SetField(enemy_tmp, "e", [[enemy_tmp.Xpos + space_X, enemy_tmp.Ypos], [enemy_tmp.Xpos - space_X, enemy_tmp.Ypos], [enemy_tmp.Xpos, enemy_tmp.Ypos + space_Y], [enemy_tmp.Xpos, enemy_tmp.Ypos - space_Y], [enemy_tmp.Xpos + space_X, enemy_tmp.Ypos + space_Y],
                    [enemy_tmp.Xpos + space_X, enemy_tmp.Ypos - space_Y], [enemy_tmp.Xpos - space_X, enemy_tmp.Ypos - space_Y], [enemy_tmp.Xpos - space_X, enemy_tmp.Ypos + space_Y]])
                if enemy_tmp.unit_type == "archer":
                    on "show" action SetField(enemy_tmp, "e", [])
                on "show" action SetField(enemy_tmp, "count_ice_arrow", 0)
                on "show" action SetField(enemy_tmp, "speed", enemy_tmp.speed - 1)
                on "show" action SetField(player, "ice_arrow_used", True)

        else:
            add enemy_tmp.image xpos enemy_tmp.Xpos ypos enemy_tmp.Ypos
        if enemy_tmp.amount > 0:
            bar:
                value enemy_tmp.currenthp 
                range enemy_tmp.health 
                xpos enemy_tmp.Xpos - 10
                xmaximum 150
                ypos enemy_tmp.Ypos + 125
                ysize 30
            text "{size=20}{color=#000}HP: [enemy_tmp.currenthp]/[enemy_tmp.health]{/color}{/size}" xpos enemy_tmp.Xpos ypos enemy_tmp.Ypos + 130
            frame:
                text str(enemy_tmp.amount) xalign 0.5 yalign 0.5
                xpos enemy_tmp.Xpos - 35
                ypos enemy_tmp.Ypos + 115
        else:
            bar:
                value 0
                range enemy_tmp.health 
                xpos enemy_tmp.Xpos - 10
                xmaximum 150
                ypos enemy_tmp.Ypos + 125
                ysize 30
            text "{size=20}{color=#000}HP: 0/[enemy_tmp.health]{/color}{/size}" xpos enemy_tmp.Xpos ypos enemy_tmp.Ypos + 130
            frame:
                text str(1) xalign 0.5 yalign 0.5
                xpos enemy_tmp.Xpos - 35
                ypos enemy_tmp.Ypos + 115

screen player_healing(current_name):
    for player_tmp in player_list:
        if player_tmp.name == current_name:
            if player_tmp.currenthp < player_tmp.health and player_tmp.health - player_tmp.currenthp > player.healing*player.amount:
                on "show" action SetField(player_tmp, "currenthp", player_tmp.currenthp+player.healing*player.amount)
            elif player_tmp.currenthp < player_tmp.health and player_tmp.health - player_tmp.currenthp <= player.healing*player.amount:
                on "show" action SetField(player_tmp, "currenthp", player_tmp.health)
            add player_tmp.image_healing xpos player_tmp.Xpos ypos player_tmp.Ypos
        else:
            add player_tmp.image xpos player_tmp.Xpos ypos player_tmp.Ypos
        bar:
            value player_tmp.currenthp 
            range player_tmp.health 
            xpos player_tmp.Xpos - 10
            xmaximum 150
            ypos player_tmp.Ypos + 125
            ysize 30
        text "{size=20}{color=#000}HP: [player_tmp.currenthp]/[player_tmp.health]{/color}{/size}" xpos player_tmp.Xpos ypos player_tmp.Ypos + 130
        frame:
            text str(player_tmp.amount) xalign 0.5 yalign 0.5
            xpos player_tmp.Xpos - 35
            ypos player_tmp.Ypos + 115
    for enemy_tmp in enemy_list:
        add enemy_tmp.image xpos enemy_tmp.Xpos ypos enemy_tmp.Ypos
        bar:
            value enemy_tmp.currenthp 
            range enemy_tmp.health 
            xpos enemy_tmp.Xpos - 10
            xmaximum 150
            ypos enemy_tmp.Ypos + 125
            ysize 30
        text "{size=20}{color=#000}HP: [enemy_tmp.currenthp]/[enemy_tmp.health]{/color}{/size}" xpos enemy_tmp.Xpos ypos enemy_tmp.Ypos + 130
        frame:
            text str(enemy_tmp.amount) xalign 0.5 yalign 0.5
            xpos enemy_tmp.Xpos - 35
            ypos enemy_tmp.Ypos + 115



screen player_turns(player, enemy_list):
    frame:
        textbutton "End of turn" xalign 0.5 yalign 0.9:
            action [If(strong_attack_2 == True, true = SetVariable("player.strong_attack_turn", player.strong_attack_turn+1), false = NullAction()), Jump("enemy_turn_continue")]
        xalign 0.5 yalign 0.9

    $ Xpos_turn_1 = player.Xpos - space_X
    $ flag = True
    for enemy_tmp in enemy_list:
        if (abs(Xpos_turn_1 - enemy_tmp.Xpos)+ abs(player.Ypos - enemy_tmp.Ypos)) <= error:
            $ flag = False
    for player_tmp in player_list:
        if (abs(Xpos_turn_1 - player_tmp.Xpos) + abs(player.Ypos - player_tmp.Ypos))<= error and player_tmp.Xpos-player.Xpos<0:
            $ flag = False
    if flag and Xpos_turn_1 - x > field_space_x:
        imagebutton xpos Xpos_turn_1 - x ypos player.Ypos - y:
            idle ("images/cell.png")
            hover ("images/cell_hover.png")
            action [SetVariable("player.Xpos", Xpos_turn_1), Hide("player_turns"), Jump("enemy_turn")]

    
    $ Xpos_turn_2 = player.Xpos + space_X
    $ flag = True
    for enemy_tmp in enemy_list:
        if (abs(Xpos_turn_2 - enemy_tmp.Xpos)+ abs(player.Ypos - enemy_tmp.Ypos)) <= error:
            $ flag = False
    for player_tmp in player_list:
        if (abs(Xpos_turn_2 - player_tmp.Xpos) + abs(player.Ypos - player_tmp.Ypos))<= error and player_tmp.Xpos-player.Xpos>0:
            $ flag = False
    if flag and Xpos_turn_2 - x < 1920 - field_space_x:
        imagebutton xpos Xpos_turn_2 - x ypos player.Ypos- y:
            idle ("images/cell.png")
            hover ("images/cell_hover.png")
            action [SetVariable("player.Xpos", Xpos_turn_2), Hide("player_turns"), Jump("enemy_turn")]


    $ Ypos_turn_2 = player.Ypos + space_Y
    $ flag = True
    for enemy_tmp in enemy_list:
        if (abs(Ypos_turn_2 - enemy_tmp.Ypos)+ abs(player.Xpos - enemy_tmp.Xpos)) <= error:
            $ flag = False
    for player_tmp in player_list:
        if (abs(Ypos_turn_2 - player_tmp.Ypos)+ abs(player.Xpos - player_tmp.Xpos))<= error and player_tmp.Ypos-player.Ypos>0:
            $ flag = False
    if flag and Ypos_turn_2- y < 1080 - field_space_menu:
        imagebutton xpos player.Xpos -x ypos Ypos_turn_2- y:
            idle ("images/cell.png")
            hover ("images/cell_hover.png")
            action [SetVariable("player.Ypos", Ypos_turn_2), Hide("player_turns"), Jump("enemy_turn")]


    $ Ypos_turn_1 = player.Ypos - space_Y
    $ flag = True
    for enemy_tmp in enemy_list:
        if (abs(Ypos_turn_1 - enemy_tmp.Ypos)+ abs(player.Xpos - enemy_tmp.Xpos)) <= error:
            $ flag = False
    for player_tmp in player_list:
        if (abs(Ypos_turn_1 - player_tmp.Ypos)+ abs(player.Xpos - player_tmp.Xpos))<= error and player_tmp.Ypos-player.Ypos<0:
            $ flag = False
    if flag and Ypos_turn_1- y > field_space_y:
        imagebutton xpos player.Xpos -x ypos Ypos_turn_1- y:
            idle ("images/cell.png")
            hover ("images/cell_hover.png")
            action [SetVariable("player.Ypos", Ypos_turn_1), Hide("player_turns"), Jump("enemy_turn")]

    
    $ Ypos_turn_1 = player.Ypos - space_Y
    $ Xpos_turn_2 = player.Xpos + space_X
    $ flag = True
    for enemy_tmp in enemy_list:
        if (abs(Ypos_turn_1 - enemy_tmp.Ypos)+ abs(Xpos_turn_2 - enemy_tmp.Xpos)) <= error:
            $ flag = False
    for player_tmp in player_list:
        if (abs(Ypos_turn_1 - player_tmp.Ypos)+ abs(Xpos_turn_2 - player_tmp.Xpos))<= error and player_tmp.Ypos-player.Ypos<0 and player_tmp.Xpos-player.Xpos>0:
            $ flag = False
    if flag and Ypos_turn_1- y > field_space_y and Xpos_turn_2 - x < 1920 - field_space_x:
        imagebutton xpos Xpos_turn_2 -x ypos Ypos_turn_1- y:
            idle ("images/cell.png")
            hover ("images/cell_hover.png")
            action [SetVariable("player.Ypos", Ypos_turn_1), SetVariable("player.Xpos", Xpos_turn_2), Hide("player_turns"), Jump("enemy_turn")]

    
    $ Ypos_turn_1 = player.Ypos + space_Y
    $ Xpos_turn_2 = player.Xpos + space_X
    $ flag = True
    for enemy_tmp in enemy_list:
        if (abs(Ypos_turn_1 - enemy_tmp.Ypos)+ abs(Xpos_turn_2 - enemy_tmp.Xpos)) <= error:
            $ flag = False
    for player_tmp in player_list:
        if (abs(Ypos_turn_1 - player_tmp.Ypos)+ abs(Xpos_turn_2 - player_tmp.Xpos))<= error and player_tmp.Ypos-player.Ypos>0 and player_tmp.Xpos-player.Xpos>0:
            $ flag = False
    if flag and Ypos_turn_2- y < 1080 - field_space_menu and Xpos_turn_2 - x < 1920 - field_space_x:
        imagebutton xpos Xpos_turn_2 - x ypos Ypos_turn_1- y:
            idle ("images/cell.png")
            hover ("images/cell_hover.png")
            action [SetVariable("player.Ypos", Ypos_turn_1), SetVariable("player.Xpos", Xpos_turn_2), Hide("player_turns"), Jump("enemy_turn")]

        
    $ Ypos_turn_1 = player.Ypos + space_Y
    $ Xpos_turn_2 = player.Xpos - space_X
    $ flag = True
    for enemy_tmp in enemy_list:
        if (abs(Ypos_turn_1 - enemy_tmp.Ypos)+ abs(Xpos_turn_2 - enemy_tmp.Xpos)) <= error:
            $ flag = False
    for player_tmp in player_list:
        if (abs(Ypos_turn_1 - player_tmp.Ypos)+ abs(Xpos_turn_2 - player_tmp.Xpos))<= error and player_tmp.Ypos-player.Ypos>0 and player_tmp.Xpos-player.Xpos<0:
            $ flag = False
    if flag and Ypos_turn_2- y < 1080 - field_space_menu and Xpos_turn_1 - x > field_space_x:
        imagebutton xpos Xpos_turn_2 - x ypos Ypos_turn_1- y:
            idle ("images/cell.png")
            hover ("images/cell_hover.png")
            action [SetVariable("player.Ypos", Ypos_turn_1), SetVariable("player.Xpos", Xpos_turn_2), Hide("player_turns"), Jump("enemy_turn")]


    $ Ypos_turn_1 = player.Ypos - space_Y
    $ Xpos_turn_2 = player.Xpos - space_X
    $ flag = True
    for enemy_tmp in enemy_list:
        if (abs(Ypos_turn_1 - enemy_tmp.Ypos)+ abs(Xpos_turn_2 - enemy_tmp.Xpos)) <= error:
            $ flag = False
    for player_tmp in player_list:
        if (abs(Ypos_turn_1 - player_tmp.Ypos)+ abs(Xpos_turn_2 - player_tmp.Xpos))<= error and player_tmp.Xpos-player.Xpos<0 and player_tmp.Ypos-player.Ypos<0:
            $ flag = False
    if flag and Xpos_turn_1 - x > field_space_x and Ypos_turn_1- y > field_space_y:
        imagebutton xpos Xpos_turn_2 - x ypos Ypos_turn_1- y:
            idle ("images/cell.png")
            hover ("images/cell_hover.png")
            action [SetVariable("player.Ypos", Ypos_turn_1), SetVariable("player.Xpos", Xpos_turn_2), Hide("player_turns"), Jump("enemy_turn")]


    if player.speed == 2:
        $ Xpos_turn_2 = player.Xpos + space_X + space_X
        $ flag = True
        for enemy_tmp in enemy_list:
            if (abs(Xpos_turn_2 - enemy_tmp.Xpos)+ abs(player.Ypos - enemy_tmp.Ypos)) <= error:
                $ flag = False
        for player_tmp in player_list:
            if (abs(Xpos_turn_2 - player_tmp.Xpos) + abs(player.Ypos - player_tmp.Ypos))<= error and player_tmp.Xpos-player.Xpos>0:
                $ flag = False
        if flag and Xpos_turn_2 - x < 1920 - field_space_x:
            imagebutton xpos Xpos_turn_2 - x ypos player.Ypos- y:
                idle ("images/cell.png")
                hover ("images/cell_hover.png")
                action [SetVariable("player.Xpos", Xpos_turn_2), Hide("player_turns"), Jump("enemy_turn")]

        
        $ Xpos_turn_1 = player.Xpos - space_X - space_X
        $ flag = True
        for enemy_tmp in enemy_list:
            if (abs(Xpos_turn_1 - enemy_tmp.Xpos)+ abs(player.Ypos - enemy_tmp.Ypos)) <= error:
                $ flag = False
        for player_tmp in player_list:
            if (abs(Xpos_turn_1 - player_tmp.Xpos) + abs(player.Ypos - player_tmp.Ypos))<= error and player_tmp.Xpos-player.Xpos<0:
                $ flag = False
        if flag and Xpos_turn_1 - x > field_space_x:
            imagebutton xpos Xpos_turn_1 - x ypos player.Ypos - y:
                idle ("images/cell.png")
                hover ("images/cell_hover.png")
                action [SetVariable("player.Xpos", Xpos_turn_1), Hide("player_turns"), Jump("enemy_turn")]


        $ Ypos_turn_2 = player.Ypos + space_Y + space_Y
        $ flag = True
        for enemy_tmp in enemy_list:
            if (abs(Ypos_turn_2 - enemy_tmp.Ypos)+ abs(player.Xpos - enemy_tmp.Xpos)) <= error:
                $ flag = False
        for player_tmp in player_list:
            if (abs(Ypos_turn_2 - player_tmp.Ypos)+ abs(player.Xpos - player_tmp.Xpos))<= error and player_tmp.Ypos-player.Ypos>0:
                $ flag = False
        if flag and Ypos_turn_2- y < 1080 - field_space_menu:
            imagebutton xpos player.Xpos -x ypos Ypos_turn_2- y:
                idle ("images/cell.png")
                hover ("images/cell_hover.png")
                action [SetVariable("player.Ypos", Ypos_turn_2), Hide("player_turns"), Jump("enemy_turn")]


        $ Ypos_turn_1 = player.Ypos - space_Y - space_Y
        $ flag = True
        for enemy_tmp in enemy_list:
            if (abs(Ypos_turn_1 - enemy_tmp.Ypos)+ abs(player.Xpos - enemy_tmp.Xpos)) <= error:
                $ flag = False
        for player_tmp in player_list:
            if (abs(Ypos_turn_1 - player_tmp.Ypos)+ abs(player.Xpos - player_tmp.Xpos))<= error and player_tmp.Ypos-player.Ypos<0:
                $ flag = False
        if flag and Ypos_turn_1- y > field_space_y:
            imagebutton xpos player.Xpos -x ypos Ypos_turn_1- y:
                idle ("images/cell.png")
                hover ("images/cell_hover.png")
                action [SetVariable("player.Ypos", Ypos_turn_1), Hide("player_turns"), Jump("enemy_turn")]


screen description(character):
    $ character_xpos = character.Xpos
    $ character_ypos = character.Ypos
    if character.Xpos > 1920 - description_space_x:
        $ character_xpos -= 300
    if character.Ypos < description_space_y:
        $ character_ypos += 350
    if character.name == "enemy_1" or character.name == "enemy_2" or character.name == "enemy_3":
        for place in character.e:
            add "images/cell_enemy.png" xpos place[0] - x ypos place[1] - y
    frame:
        background Solid("#b16e16a9")
        padding(25,25)
        xpos character_xpos + 100
        ypos character_ypos - 200
        vbox:
            text "{color=#000}{size=30}Attack: [character.attack]{/size}{/color}"
            text "{color=#000}{size=30}Defense: [character.defense]{/size}{/color}"
            text "{color=#000}{size=30}Health: [character.health]{/size}{/color}"
            text "{color=#000}{size=30}Speed: [character.speed]{/size}{/color}"
            #text "{color=#000}{size=30}Amount: [character.amount]{/size}{/color}"
            #text "{color=#000}{size=30}Count_ice_arrow: [character.count_ice_arrow]{/size}{/color}"


screen attack(enemy_list):
    if healing == False:
        for player_tmp in player_list:
            imagebutton xpos player_tmp.Xpos ypos player_tmp.Ypos:
                idle "images/free.png"
                action NullAction()
                alternate Show("description", character = player_tmp)
                unhovered Hide("description")

        for enemy_tmp in enemy_list:
            if player.unit_type == "warrior":
                imagebutton xpos enemy_tmp.Xpos ypos enemy_tmp.Ypos:
                    idle (enemy_tmp.image)
                    action NullAction()
                    alternate Show("description", character = enemy_tmp)
                    unhovered Hide("description")
                if abs(player.Xpos- enemy_tmp.Xpos) <= space_X + error and abs(player.Ypos- enemy_tmp.Ypos) <= space_Y + error:
                    imagebutton xpos enemy_tmp.Xpos ypos enemy_tmp.Ypos:
                        idle (enemy_tmp.image)
                        hover (enemy_tmp.image_attacked)
                        alternate Show("description", character = enemy_tmp)
                        unhovered Hide("description")
                        action [Play("sound", "audio/punch.mp3"), Hide("enemy"),Hide("attack"), Hide("end_of_turn"), Hide("player_ability"), Hide("player_turns"), 
                        Show("enemy_attacked", current_name = enemy_tmp.name), Hide("description"), Jump("enemy_turn_continue_attacked")]

            elif player.unit_type == "archer":
                imagebutton xpos enemy_tmp.Xpos ypos enemy_tmp.Ypos:
                    idle (enemy_tmp.image)
                    hover (enemy_tmp.image_attacked)
                    alternate Show("description", character = enemy_tmp)
                    unhovered Hide("description")
                    action [Play("sound", "audio/punch.mp3"), Hide("enemy"),Hide("attack"), Hide("end_of_turn"), Hide("player_ability"), Hide("player_turns"), 
                    Show("enemy_attacked", current_name = enemy_tmp.name), Hide("description"), Jump("enemy_turn_continue_attacked")]

            elif player.unit_type == "wizard":
                imagebutton xpos enemy_tmp.Xpos ypos enemy_tmp.Ypos:
                    idle (enemy_tmp.image)
                    hover (enemy_tmp.image_attacked)
                    alternate Show("description", character = enemy_tmp)
                    unhovered Hide("description")
                    action [Play("sound", "audio/punch.mp3"), Hide("enemy"),Hide("attack"), Hide("end_of_turn"), Hide("player_ability"), Hide("player_turns"), 
                    Show("enemy_attacked", current_name = enemy_tmp.name), Hide("description"), Jump("enemy_turn_continue_attacked")]
    else:
        for player_tmp in player_list:
            imagebutton xpos player_tmp.Xpos ypos player_tmp.Ypos:
                idle "images/free.png"
                hover (player_tmp.image_healing)
                if player_tmp == player:
                    hovered [Hide("player"), Show("player_healing_current", player_list = player_list)]
                action [Hide("player"),Hide("attack"), Hide("end_of_turn"), Hide("player_ability"), Hide("player_turns"), 
                Show("player_healing", current_name = player_tmp.name), Hide("description"), Jump("enemy_turn_continue_attacked")]
                alternate Show("description", character = player_tmp)
                unhovered [Hide("attack"), Hide("player_healing_current"), Show("player", player_list = player_list), Show("attack", enemy_list = enemy_list), Hide("description")]
        for enemy_tmp in enemy_list:
            imagebutton xpos enemy_tmp.Xpos ypos enemy_tmp.Ypos:
                idle "images/free.png"
                action NullAction()
                alternate Show("description", character = enemy_tmp)
                unhovered Hide("description")




screen end_of_turn:
    frame:
        textbutton "End of turn" xalign 0.5 yalign 0.9:
            action [If(strong_attack_2 == True, true = SetVariable("player.strong_attack_turn", player.strong_attack_turn+1), false = NullAction()), Jump("enemy_turn_continue")]
        xalign 0.5 yalign 0.9


screen player_ability(player):
    hbox:
        frame:
            add player.image
        if player.unit_type == "warrior" and player.strong_attack_turn == 0:
            frame:
                padding(10,10)
                xmargin 50
                textbutton "Strong\nattack" xalign 0.3 yalign 0.9:
                    action SetVariable("strong_attack", True)
                xalign 0.05 yalign 0.98
            
        if player.unit_type == "wizard":
            frame:
                padding(10,10)
                xmargin 50
                textbutton "Healing" xalign 0.3 yalign 0.9:
                    action SetVariable("healing", True)
                xalign 0.05 yalign 0.98
        if player.unit_type == "archer" and player.ice_arrow_used == False:
            frame:
                padding(10,10)
                xmargin 50
                textbutton "Ice\narrow" xalign 0.3 yalign 0.9:
                    action SetVariable("ice_arrow", True)
                xalign 0.05 yalign 0.98

        if strong_attack == True:
            frame:
                padding(10,10)
                xmargin 3
                textbutton "×":
                    action SetVariable("strong_attack", False)
                xalign 0.05 yalign 0.98
        if healing == True:
            frame:
                padding(10,10)
                xmargin 3
                textbutton "×":
                    action SetVariable("healing", False)
                xalign 0.05 yalign 0.98
        if ice_arrow == True:
            frame:
                padding(10,10)
                xmargin 3
                textbutton "×":
                    action SetVariable("ice_arrow", False)
                xalign 0.05 yalign 0.98
        xalign 0.05 yalign 0.98
    

#screen strong_attack_turn_visual:
    #frame:
        #textbutton str(player.strong_attack_turn) xalign 0.6 yalign 0.9:
            #action NullAction()
        #xalign 0.6 yalign 0.9

label player_turn:
    python:
        for enemy in enemy_list:
            if enemy.unit_type == "warrior":
                if enemy.count_ice_arrow < 3:
                    enemy.e = [[enemy.Xpos, enemy.Ypos], [enemy.Xpos + space_X, enemy.Ypos], [enemy.Xpos - space_X, enemy.Ypos], [enemy.Xpos, enemy.Ypos + space_Y], [enemy.Xpos, enemy.Ypos - space_Y], [enemy.Xpos + space_X, enemy.Ypos + space_Y],
                    [enemy.Xpos + space_X, enemy.Ypos - space_Y], [enemy.Xpos - space_X, enemy.Ypos - space_Y], [enemy.Xpos - space_X, enemy.Ypos + space_Y]]
                if enemy.count_ice_arrow == 3:
                    enemy.speed = 2
                    enemy.e = [[enemy.Xpos, enemy.Ypos], [enemy.Xpos + space_X, enemy.Ypos], [enemy.Xpos - space_X, enemy.Ypos], [enemy.Xpos, enemy.Ypos + space_Y], [enemy.Xpos, enemy.Ypos - space_Y], [enemy.Xpos + space_X, enemy.Ypos + space_Y],
                    [enemy.Xpos + space_X, enemy.Ypos - space_Y], [enemy.Xpos - space_X, enemy.Ypos - space_Y], [enemy.Xpos - space_X, enemy.Ypos + space_Y], [enemy.Xpos + space_X + space_X, enemy.Ypos], [enemy.Xpos - space_X - space_X, enemy.Ypos], [enemy.Xpos, enemy.Ypos + space_Y + space_Y], [enemy.Xpos, enemy.Ypos - space_Y - space_Y]] 
            if enemy.unit_type == "wizard":
                if enemy.count_ice_arrow < 3:
                    enemy.e = [[enemy.Xpos, enemy.Ypos], [enemy.Xpos + space_X, enemy.Ypos], [enemy.Xpos - space_X, enemy.Ypos], [enemy.Xpos, enemy.Ypos + space_Y], [enemy.Xpos, enemy.Ypos - space_Y], [enemy.Xpos + space_X, enemy.Ypos + space_Y],
                    [enemy.Xpos + space_X, enemy.Ypos - space_Y], [enemy.Xpos - space_X, enemy.Ypos - space_Y], [enemy.Xpos - space_X, enemy.Ypos + space_Y]]
                if enemy.count_ice_arrow == 3:
                    enemy.speed = 2
                    enemy.e = [[enemy.Xpos, enemy.Ypos], [enemy.Xpos + space_X, enemy.Ypos], [enemy.Xpos - space_X, enemy.Ypos], [enemy.Xpos, enemy.Ypos + space_Y], [enemy.Xpos, enemy.Ypos - space_Y], [enemy.Xpos + space_X, enemy.Ypos + space_Y],
                    [enemy.Xpos + space_X, enemy.Ypos - space_Y], [enemy.Xpos - space_X, enemy.Ypos - space_Y], [enemy.Xpos - space_X, enemy.Ypos + space_Y], [enemy.Xpos + space_X + space_X, enemy.Ypos], [enemy.Xpos - space_X - space_X, enemy.Ypos], [enemy.Xpos, enemy.Ypos + space_Y + space_Y], [enemy.Xpos, enemy.Ypos - space_Y - space_Y]]   
            if enemy.unit_type == "archer":
                if enemy.count_ice_arrow < 3:
                    enemy.e = [[enemy.Xpos, enemy.Ypos]]
                if enemy.count_ice_arrow == 3:
                    enemy.speed = 1
                    enemy.e = [[enemy.Xpos, enemy.Ypos], [enemy.Xpos + space_X, enemy.Ypos], [enemy.Xpos - space_X, enemy.Ypos], [enemy.Xpos, enemy.Ypos + space_Y], [enemy.Xpos, enemy.Ypos - space_Y], [enemy.Xpos + space_X, enemy.Ypos + space_Y],
                    [enemy.Xpos + space_X, enemy.Ypos - space_Y], [enemy.Xpos - space_X, enemy.Ypos - space_Y], [enemy.Xpos - space_X, enemy.Ypos + space_Y]]
    python:
        for player_tmp in player_list:
            for enemy in enemy_list:
                for place in enemy.e:
                    if abs(player_tmp.Xpos - place[0]) <= space_X - error and abs(player_tmp.Ypos- place[1]) <= space_Y - error:
                        enemy.e.remove(place)
        for enemy_tmp in enemy_list:
            for enemy in enemy_list:
                for place in enemy.e:
                    if abs(enemy_tmp.Xpos - place[0]) <= space_X - error and abs(enemy_tmp.Ypos- place[1]) <= space_Y - error:
                        enemy.e.remove(place)

        ######## 2 раза повторяется! (возможна ошибка)
        for enemy_tmp in enemy_list:
            for place in enemy_tmp.e:
                if place[1] >= 1080 - field_space_menu:
                    enemy_tmp.e.remove(place)
                elif place[0] >= 1920 - field_space_x:
                    enemy_tmp.e.remove(place)
                elif place[1] < field_space_y:
                    enemy_tmp.e.remove(place)
                elif place[0] < field_space_x:
                    enemy_tmp.e.remove(place)
        for enemy_tmp in enemy_list:
            for place in enemy_tmp.e:
                if place[1] >= 1080 - field_space_menu:
                    enemy_tmp.e.remove(place)
                elif place[0] >= 1920 - field_space_x:
                    enemy_tmp.e.remove(place)
                elif place[1] < field_space_y:
                    enemy_tmp.e.remove(place)
                elif place[0] < field_space_x:
                    enemy_tmp.e.remove(place)
        ##########

    $ strong_attack = False
    $ strong_attack_2 = False
    $ healing = False
    $ ice_arrow = False
    if player.strong_attack_turn == 2:
        $ player.strong_attack_turn = 0
    if player.strong_attack_turn == 1:
        $ strong_attack_2 = True
    #show screen strong_attack_turn_visual
    hide screen player_inactive
    show screen enemy(enemy_list)
    show screen player(player_list)
    show screen player_turns(player, enemy_list)
    show screen player_ability(player)
    call screen attack(enemy_list)



label enemy_turn:  
    python:
        for enemy in enemy_list:
            if enemy.unit_type == "warrior":
                if enemy.count_ice_arrow < 3:
                    enemy.e = [[enemy.Xpos, enemy.Ypos], [enemy.Xpos + space_X, enemy.Ypos], [enemy.Xpos - space_X, enemy.Ypos], [enemy.Xpos, enemy.Ypos + space_Y], [enemy.Xpos, enemy.Ypos - space_Y], [enemy.Xpos + space_X, enemy.Ypos + space_Y],
                    [enemy.Xpos + space_X, enemy.Ypos - space_Y], [enemy.Xpos - space_X, enemy.Ypos - space_Y], [enemy.Xpos - space_X, enemy.Ypos + space_Y]]
                if enemy.count_ice_arrow == 3:
                    enemy.speed = 2
                    enemy.e = [[enemy.Xpos, enemy.Ypos], [enemy.Xpos + space_X, enemy.Ypos], [enemy.Xpos - space_X, enemy.Ypos], [enemy.Xpos, enemy.Ypos + space_Y], [enemy.Xpos, enemy.Ypos - space_Y], [enemy.Xpos + space_X, enemy.Ypos + space_Y],
                    [enemy.Xpos + space_X, enemy.Ypos - space_Y], [enemy.Xpos - space_X, enemy.Ypos - space_Y], [enemy.Xpos - space_X, enemy.Ypos + space_Y], [enemy.Xpos + space_X + space_X, enemy.Ypos], [enemy.Xpos - space_X - space_X, enemy.Ypos], [enemy.Xpos, enemy.Ypos + space_Y + space_Y], [enemy.Xpos, enemy.Ypos - space_Y - space_Y]] 
            if enemy.unit_type == "wizard":
                if enemy.count_ice_arrow < 3:
                    enemy.e = [[enemy.Xpos, enemy.Ypos], [enemy.Xpos + space_X, enemy.Ypos], [enemy.Xpos - space_X, enemy.Ypos], [enemy.Xpos, enemy.Ypos + space_Y], [enemy.Xpos, enemy.Ypos - space_Y], [enemy.Xpos + space_X, enemy.Ypos + space_Y],
                    [enemy.Xpos + space_X, enemy.Ypos - space_Y], [enemy.Xpos - space_X, enemy.Ypos - space_Y], [enemy.Xpos - space_X, enemy.Ypos + space_Y]]
                if enemy.count_ice_arrow == 3:
                    enemy.speed = 2
                    enemy.e = [[enemy.Xpos, enemy.Ypos], [enemy.Xpos + space_X, enemy.Ypos], [enemy.Xpos - space_X, enemy.Ypos], [enemy.Xpos, enemy.Ypos + space_Y], [enemy.Xpos, enemy.Ypos - space_Y], [enemy.Xpos + space_X, enemy.Ypos + space_Y],
                    [enemy.Xpos + space_X, enemy.Ypos - space_Y], [enemy.Xpos - space_X, enemy.Ypos - space_Y], [enemy.Xpos - space_X, enemy.Ypos + space_Y], [enemy.Xpos + space_X + space_X, enemy.Ypos], [enemy.Xpos - space_X - space_X, enemy.Ypos], [enemy.Xpos, enemy.Ypos + space_Y + space_Y], [enemy.Xpos, enemy.Ypos - space_Y - space_Y]]   
            if enemy.unit_type == "archer":
                if enemy.count_ice_arrow < 3:
                    enemy.e = [[enemy.Xpos, enemy.Ypos]]
                if enemy.count_ice_arrow == 3:
                    enemy.speed = 1
                    enemy.e = [[enemy.Xpos, enemy.Ypos], [enemy.Xpos + space_X, enemy.Ypos], [enemy.Xpos - space_X, enemy.Ypos], [enemy.Xpos, enemy.Ypos + space_Y], [enemy.Xpos, enemy.Ypos - space_Y], [enemy.Xpos + space_X, enemy.Ypos + space_Y],
                    [enemy.Xpos + space_X, enemy.Ypos - space_Y], [enemy.Xpos - space_X, enemy.Ypos - space_Y], [enemy.Xpos - space_X, enemy.Ypos + space_Y]]     
    python:
        for player_tmp in player_list:
            for enemy in enemy_list:
                for place in enemy.e:
                    if abs(player_tmp.Xpos - place[0]) <= space_X - error and abs(player_tmp.Ypos- place[1]) <= space_Y - error:
                        enemy.e.remove(place)
        for enemy_tmp in enemy_list:
            for enemy in enemy_list:
                for place in enemy.e:
                    if abs(enemy_tmp.Xpos - place[0]) <= space_X - error and abs(enemy_tmp.Ypos- place[1]) <= space_Y - error:
                        enemy.e.remove(place)
        
        ######## 2 раза повторяется! (возможна ошибка)
        for enemy_tmp in enemy_list:
            for place in enemy_tmp.e:
                if place[1] >= 1080 - field_space_menu:
                    enemy_tmp.e.remove(place)
                elif place[0] >= 1920 - field_space_x:
                    enemy_tmp.e.remove(place)
                elif place[1] < field_space_y:
                    enemy_tmp.e.remove(place)
                elif place[0] < field_space_x:
                    enemy_tmp.e.remove(place)
        for enemy_tmp in enemy_list:
            for place in enemy_tmp.e:
                if place[1] >= 1080 - field_space_menu:
                    enemy_tmp.e.remove(place)
                elif place[0] >= 1920 - field_space_x:
                    enemy_tmp.e.remove(place)
                elif place[1] < field_space_y:
                    enemy_tmp.e.remove(place)
                elif place[0] < field_space_x:
                    enemy_tmp.e.remove(place)
        ##########

    show screen end_of_turn
    #show screen player_ability(player)
    call screen attack(enemy_list)

        

label enemy_turn_continue_attacked:
    pause 0.2
    hide screen enemy_attacked
    hide screen player_healing
    python:
        for enemy_tmp in enemy_list:
            if enemy_tmp.amount == 0:
                enemy_list.remove(enemy_tmp)
    if len(enemy_list) == 0:
        jump battle_end_win
    else:
        show screen enemy(enemy_list)
        show screen player(player_list)
        jump enemy_turn_continue



label enemy_turn_continue:
    hide screen attack
    hide screen end_of_turn
    hide screen player_ability
    hide screen player_turns
    hide screen player
    hide screen player_healing_current
    show screen player_inactive(player_list)
    $ distance = 10000
    $ dist_exclude = [0]
    $ enemy = enemy_list[0]
    $ player_hp_min = player
    hide screen enemy
    show screen enemy_active_screen(enemy, enemy_list)
    pause 2.0
    hide screen enemy_active_screen
    hide screen player_inactive
    show screen enemy(enemy_list)
    python:
        for player_tmp in player_list:
            if player_tmp.currenthp < player_hp_min.currenthp:
                player_hp_min = player_tmp

    if abs(player_hp_min.Xpos - enemy.Xpos) <= space_X + error and abs(player_hp_min.Ypos- enemy.Ypos) <= space_Y + error and enemy.unit_type == "warrior":
        play sound "punch.mp3"
        if enemy.attack*enemy.amount > player_hp_min.defense:
            $ player_hp_min.currenthp = player_hp_min.currenthp - enemy.attack*enemy.amount + player_hp_min.defense
        hide screen player
        show screen player_attacked(player_hp_min)
        pause 0.2
        if player_hp_min.currenthp <= 0 and player_hp_min.amount > 0:
            $ player_hp_min.currenthp = player_hp_min.health
            $ player_hp_min.amount -= 1
        if player_hp_min.amount == 0:
            $ player_list.remove(player_hp_min)
        if enemy.count_ice_arrow < 3:
            $ enemy.count_ice_arrow = enemy.count_ice_arrow + 1
        hide screen player_attacked

    elif enemy.unit_type == "archer":
        play sound "punch.mp3"
        if enemy.attack*enemy.amount > player_hp_min.defense:
            $ player_hp_min.currenthp = player_hp_min.currenthp - enemy.attack*enemy.amount + player_hp_min.defense
        hide screen player
        show screen player_attacked(player_hp_min)
        pause 0.2
        if player_hp_min.currenthp <= 0 and player_hp_min.amount > 0:
            $ player_hp_min.currenthp = player_hp_min.health
            $ player_hp_min.amount -= 1
        if player_hp_min.amount == 0:
            $ player_list.remove(player_hp_min)
        if enemy.count_ice_arrow < 3:
            $ enemy.count_ice_arrow = enemy.count_ice_arrow + 1
        hide screen player_attacked

    elif enemy.unit_type == "wizard":
        play sound "punch.mp3"
        if enemy.attack*enemy.amount > player_hp_min.defense:
            $ player_hp_min.currenthp = player_hp_min.currenthp - enemy.attack*enemy.amount + player_hp_min.defense
        hide screen player
        show screen player_attacked(player_hp_min)
        pause 0.2
        if player_hp_min.currenthp <= 0 and player_hp_min.amount > 0:
            $ player_hp_min.currenthp = player_hp_min.health
            $ player_hp_min.amount -= 1
        if player_hp_min.amount == 0:
            $ player_list.remove(player_hp_min)
        if enemy.count_ice_arrow < 3:
            $ enemy.count_ice_arrow = enemy.count_ice_arrow + 1
        hide screen player_attacked

    else:
        $ newX = 0
        $ newY = 0
        $ flag_2 = True
        while (flag_2):
            $ count = 0
            $ distance = 10000
            python:
                for player_tmp in player_list:
                    for place in enemy.e:
                        distance_1 = math.sqrt(abs(place[0]-player_tmp.Xpos)*abs(place[0]-player_tmp.Xpos) + abs(place[1]-player_tmp.Ypos)*abs(place[1]-player_tmp.Ypos))
                        for dist in dist_exclude:
                            if distance_1 == dist:
                                count+=1
                        if count == 0:
                            if distance_1 < distance and distance_1 > error:
                                distance = distance_1
                                newX = place[0]
                                newY = place[1]
    
            python:
                for enemy_tmp in enemy_list:
                    if enemy_tmp.Xpos == newX and enemy_tmp.Ypos == newY:
                        flag_2 = False
                        dist_exclude.append(distance)
            if flag_2:
                if distance > error:
                    $ enemy.Xpos = newX
                if distance > error:
                    $ enemy.Ypos = newY
                
                if enemy.count_ice_arrow < 3:
                    $ enemy.count_ice_arrow = enemy.count_ice_arrow + 1
                
                $ flag_2 = False
            else:
                $ flag_2 = True

        python:
            for player_tmp in player_list:
                if player_tmp.currenthp < player_hp_min.currenthp:
                    player_hp_min = player_tmp


        if len(player_list) == 0:
            jump battle_end_loss

        if abs(player_hp_min.Xpos- enemy.Xpos) <= space_X + error and abs(player_hp_min.Ypos- enemy.Ypos) <= space_Y + error:
            play sound "punch.mp3" 
            if enemy.attack*enemy.amount > player_hp_min.defense:
                $ player_hp_min.currenthp = player_hp_min.currenthp - enemy.attack*enemy.amount + player_hp_min.defense
            hide screen player
            show screen player_attacked(player_hp_min)
            pause 0.2
            if player_hp_min.currenthp <= 0 and player_hp_min.amount > 0:
                $ player_hp_min.currenthp = player_hp_min.health
                $ player_hp_min.amount -= 1
            if player_hp_min.amount == 0:
                $ player_list.remove(player_hp_min)
            hide screen player_attacked
        else:
            python:
                for player_tmp in player_list:
                    if abs(player_tmp.Xpos- enemy.Xpos) <= space_X + error and abs(player_tmp.Ypos- enemy.Ypos) <= space_Y + error:
                        player_hp_min = player_tmp
                        renpy.jump("attack_nearest_player")
        if len(player_list) == 0:
            jump battle_end_loss

    if len(player_list) == 0:
            jump battle_end_loss

    label attack_nearest_player_continue:
        python:
            player_list = player_list[-1:] + player_list[:-1]

        python:
            enemy_list = enemy_list[-1:] + enemy_list[:-1]

        $ player = player_list[0]
        $ enemy = enemy_list[0]

    jump player_turn

label attack_nearest_player:
    play sound "punch.mp3" 
    $ player_hp_min.currenthp -= enemy.attack
    hide screen player
    show screen player_attacked(player_hp_min)
    pause 0.2
    hide screen player_attacked
    jump attack_nearest_player_continue


screen battle_end_win_screen:
    frame:
        padding (50, 50)
        text "{size=50}WIN{/size}" xalign 0.5 yalign 0.5
        xalign 0.5 yalign 0.5

screen battle_end_loss_screen:
    frame:
        padding (50, 50)
        text "{size=50}LOSS{/size}" xalign 0.5 yalign 0.5
        xalign 0.5 yalign 0.5


label battle_end_win:
    call screen battle_end_win_screen


label battle_end_loss:
    call screen battle_end_loss_screen




label start:
    $ enemy_x_start_1 = 1680
    $ enemy_x_start_2 = 1680
    $ enemy_y_start_1 = 210
    $ enemy_y_start_2 = 560
    $ enemy_x_start_3 = 1680
    $ enemy_y_start_3 = 735

    $ player_1 = Player(Character("player_1"), "player_1", "wizard", "images/player_1.png", "images/player_1_attacked.png", "images/player_1_healing.png", 10, 100, 100, 115, 560, 2, 5, 2, 0, False)
    $ player_2 = Player(Character("player_2"), "player_2", "archer", "images/player_2.png", "images/player_2_attacked.png", "images/player_2_healing.png", 10, 100, 100, 115, 735, 2, 5, 1, 0, False)
    $ player_3 = Player(Character("player_3"), "player_3", "warrior", "images/player_3.png", "images/player_3_attacked.png", "images/player_3_healing.png", 10, 100, 100, 115, 210, 2, 5, 2, 0, False)
    $ player_list = [player_1, player_2, player_3]

    $ enemy_1 = Enemy(Character("enemy_1"), "enemy_1", "wizard", "images/enemy_1.png", "images/enemy_1_attacked.png", 10, 100, 100, enemy_x_start_1, enemy_y_start_1, [[enemy_x_start_1, enemy_y_start_1], [enemy_x_start_1 + space_X, enemy_y_start_1], [enemy_x_start_1 - space_X, enemy_y_start_1], [enemy_x_start_1, enemy_y_start_1 + space_Y], [enemy_x_start_1, enemy_y_start_1 - space_Y], [enemy_x_start_1 + space_X, enemy_y_start_1 + space_Y],
    [enemy_x_start_1 + space_X, enemy_y_start_1 - space_Y], [enemy_x_start_1 - space_X, enemy_y_start_1 - space_Y], [enemy_x_start_1 - space_X, enemy_y_start_1 + space_Y], [enemy_x_start_1 + space_X + space_X, enemy_y_start_1], [enemy_x_start_1 - space_X - space_X, enemy_y_start_1], [enemy_x_start_1, enemy_y_start_1 + space_Y + space_Y], [enemy_x_start_1, enemy_y_start_1 - space_Y - space_Y]], 1, 5, 2)

    $ enemy_2 = Enemy(Character("enemy_2"), "enemy_2", "warrior", "images/enemy_2.png", "images/enemy_2_attacked.png", 10, 100, 100, enemy_x_start_2, enemy_y_start_2, [[enemy_x_start_2, enemy_y_start_2], [enemy_x_start_2 + space_X, enemy_y_start_2], [enemy_x_start_2 - space_X, enemy_y_start_2], [enemy_x_start_2, enemy_y_start_2 + space_Y], [enemy_x_start_2, enemy_y_start_2 - space_Y], [enemy_x_start_2 + space_X, enemy_y_start_2 + space_Y],
    [enemy_x_start_2 + space_X, enemy_y_start_2 - space_Y], [enemy_x_start_2 - space_X, enemy_y_start_2 - space_Y], [enemy_x_start_2 - space_X, enemy_y_start_2 + space_Y], [enemy_x_start_2 + space_X + space_X, enemy_y_start_2], [enemy_x_start_2 - space_X - space_X, enemy_y_start_2], [enemy_x_start_2, enemy_y_start_2 + space_Y + space_Y], [enemy_x_start_2, enemy_y_start_2 - space_Y - space_Y]], 2, 5, 2)

    $ enemy_3 = Enemy(Character("enemy_3"), "enemy_3", "archer", "images/enemy_3.png", "images/enemy_3_attacked.png", 10, 100, 100, enemy_x_start_3, enemy_y_start_3, [[enemy_x_start_3, enemy_y_start_3], [enemy_x_start_3 + space_X, enemy_y_start_3], [enemy_x_start_3 - space_X, enemy_y_start_3], [enemy_x_start_3, enemy_y_start_3 + space_Y], [enemy_x_start_3, enemy_y_start_3 - space_Y], [enemy_x_start_3 + space_X, enemy_y_start_3 + space_Y],
    [enemy_x_start_3 + space_X, enemy_y_start_3 - space_Y], [enemy_x_start_3 - space_X, enemy_y_start_3 - space_Y], [enemy_x_start_3 - space_X, enemy_y_start_3 + space_Y]], 3, 5, 1)

    $ enemy_list = [enemy_1, enemy_2, enemy_3]


    show screen field

    $ player = player_list[0]

    jump player_turn

    return
