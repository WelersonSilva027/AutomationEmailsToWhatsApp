from imap_tools import MailBox, AND
import imaplib
#Configurações IMAP
imap_host = 'imap.gmail.com'
username = '' #EMAIL
password = '' #CHAVE DE ACESSO

#Conexão IMAP
mail = imaplib.IMAP4_SSL(imap_host)
mail.login(username, password)
mail.select('inbox')

username = ''
password = ''

meu_email = MailBox('imap.gmail.com').login(username, password)

list_emails = meu_email.fetch(AND(from_='contato@thenewscc.com.br'))


from unidecode import unidecode
# Função para converter texto Unicode em ASCII aproximado
def sanitize_text(text):
    return unidecode(text)

# Loop sobre os e-mails e imprimir o assunto e o texto, utilizando a função sanitize_text
for email in list_emails:
    print(sanitize_text(email.subject))
    print(sanitize_text(email.text))



"""# Função para substituir caracteres problemáticos por '?'
def sanitize_text(text):
    return ''.join(char if ord(char) < 128 else '?' for char in text)

# Loop sobre os e-mails e imprimir o assunto e o texto, utilizando a função sanitize_text
for email in list_emails:
    print(sanitize_text(email.subject))
    print(sanitize_text(email.text))"""


    


