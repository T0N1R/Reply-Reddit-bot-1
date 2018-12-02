#! /usr/local/bin/python
'''
Author: T0N1R
" 'Thank you for doing your part' bot, El objetivo de este programa es responder a todos los posts que contengan las frase 'I'm doing my part'
con un comentario. en este caso, se contesta:

'**Clap** **Clap**' + '\n' + '   Thanks for helping the 9 year old army!' + '\n' + '\n' + 'I am a bot :V'

Se da esta respuesta por el contexto del subreddit en el que se habia utilizado 
'''
import praw
import time
import sys

a = 1
while a>0:
        reddit = praw.Reddit(client_id='INGRESAR ID', 
                        client_secret='INGRESAR SECRETO',
                        password='INGRESAR CONTRASEÑA', 
                        user_agent='USER_AGENT',
                        username='USERNAME')

        #elegir subreddit (en este caso PewdiepieSubmissions)
        subreddit = reddit.subreddit('PewdiepieSubmissions')

        #frases que se buscarán en el título del post
        frases = ['doing my part', 'doing my part!', 'doing my part!!', 'doing my part!!!', 'doing your part']

        #respuesta
        respuesta = '**Clap** **Clap**' + '\n' + '   Thanks for helping the 9 year old army!' + '\n' + '\n' + 'I am a bot :V'

        non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

        for submission in subreddit.stream.submissions():
                try:
                        titulo = submission.title

                        #para evitar errores al haber un emoji en el titulo
                        titulo = titulo.translate(non_bmp_map)
                        titulo = titulo.lower()


                        for i in frases:
                                if i in titulo:
                                        print (titulo)
                                        submission.reply(respuesta)
                
                except praw.exceptions.PRAWException as e:
                        pass

