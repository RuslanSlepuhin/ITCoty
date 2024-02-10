greet = "Привет, {name},  я ITCoty бот который поможет вам найти работу в IT. Нажмите 'найти вакансии' и выберете желаемые параметры для подбора."
menu = "Меню фильтра вакансий"
info = 'Я ITCoty бот который поможет вам найти работу в IT,\nДля прохождения опроса команда "start" \n Для вывода меню фильра вакансий команда "menu".'
direction = "Необходимо выбрать IT направление"
get_vacancy = "Поиск вакансий по базе"
sent_first_question = "Привет! Давайте начнем заполнение данных. Как вас зовут?"
get_notification = "Необходимо выбрать подходящую периодичность"

create_table = """CREATE TABLE tg_bot ( user_id bigint ,name varchar(255), email varchar(255),direction varchar(255), specialization varchar(255),location varchar(255),salary_rate varchar(255),work_format varchar(255),keywords varchar(255),CV_url varchar(255)) """
skip_continue = "Skip & Continue"

# Главное меню
vacancy_filter = "Фильтр вакансий"
start_survey = "Пройти опрос"
notification = "Периодичность уведомлений"
user_profile = "Профиль на сайте"
restart = "Прекращение выдачи"
# Направления
design = "Design"
# Специализации 'Design'
motion = "Motion"
three_d = "3D"
ux_ui = "UX/UI"
illustrator = "Illustrator"
graphic = "Graphic "
designer = "Designer "

backend = "Backend"
# Специализации backend
one_c = "1C"
java = "Java"
python = "Python"
php = "PHP"
c_plus_plus = "C++"
c_sharp = "C#"
dot_net = ".Net"
golang = "Golang"

analyst = "Analyst"
# Специализации analyst
system_analyst = "System Analyst"
ba = "BA"

mobile = "Mobile"
# Специализации mobile
ios = "IOS"
android = "Android"
flutter = "Flutter"

marketing = "Marketing"
# Специализации marketing
seo = "SEO"
copywriter = "Copywriter"
marketer = "Marketer"
content_manager = "Content manager"
media_buyer = "Media buyer"

product_project_manager = "Product & Project manager"
# Специализации Product & Project manager
project_manager = "Project manager"
product_manager = "Product manager"

sales = "Sales"
# Специализации Sales

dev_ops = "DevOps"
# Специализации DevOps

frontend = "Frontend"
# Специализации Frontend
react = "React"
angular = "Angular"
vue = "Vue"

support = "Support"
# Специализации Support

fullstack = "Fullstack"
# Специализации Fullstack

hr = "HR"
# Специализации HR

game_dev = "GameDev"
# Специализации GameDev
unity = "Unity"
game_designer = "Game designer"

qa = "QA"
# Специализации QA
manual = 'Manual'
auto = 'Auto'
# Уровень по вакансиям
trainee = "Trainee"
junior = "Junior"
middle = "Middle"
senior = "Senior"
tech_lead = "Lead"

# Формат работы
remote = "Remote"
office = "Office"
hybrid = "Hybrid"
part_time = "Part_time"
full_time = "Full_time"
any_format = "Any"
