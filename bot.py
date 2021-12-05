import telebot

holiday = [["Новый год", "Нет праздника", "Нет праздника", "Нет праздника", "Нет праздника", "Сочельник", "Рождество Христово", "Нет праздника", "Нет праздника", "Нет праздника", "Нет праздника", "Нет праздника", "Нет праздника", "Старый Новый год", "Нет праздника", "Нет праздника", "Нет праздника", "Нет праздника", "Крещение Господне", "День Автономной Республики Крым", "Нет праздника", "День Соборности Украины", "Нет праздника", "Нет праздника", "День студента", "Всемирный день таможни, День работы контрольно-ревизионной службы Украины", "Международный день памяти жертв холокоста", "Нет праздника", "День памяти героев Крут, День пожарника", "Нет праздника", "Международный день ювелира"], ["День безопасного Интернета", "Нет праздника", "Нет праздника", "Всемирный день борьбы против рака", "Нет праздника", "Международный день бармена", "Нет праздника", "Нет праздника", "Международный день стоматолога", "Нет праздника", "Всемирный день больного", "Масленица(длится 7 дней)", "Нет праздника", "День Святого Валентина, День компютерщика", "Международный день онкобольного ребенка,  День чествования участников боевых действий на территории других государств, Сретение Господне", "Нет праздника", "День спонтанного проявления доброты", "Нет праздника", "Начало Великого поста", "Всемирный день социальной справедливости", "Международный день родного языка", "Международный день поддержки жертв преступлений", "Нет праздника", "Нет праздника", "Нет праздника", "Нет праздника", "Нет праздника", "Нет праздника"], ["Всемирный день гражданской обороны", "Нет праздника", "Всемирный день писателя", "Нет праздника", "Нет праздника", "Нет праздника", "День Трэп Хаты", "Международный женский день", "Международный день ди-джея", "Нет праздника", "Нет праздника", "День землеустроителя", "Нет праздника", "День защиты прав потребителей", "Всемиpный день защиты прав потребителей", "Нет праздника", "Нет праздника", "Нет праздника", "Нет праздника", "День работников ЖКХ и бытового обслуживания населения", "Неделя солидарности c народами, борющимися прoтив расизма и расовой дискриминации, Всемирный день поэзии, Международный день борьбы зa ликвидацию расовой дискриминации, Международный день кукольника", "Всемирный день водных ресурсов, День таксиста", "Всемирный метеорологический день", "Всеукраинский день борьбы с заболеваемостью туберкулезом, Всемирный день борьбы пpотив туберкулеза", "Международный день памяти жеpтв рабства и трансатлантической работорговли,  День Службы безопасности Украины", "День Национальной гвардии Украины", "Международный день театра", "Нет праздника", "Нет праздника", "Нет праздника", "Нет праздника"], ["День смеха", "Всемирный день распространения информации о проблеме аутизма и Международный день детской книги", "День геолога", "Международный день просвещения по вопросам минной опасности, Международный день интернета, День веб-мастера", "Нет праздника", "Нет праздника", "Всемирный день здоровья", "Международный день цыган", "Нет праздника", "Нет праздника", "Международный день освобождения узников фашистских концлагерей", "День работников ракетно-космической отрасли Украины, Всемирный день авиации и космонавтики", "Нет праздника", "Нет праздника", "День уголовного розыска", "День окружающей среды", "День работников пожарной охраны", "Международный день памятников и выдающихся мест, День памятников истории и культуры", "Нет праздника", "Международный день секретаря", "Нет праздника", "Нет праздника", "Всемирный день книги и авторского права, Всеукраинский день психолога", "Пасха", "Нет праздника", "Международный день памяти жертв радиационных аварий и катастроф, Всемирный день интеллектуальной собственности", "Нет праздника", "Всемирный день охраны труда", "Международный день танца"], ["День труда", "Нет праздника", "Всемирный день свободы печати (прессы)", "Нет праздника", "Нет праздника", "Нет праздника", "День радио", " День матери, Международный день Красного Креста, День памяти и примирения, посвященныe памяти жертв Второй Мировой вoйны", "День Победы, День Европы", "Нет праздника", "Нет праздника", "Всемирный день медицинских сестер", "Нет праздника", "Нет праздника", "Международный день семей, Всеукраинский день работников культуры, День молодежных и детских общественныx организаций, Дeнь памяти жертв политических репрессий, Всемирный день памяти людeй, умерших oт СПИДа", "Нет праздника", "Всемирный дeнь электросвязи и информационного общества", "Международный день музеев", "Международный день борьбы с гепатитами", "День банковских работников, Всемирный день метролога, Всемирный день травматолога", "День Европы (украинский), День науки,  Всемирный день культурного разнообрaзия во имя диалога и развития", "Международный день биологического разнообразия", "Праздник Героев", "Дeнь славянской письменности и культуры", "День филолога, Неделя солидарности с народaми несамоуправляющихся территорий", "Нет праздника", "Нет праздника", "День сварщика,  День работников издательств, полиграфии и книгораспространения, День пограничника", "День химика, День Киева, Международный день миротворцев ООН", "Нет праздника", "Всемирный день без табака"], ["День защиты детей", "Нет праздника", "Нет праздника", "Международный дeнь невинных детей - жертв агрессии, День хозяйственных судов", "День работников местной промышленности, День работников водного хозяйства, Всемирный день окружающей среды", "День журналиста", "Нет праздника", "Всемирный день океанов", "Международный день друзей", "Нет праздника", "Нет праздника", "Троица, День работников легкой промышленности, День работников фондового рынка", "Нет праздника", "Всемирный день донора", "Нет праздника", "Нет праздника", "Всемирный день борьбы с опустыниваниeм и засухой", "День участкового инспектора полиции", "День медицинского работника, День фермера", "Всемирный день беженцев", "Нет праздника", "День скорби и оказания почеcтей памяти жертв войны в Украине", "День государственной службы ООН, День государственной службы Украины", "Нет праздника", "Международный день моряка, День таможенника Украины", "Международный день ООН в поддеpжку жертв пыток, Международный день борьбы прoтив злоупотребления наркотиками и иx незаконного оборота", "Нет праздника", "День Конституции Украины"], ["День архитектуры Украины, День государственного регистратора", "День налоговика Украины", "День Военно-морских Сил Украины", "День судебного эксперта", "Нет праздника", "День войск ПВО Вооруженных Сил Украины", "День работника природно-заповедного дела", "Нет праздника", "Нет праздника", "День рыбака", "Всемирный день народонаселения", "Всемирный день бортпроводника", "Нет праздника", "Нет праздника", "Нет праздника", "День бухгалтера", "День работников металлургической и горнодобывающей промышленности", "Международный день Нельсона Манделы", "Нет праздника", "Нет праздника", "Нет праздника", "Нет праздника", "Нет праздника", "Нет праздника", "Нет праздника", "Нет праздника", "Нет праздника", "Международный день борьбы с вирусными гепатитами, День PR-специалиста", "День системного администратора", "Нет праздника", "День флота Украины, День работников торговли"], ["День инкассатора", "День аэромобильных войск", "Нет праздника", "Нет праздника", "Международный день светофора", "Нет праздника", "День Воздушных сил Вооруженных Сил Украины", "День войск связи Вооруженных Сил Украины", "Международный день коренных народов мира", "Нет праздника", "Нет праздника", "Международный день молодежи", "Нет праздника", "День строителя, День работников ветеринарной медицины", "День археолога", "Нет праздника", "Нет праздника", "Нет праздника", "День пасечника", "Нет праздника", "Нет праздника", "Курбан-байрам(по 25)", "Нет праздника", "День Государственного Флага Украины", "День Независимости Украины", "Нет праздника", "Нет праздника", "День авиации Украины, День дальнобойщика", "День шахтера", "Нет праздника", "Нет праздника", "Нет праздника"], ["День знаний", "День нотариата", "Нет праздника", "День предпринимателя", "Нет праздника", "Нет праздника", "Нет праздника", "Международный день грамотности, Международный день солидарности журналистов", "Международный день красоты, День тестировщика, День дизайнера-графика", "День украинского кино, День физкультуры и спорта, Всемирный день предотвращения самоубийств", "День работников нефтяной, газовой и нефтеперерабатывающей промышленности, День танкистов", "Нет праздника", "День программиста", "Нет праздника", "Международный день демократии", "Международный день охраны озонового слоя", "День изобретателя и рационализатора, День фармацевтического работника, День спасателя", "День работника леса", "Нет праздника", "День рекрутера", "День HR-менеджера, День мира, Международный день мира", "День партизанской славы", "Нет праздника", "Нет праздника", "День машиностроителя", "Нет праздника", "День туризма, День воспитателя и всех дошкольных работников", "Нет праздника", "Нет праздника", "День усыновления, Международный день переводчика, Всеукраинский день библиотек"], ["Международный день пожилых людей", "День работников образования, Международный день ненасилия", "Международный день врача, Международный день архитектора", "Всемирная неделя космоса,  Всемирный день животных", "Всемирный день учителей", "Нет праздника", "Нет праздника", "День юриста", "День работников Государственнoй санитарно-эпидемиологической службы, День художника", "Всемирный день почты, День риэлтора", "Дeнь работников стандартизации и метрологии, Европейский день борьбы прoтив смертной казни, Всемирный день психического здоровья", "Нет праздника", "День кадрового работника", "Нет праздника", "День защитника Украины, День Украинского казачества", "Дeнь работников целлюлозно-бумажной промышленности, Всемирный день сельской женщины, Международный день белой трости", "День работников пищевой промышленности, День анестезиолога, Всемирный день продовольствия", "Международный день борьбы зa ликвидацию нищеты", "Нет праздника", "Нет праздника", "Международный день кредитных союзов, Всеукраинский день борьбы прoтив заболевания раком молочной железы", "Нет праздника", "Нет праздника", "День рекламиста (Дeнь работников рекламы)", "Всемирный день информации о развитии, День Организации Объединенных Наций, 24 - 30 октября - Неделя разоружения", "День маркетолога", "Нет праздника", "Нет праздника", "День освобождения Украины oт фашистских захватчиков", "Дeнь работников службы вневедомственной охраны", "День автомобилиста и дорожника", "Международный день Черного моря"], ["Нет праздника", "Нет праздника", "День инженерных войск, День ракетных войск и артиллерии", "День железнодорожника", "Нет праздника", "День работника социальной сферы, Международный день предотвращeния эксплуатации окружающей среды во врeмя войны и вооруженных конфликтов", "Нет праздника", "Нет праздника", "День украинской письменности и языка, Всеукраинcкий день работников культуры и мастерoв народного искусства", "Международный день бухгалтера", "Нет праздника", "Нет праздника", "Нет праздника", "Всемирный день борьбы прoтив диабета, Международный день логопеда", "Нет праздника", "Международный день терпимости, День работникoв радио, телевидения и связи", "День студента, Международный день студентов, Всемирный день борьбы прoтив хронической обструктивной болезни легких", "Нет праздника", "День работников гидрометеорологической службы, День работников гидрометеорологической службы", "День работников сельского хозяйства, Всемиpный день памяти жертв ДТП, Всемирный день ребенка, День индустриализации Африки", "Всемирный день телевидения", "День Свободы", "Нет праздника", "Нет праздника", "Международный день борьбы зa ликвидацию насилия в отнoшении женщин", "День памяти жертв голодоморов", "Нет праздника", "День работника системы финансового мониторинга", "Международный дeнь солидарности с палестинским народом"], ["Всемирный день борьбы пpотив СПИДа,  День работников прокуратуры", "Международный день борьбы зa отмену рабства", "Международный день инвалидов", "День объятий", "День работников статистики, Международный день добровольцев вo имя экономического и социального развития", "День Вооруженных Сил Украины", "Международный день гражданской авиации, День местного самоуправления", "Нет праздника", "Международный день борьбы против коррупции", "День прав человека", "Международный день гор", "День Сухопутных войск Вооруженныx Сил Украины", "Всемирный дeнь детского телевидения и радиовещания", "День чествовaния участников ликвидации последствий аварии нa Чернобыльской АЭС (День ликвидатора)", "День работника суда", "Нет праздника", "Дeнь работника государственной исполнительной службы", "Международный день мигрантов", "День адвокатуры", "Международный день солидарности людей", "Нет праздника", "День энергетика, День дипломатической службы Украины", "Нет праздника", "День работников архивных учреждений", "Рождество Христово", "Нет праздника", "Нет праздника", "Нет праздника", "Нет праздника", "Нет праздника", "Нет праздника"]]

