label dialog_stud_0_1:
    $ teacher = teachers[rand(0,len(teachers)-1)] #Случайный учитель
    'Вы поговорили о том, что [teacher.club] является важной наукой, а её преподаватель, [teacher.name], является прекрасным человеком.'
    'И ещё немного о том, о сём.'
    call screen show_stat

label dialog_stud_0_2:
    $ teacher = teachers[rand(0,len(teachers)-1)]
    $ science = teacher.club.title() #Наука с заглавной буквы
    player.say '[science] очень интересна в изучении, как ты думаешь?'
    if teacher == danokova:
        user.say 'Я думаю, что Вам надо сначала заняться русским языком.'
    else :
        user.say 'Ага! Мне нравится как [teacher.name] преподаёт предмет!'
    'Вы ещё немного поболтали об учителе и предмете.'
    call screen show_stat

label dialog_stud_0_3:
    $ teacher = teachers[rand(0,len(teachers)-1)]
    $ science = teacher.club.title()
    player.say '[science] - это классно! - весело говорите Вы.'
    user.say 'Угу, просто мне не нравится, как [teacher.name] выглядит. - угрюмо отвечают Вам.'
    'Вы немного поболтали о внешности учителя, и том, что это не главное.'
    call screen show_stat

label dialog_stud_0_4:
    $ teacher = teachers[rand(0,len(teachers)-1)]
    $ science = teacher.club.title()
    player.say '[science] - мой любимый предмет! - заводите Вы разговор.'
    if user.getSex() == 'male':
        user.say 'А мой - [science]! - как-то невпопад отвечает ученик. Или [user.fname] просто подкалывает вас?'
    else:
        user.say 'А мой - [science]! - как-то невпопад отвечает ученица. Или [user.fname] просто подкалывает вас?'
    player.say 'Вы удивленно переспросили собеседника и выяснили, что Вас просто не расслышали.'
    call screen show_stat

label dialog_stud_0_5:
    $ teacher = teachers[rand(0,len(teachers)-1)]
    $ science = teacher.club.title()
    player.say 'Как тебе [teacher.name]? - интересуетесь Вы.'
    user.say 'Как и все, просто [science] не самый мой любимый предмет, - оправдывается [user.fname].'
    'Вы разговорились о приоритетах в учёбе и важности образования.'
    call screen show_stat

label dialog_stud_0_6:
    $ teacher = teachers[rand(0,len(teachers)-1)]
    $ science = teacher.club.title()
    player.say 'У тебя всё в порядке с учебой? - интересуетесь Вы.'
    if user.getSex() == 'male':
        user.say 'Я просто забыл сделать домашнее задание, теперь [teacher.name] будет ругаться. - сокрушается старшеклассник.'
    else:
        user.say 'Я просто забыла сделать домашнее задание, теперь [teacher.name] будет ругаться. - сокрушается старшеклассница.'
    'Вы ещё немного поболтали о тайм-менеджменте и важности выполнения домашнего задания.'
    call screen show_stat

label dialog_stud_0_7:
    $ char = getChar('female','beautymax')
    'Вы завели ничего не значащий разговор, из которого узнали, что [char.name] - самая красивая ученица в школе!'
    'Вы ещё немного поболтали о том, о сём.'
    call screen show_stat

label dialog_stud_0_8:
    'Из разговора с учеником Вы узнали, что на торговой улице недавно появился салон красоты!'
    'Вы ещё немного поболтали о том, о сём.'
    call screen show_stat

label dialog_stud_0_9:
    'Вам рассказали, что однажды видели девушку в бикини, которая шла по городу! От зевак отбоя не было! Хотя, судя по тому, что такие случаи нечасты, её всё таки посадили или выдворили из города.'
    'Вы ещё немного поболтали о том, о сём.'
    call screen show_stat

