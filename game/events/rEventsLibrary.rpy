label event_loc_library_0_no1:
    show library
    python:
        st1 = getChar('female')
    show expression 'pic/locations/school/library/no1.jpg' at top as tempPic
    '[st1.fname] судя по всему совсем увлеклась чтением фентези и прочих Леголасов. Даже кота своего притащила, чтобы кормить его не отвлекаясь от чтения.'
    menu:
        'Попросить ученицу убрать животное':
            'Вы просите ученицу убрать кота из библиотеки, потому что он может испортить книги.'
            'Ученица нехотя прерывает чтение и, взяв кота подмышку уходит на улицу.'
            if player.getCorr() > 80:
                show expression 'pic/locations/school/library/no1_1.jpg' at top as tempPic
                player.say '"Кошки - пфф, мелкие проказники! Вот большие собаки - это да! Они и защитят, и убаюкают!"'
                'Ваши мысли затуманились картинкой того, что могло бы произойти, будь у вас собака. Как её огромный член проникает в вашу киску, как в ней раздувается узел, не давая ему выскочить из вас. Вы почти чувствуете, как увлажняется ваша распутная щёлка от подобных мыслей.'
                $ player.incLust(15)
            $ st1.incLoy(-5)
        'Не обращать внимания':
            $ st1.incLoy(5)
            'Вы решаете ничего ей не говорить. И прощаетесь.'
            if rand(1,5) == 1:
                'Как вдруг котяра с воем бросается на ближайшую полку, и раздирает несколько журналов простым прикосновением когтей! Чёрт возьми, эти игры кота встали школе в 500 монет! В наказание вы заставляете ученицу остаться после уроков.'
                $ school.budget -= 500
                $ detentions.append(st1)
    $ move(curloc)
    
label event_loc_library_0_no2:
    show library
    python:
        st1 = getChar('female')
        st2 = getChar('male')
    show expression 'pic/locations/school/library/no2.jpg' at top as tempPic
    'Заметив, что вы идёте, [st1.fname] прикрыла спиной книгу, которую она выбрала для чтения.'
    menu:
        'Узнать, что за книга':
            player.say 'Ну ка, покажи что ты там прячешь!'
            if st1.getCorr() > 20:
                show expression 'pic/locations/school/library/no2_2.jpg' at top as tempPic
                'Смущаясь, ученица протягивает вам обычную мангу с искромётным названием "Мой любимый директор". У вас не находится сил отбирать эту брошюру.'
                $ st1.incLoy(10)
            else:
                'В ответ нехотя ученица протягивает вам "Индульгенция, как способность индидуума абстрагироваться от религиозной самонедостаточности" В.Ю. Фрейта. Вы не видите в ней ничего страшного, и нехотя возвращаете книгу. Была надежда поймать что то более приземлённое, чем религиозная тема.'
                player.say '"Она что, в монашки собралась после школы?"'
                $ st1.incLoy(-5)
        'Не обращать внимания':
            'Вы решаете не обращать внимания на странное поведение, но бросив случайный взгляд на полку, заметили цветастую корку с надписью "Крашмапутра". Уж не эту ли книгу искала ученица? Судя по её румянцу, вы не ошиблись.'
            if player.getCorr() > 60 and st2.getCorr() > 70:
                show expression 'pic/locations/school/library/no2_1.jpg' at top as tempPic
                'Не сдержавшись, вы решаете пролистать этот известный труд, и с удивлением видите, что он проиллюстрирован вполне известными вам людьми. Это [st2.name] и его мама. Подпись к картинке гласит: "И как мать обнимает своего сына, так и вы прижмите своего любовника к своему телу и слейтесь с ним в экстазе. Nбург, [str(year)] год."'
                player.say '"Однако вряд ли они мне будут доставлять проблемы с репутацией. С таким то компроматом!"'
                $ st2.incRep(25)
                $ player.incLust(10)
    $ move(curloc)
    
label event_loc_library_0_no3:
    show library
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        incLust(5,10)
    show expression 'pic/locations/school/library/no3.jpg' at top as tempPic
    '[st1.fname] и [st2.fname], сидя на полу читают какую то брошурку. Блин, они же так простудятся, будут болеть дома, и не посещать школу!'
    if player.getCorr() < 40:
        'Вы просите девчёнок пересесть за стол, благо строительная компания озаботилась не только стенами, но и мебелью.'
    else:
        show expression 'pic/locations/school/library/no3_1.jpg' at top as tempPic
        player.say '"Надеюсь это какой то хентай, с кучей молодых тел, множеством членов и спермы, и главное - без цензуры!"'
    $ move(curloc)
        