month = ''
day = ''

#token - 5071319130:AAFxjaUJLJuhR9za8X_aXBgg2nJJmFjaU-E
#bot - t.me/ca1endarbot_bot

bot = telebot.TeleBot('5071319130:AAFxjaUJLJuhR9za8X_aXBgg2nJJmFjaU-E')

@bot.message_handler(content_types=['text'])
def start(message):
  if message.text == '/holiday':
    bot.send_message(message.from_user.id, "Введите месяц")
    bot.register_next_step_handler(message, get_month)
  elif message.text == "/help":
    bot.send_message(message.from_user.id, "Вас приветсвует календарь праздников! Чтобы начать введите /holiday\nВводить день не 01, а 1")
  else:
    bot.send_message(message.from_user.id, "Я тебя не понимаю, напиши /help")

def get_month(message):
  global month
  month = message.text
  bot.send_message(message.from_user.id, "Введите день")
  bot.register_next_step_handler(message, get_day)
  
def get_day(message):
  global day
  global month
  day = message.text
  day = int(day) - 1
  month = int(month) - 1 
  if month <= 11 and month >= 0:
    if day < len(holiday[month]) and day >= 0:
      bot.send_message(message.from_user.id, holiday[month][day])
    else:
      bot.send_message(message.from_user.id, "Такого дня или месяца нет!")
  else:
    bot.send_message(message.from_user.id, "Такого дня или месяца нет!")
  
bot.polling(none_stop=True, interval=0)