label dialog_stud_0_10:
    if user.getSex() == 'male':
        user.say '[user.name] подсказал вам, что неплохие вещи продаются на углу Торговой улицы, в небольшом минимаркете.'
    else:
        user.say '[user.name] подсказала вам, что неплохие вещи продаются на углу Торговой улицы, в небольшом минимаркете.'
    call screen show_stat

label dialog_stud_0_11:
    if user.getSex() == 'male':
        user.say '[user.name] рассказал, что однажды слышал стоны привидения в раздевалке на пляже. Он, конечно не трус, но от опрометчивых действий воздержался и быстренько сбежал оттуда.'
    else:
        user.say '[user.name] рассказала, что однажды слышала стоны привидения в раздевалке на пляже. Она страшно испугалась и убежала.'
    player.say '"Как мило! Раздевалочное привидение..."'
    call screen show_stat

label dialog_stud_0_12:
    if user.getSex() == 'male':
        user.say '[user.name] поведал, что на пляже происходит больше всего событий в городе!'
    else:
        user.say '[user.name] поведала, что на пляже происходит больше всего событий в городе!'
    player.say '"Хех, надо почаще посещать пляж!"'
    call screen show_stat

label dialog_stud_0_13:
    if user.getSex() == 'male':
        user.say '[user.name] рассказал, что одна его подруга не ела много дней, соблюдая диету, а потом заболела и умерла.'
    else:
        user.say '[user.name] рассказала, что одна её подруга не ела много дней, cоблюдая диету, а потом заболела и умерла.'
    'Вы поскорбели вместе о безвременной кончине юной анорекисички.'
    call screen show_stat

label dialog_stud_0_14:
    if user.getSex() == 'male':
        user.say '[user.name] рассказал, что в 4 классе за учительской тумбой живёт мышь, которая иногда скребётся после уроков!'
    else:
        user.say '[user.name] рассказала, что в 4 классе за учительской тумбой живёт мышь, которая иногда скребётся после уроков!'
    'Вы приняли во внимание этот странный факт.'
    call screen show_stat

label dialog_stud_0_15:
    if is_library == 0:
        user.say '[user.name] невинно интересуется, почему во всех школах есть библиотеки, а в нашей нет?'
        player.say 'Вы отбрыкиваетесь недостатком финансирования и прочей чепухой.'
    else:
        user.say '[user.name] благодарит Вас за финансирование постройки школьной библиотеки!'
        player.say 'Вы принимаете благодарность с довольной улыбкой, напутствуя ученика, чтобы он чаще её посещал!'
    call screen show_stat

label dialog_stud_0_16:
    if 'wall' in school.furniture:
        user.say '[user.name] спрашивает, не слишком ли острая ограда у школы? Кто-нибудь может и пораниться!'
        player.say 'Вы обещаете подумать над тем, как её улучшить. Хех, улучшить ограду? Стену чтоли вместо неё отгрохать? Просто заложить всё кирпичём и готово...'
    else:
        user.say '[user.name] спрашивает, зачем мы построили стену вокруг школы?'
        player.say 'Вы объясняете, что это необходимая политика в виду усилившейся террористической угрозы. Старательно пытаясь не засмеяться, пока Вы несёте эту ахинею. Ну, по крайней мере, [user.fname] уверенно кивает, видимо полностью доверяя Вам!'
    call screen show_stat









label dialog_teacher_0_1:
    $ st = getChar('','edumin')
    if st.body.sex() == 'male':
        user.say 'Вы поговорили об успеваемости в школе, о двоечниках. Особой темой для разговора был [st.name]. Его оценки оставляют желать лучшего по сравнению со средним уровнем образования.'
    else:
        user.say 'Вы поговорили об успеваемости в школе, о двоечниках. Особой темой для разговора была [st.name]. Её оценки оставляют желать лучшего по сравнению со средним уровнем образования.'
    call screen show_stat

