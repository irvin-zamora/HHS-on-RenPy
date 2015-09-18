label cabbageInit:
    $ p = player
    $ s = secretary
    show expression Image('pic/events/cabbage/secretary.png', xalign=0.8, yalign= 0.8, yanchor = 'center') as char1 
    show expression getCharImage(player,'dialog') as char2
    p.say 'Здравствуйте, что Вы здесь делаете? - интересуетесь вы у незнакомца в вашем кабинете.'
    s 'Приятно познакомится, [p.name], если я не ошибаюсь?'
    'Мужчина наклоняется к вам, и галантно целует ручку.'
    p.say 'Да, вы не ошиблись, с кем имею честь? - принимаете вы правила игры, начиная изображать из себя великосветскую львицу.'
    s 'Александр, для Вас просто Александр, - поправляет свой галстук мужчина.'
    p.say 'Просто Александр может перейти ближе к делу?'
    s 'Ну размумеется. В общем я представляю компанию по выращиванию овощей, и занимаюсь рекрутингом, - начинает объяснять мужчина.'
    p.say 'В школе? - выгибаете вы бровь.'
    s 'Да, в школе... У нас уродился ОГРОМНЫЙ урожай капусты, и нам необходимо её собрать. С министерством всё согласовано, дело осталось за вами.'
    'Он протягивает вам какие то бумаги. Быстро пробежавшись по ним глазами, вы выясняете, что подписав, сможете отправлять учителей и школьников на уборку капусты хоть ежедневно. Но платить вам будут в зависимости от собранного количества.'
    p.say 'Мне необходимо отправлять их каждый день? - задаёте вы уточняющий вопрос.'
    s 'Как захотите, автобус будет ждать вас с 7 до 8. Если никто не появится, то он поедет собирать людей в другом месте, - пожимает плечами Александр.'
    'Не вижу причин отказываться от столь привлекательного предложения! - Вы подмахиваете документ и прощаетесь с мужчиной.'
    $ is_cabbage = 1
    $ move(curloc)
    
label cabbageStart:
    'Собрав всех учеников, и объявив им что сегодня вместо занятий все отправляются на заготовку овощей, вы под радостный вой загнали всех в автобус и отправились покорять капусту.'
    'В пути студенты веселились и шутили, чем подняли себе настроение. Спустя час, вы прибыли на место и тут же взяли на себя руководящую роль, отправив учеников на заготовки, учителей на сортировку. Для себя вы приготовили занятие получше - отдохнуть, походить и посмотреть что да как'
    if stat_fun < 20: 
        $ setFun(50,4)
        $ setLoy(50,4)
    $ cabbage_eff = 0
    jump cabbageIn
    
label cabbageIn:
    $clrscr()
    hide tempPic
    if hour > 18:
        jump cabbageEnd
    show expression 'pic/events/cabbage/cabbage.png' at top as bg
    menu:
        'Погоды стоят жаркие, ученики работают, все при деле. Чем бы заняться самой?'
        'Погулять пару часиков' if player.getEnergy() >= 300:
            if rand(1,3) == 1:
                $ changetime(120)
                $ tryEvent('loc_cabbage')
            else:
                'Вы погуляли пару часиков, но ничего интересного не встретили. Зато эта прогулка положительно сказалась на вашем здоровье!'
                $ player.setHealth(10)
                $ player.setEnergy(-250)
                $ changetime(120)
            jump cabbageIn
        'Надзирать за работой' if player.getEnergy() >= 300:
            show expression 'pic/events/cabbage/angry.png' at left as tempPic
            'Вы 2 часа гоняли учеников в хвост и гриву, заставляя их работать. Это безусловно скажется на их эффективности положительно, но вот на лояльности к вам - отрицательно. К тому же постоянный надзор - жутко утомительное занятие.'
            python:
                cabbage_eff += 1
                setFun(50,-1)
                setLoy(50,-1)
                changetime(120)
            jump cabbageIn
        'Отдохнуть пару часиков':
            show expression 'pic/events/cabbage/rest.png' at top as tempPic
            'Вы отдохнули пару часиков, глядя на облачка, и, кажется, даже всхрапнув минут на 40. Вроде самочуствие улучшилось, да и сил прибавилось.'
            python:
                changetime(120)
                player.setEnergy(150)
            jump cabbageIn

