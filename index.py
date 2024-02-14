'''
import time
import imaplib
import email

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)
import pyautogui

#Configurações IMAP
imap_host = 'imap.gmail.com'
username = 'welerson.mateus0510@shopeemobile-external.com'
password = '88254099'

#Conexão IMAP
mail = imaplib.IMAP4_SSL(imap_host)
mail.login(username, password)
mail.select('inbox')

# Procurar por emails não lidos

result, data = mail.search(None, 'UNSEEN')
ids = data[0].split()

for email_id in ids:
    #Obter o conteúdo do email
    result, data = mail.fetch(email_id, 'RFC822')
    raw_email = data[0][1]
    msg = email.message_from_bytes(raw_email)

    #Exibe o Remetente e o Assunto do Email
    print('Remetente', msg['from'])
    print('Assunto', msg['Subject'])

    #Fecha a conexão IMAP

    mail.close()
    mail.logout()
'''

from imap_tools import MailBox, AND
import imaplib
#Configurações IMAP
imap_host = 'imap.gmail.com'
username = 'welerson.cote2@gmail.com'
password = 'rnbmxigqeimorxbh'

#Conexão IMAP
mail = imaplib.IMAP4_SSL(imap_host)
mail.login(username, password)
mail.select('inbox')

username = 'welerson.cote2@gmail.com'
password = 'rnbmxigqeimorxbh'

meu_email = MailBox('imap.gmail.com').login(username, password)

list_emails = meu_email.fetch(AND(from_='contato@thenewscc.com.br'))

"""print(len(list(list_emails)))  """

for email in list_emails:
    print(email.subject)
    print(email.text.encode)