label dialog_teacher_0_2:
    $ st = getChar('','corrmax')
    if st.body.sex() == 'male':
        user.say 'Вы поговорили о поведении в школе, о хулиганах. Особой темой для разговора был [st.name]. Его поведение оставляет желать лучшего.'
    else:
        user.say 'Вы поговорили о поведении в школе, о хулиганах. Особой темой для разговора была [st.name]. Её поведение оставляет желать лучшего.'
    call screen show_stat

label dialog_teacher_0_3:
    $ st = getChar('','lustmax')
    if st.body.sex() == 'male':
        user.say 'Вы поговорили о поведении в школе, о хулиганах. Особой темой для разговора был [st.name]. Его поведение оставляет желать лучшего. Он попросту не пропускает ни одной юбки!'
    else:
        user.say 'Вы поговорили о поведении в школе, о хулиганах. Особой темой для разговора была [st.name]. Её поведение оставляет желать лучшего. Такое чувство, как будто она охотится за всеми парнями в школе.'
    call screen show_stat

label dialog_teacher_0_4:
    $ rep = getPar(studs, 'rep')
    if rep < 20:
        user.say 'Вы поговорили о Вашей низкой репутации. Преподаватель посочувствовал вам, пожелав удачи на новом месте работы.'
    elif rep < 50:
        user.say 'Вы поговорили о Вашей невысокой репутации. Преподаватель посоветовал вам уделять больше внимания личному общению с учениками.'
    elif rep < 80:
        user.say 'Вы поговорили о Вашей высокой репутации. Преподаватель порадовался, что у них наконец-то такой уважаемый директор.'
    else:
        user.say 'Вы поговорили о Вашей непревзойдённой репутации. Преподаватель искренне завидует Вашему всеобщему уважению.'
    call screen show_stat

label dialog_teacher_0_5:
    $ st = getChar('','edumax')
    if st.body.sex() == 'male':
        'Вы поговорили об успеваемости в школе, об отличниках. Особой темой для разговора был [st.name]. Его оценки просто прекрасны по сравнению со средним уровнем образования.'
    else :
        'Вы поговорили об успеваемости в школе, об отличниках. Особой темой для разговора была [st.name]. Её оценки просто прекрасны по сравнению со средним уровнем образования'
    call screen show_stat

label dialog_teacher_0_6:
    if user.getSex() == 'male':
        user.say '[user.name] 5 минут распинался про то, что не нужно химичке такое количество пробирок, колбочек, баночек и прочей фигни! Не нужно и всё! А у него мячей не хватает в спортзале. И одежды походу тоже.'
    else :
        user.say '[user.name], хихикнув, начала обсуждать нелёгкую жизнь Мустанговича. То ему мячей не хватает, то спортивной одежды...'
    call screen show_stat

label dialog_teacher_0_mustangovich1:
    if mile_quest_1 >= 1 and user == mustangovich:
        player.say 'Кстати, насчёт твоих таблеточек... У тебя не найдётся одной для меня?'
        user.say 'Для вас всё что угодно, [player.name]! Держите!'
        '[user.fname] протягивает вам одну из своих таблеток. Учитывая что капсула наполнена маленькими сердечками, неудивительно, что он думал, что это таблетки от сердца.'
        $ player.addItem(tablet)
    else:
        $ dialogueSelector(user)
    call screen show_stat

label dialog_teacher_20_1:
    $ st1 = getChar('female')
    $ st2 = getChar('male')
    if user.getSex() == 'male':
        user.say 'А вы видели, как сегодня выглядит [st1.name]? Я бы её э-х-х...'
        user.say 'Мы бы с ней о-о-о!'
        player.say 'В общем, всё как обычно, мыслите головкой, а не головой?'
        user.say 'Да...'
        player.say 'Это радостно, что в нашем бурном мире какие то вещи остаются неизменными.'
    else:
        user.say 'Я недавно видела мальчика на пляже... По-моему это был [st2.name]. Он такой, такой...'
        player.say 'Соблазнительный?'
        user.say 'Да! Именно это я и хотела сказать!'
    call screen show_stat