label cabbageEnd:
    $ clrscr()
    $ cabbage_eff += int((100 - stat_corr)/20)
    show expression 'pic/events/cabbage/farmer.jpg' at top as bg
    'К концу дня к вам подходит фермер. Владелец поля на котором работали ваши ученики.'
    if cabbage_eff >= 9:
        farmer 'Ваши ученики - великолепные работники! Никогда таких не видел! Просто загляденье, вот что значит строгий учитель и прилежание! - радостно сказал он, начиная отсчитывать Ваш дневной заработок.'
    elif cabbage_eff >= 6:
        farmer 'Ваши ученики - хорошие работники! Но могли бы постараться и  получше! - улыбаясь сказал он, подсчитывая Ваш дневной заработок.'
    elif cabbage_eff >= 3:
        farmer 'Ваши ученики - весьма посредственные работники... Хотя учитывая то, что работа сдельная... И так сойдёт, - хмурясь сказал он, подсчитывая Ваш дневной заработок.'
    else:
        farmer 'Не видел я хуже работников. Просто не видел. Младенец сможет натаскать больше, чем ваши озабоченные остолопы, - недовольно бросил он, подсчитывая ваш дневной заработок и свой убыток.'
    python:
        cabbage_eff = max(1,cabbage_eff)
        temp = int(cabbage_eff*rand(500,600))
        school.budget += temp
    'Вы пересчитали купюры, оказалось, что за сегодня ваши ученики заработали [temp] монет. Жаль, что все эти деньги пройдут мимо вашего кармана, прямо в школьный бюджет.'
    $ move(curloc)
    
label event_loc_cabbage_1:
    'Прогуливаясь, Вы наткнулись на небольшой сарайчик из которого доносились стоны и крики.'
    menu:
        'Заглянуть' if player.getCorr() > 20:
            show expression 'pic/events/cabbage/ahmed_sex.jpg' at top as tempPic
            'Аккуратно заглянув в окошко, Вы увидели там вашего физрука, беззастенчиво трахающего в задницу жену фермера. Мало того, он использовал морковку на её текущей киске, осуществляя двойное проникновение.'
            player.say 'Афигеть... - тихо прошептали вы, ощущая как теплеет в вашем животе. Рыкнув в очередной раз, Ахмед загнал весь свой член в задницу женщины, и протолкнул поглубже морковку.'
            mustangovich.say 'Класс! - выдохнул он, и его член начал дёргаться внутри её попки, расширяя сфинктер уже совсем до неприличных размеров'
            $ renpy.say('Настасья Прокофьевна', 'Мой мустанг! - закричала изменщица, кончая.')
            'Вы поспешили убраться подальше, предварительно запомнив местоположение сарайчика'
            $ player.setLust(15)
            $ mile_qwest_2_Ahmed = 1
        'Убежать':
            'Вы решили не испытывать судьбу, и, боясь быть замеченной за столько неприглядным занятием, убегаете.'
    $ hadSex(mustangovich)
    $ mustangovich.setLust(-100)
    jump cabbageIn
    
label event_loc_cabbage_2:
    $st1 = getChar('male')
    show expression 'pic/events/cabbage/2.jpg' at top as tempPic
    'Идя по дороге, Вы встретили селянку о чём то разговаривающую с вашим учеником. Вас довольно сильно удивило то, что через 5 минут разговора, она неожиданно подняла своё платье, и принялась активно поглаживать свою текущую киску перед оторопевшим парнем.'
    p.say '[st1.name]! - окликнули вы парня, и выразительно показали пальцем в сторону капустного поля.'
    'Вам не особо хочется, чтобы по городу начали распространятся слухи о том, что вы тут какой то секс туризм в глубинку устроили.'
    $ player.setLust(5)
    $ st1.setLust(20)
    jump cabbageIn
    
label event_loc_cabbage_3:
    show expression 'pic/events/cabbage/3.jpg' at top as tempPic
    $ renpy.say('Прошка', 'Да, Рекс, да!!!.')
    'Вы с удивлением узнали в кончающей девушке дочь фермера.'
    'Её всю заливала сперма из огромного члена пса. И как чёрт побери в такой девочке уместился такой член? Вы поспешили смотаться, пока Вас не заметили.'
    $ player.setLust(15)
    jump cabbageIn
    
    
    
    