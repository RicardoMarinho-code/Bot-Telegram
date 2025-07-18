import telebot
Chave_API = 'CHAVE_API_AQUI'

#cria o bot
bot = telebot.TeleBot(Chave_API)

#handler para responder caso escolha PE
@bot.message_handler(commands = ["PE"]) #message_handler é o que vai responder quando o usuário digitar /PE
def PE(mensagem):
    bot.send_message(mensagem.chat.id, "Vixe, não sei. Clique aqui para /iniciar")

@bot.message_handler(commands = ["ES"])
def ES(mensagem):
    bot.send_message(mensagem.chat.id, "Rapaz, e você acha que eu sei? Clique aqui para /iniciar") #send_message envia uma mensagem para o usuário

@bot.message_handler(commands = ["opcao1"]) 
def opcao1(mensagem):
    texto = """Sobre Engenharia de Software:
    
/PE para assuntos sobre Programação Estruturada
/ES para assuntos sobre Engenharia de Software
"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands = ["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Júnio entende muito sobre criptos. Qual é a sua dúvida?")

@bot.message_handler(commands = ["opcao3"])
def opcao3(mensagem):

    RaizTech = ("A RaizTech é uma startup do Juninho voltada para tecnologias para o Agro."
                " Ela é uma nova classe de irrigadores, os chamados Irrigadores Inteligentes, "
                "tratando de automação e gerenciamento de irrigação inteligente para plantações."
                " Com isso, a plantação pode ter uma economia hídrica de 50% e aumento na produção "
                "de até 100%, comparado com outros meio de irrigação.")
    bot.send_message(mensagem.chat.id, RaizTech)

def verificar(mensagem):
    return True

#se nenhum comando aparecer, aparece a mensagem
@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Não entendi o que você quis dizer. Escolha uma das opções abaixo:
    
/opcao1 Assuntos sobre Engenharia de Software
/opcao2 Assuntos sobre criptos
/opcao3 assunstos sobre a RaizTech

Responder outra opção não vai funcionar, escolha uma opção."""
    bot.reply_to(mensagem, texto)

bot.polling()
