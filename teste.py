from pytube import YouTube
from pytube import Playlist
import os

#Variaveis 
path = os.getcwd() + '/download'
op = '0'
url = ''

def video_download(url):
    try:
        yt = YouTube(url)
        print('\nDownload...')
        yt.streams.get_highest_resolution().download(output_path=path + '/videos')
    except Exception as e:
        return 'Ocorreu um erro '
    
    return 'concluido'

def audio_download(url):
    try:
        yt = YouTube(url)
        print('\nDownload...')
        yt.streams.filter(only_audio=True).first().download(output_path=path + '/audio', filename= yt.title + '.mp3')
    except Exception as e:
        return 'Ocorreu um erro '  
    
    return 'concluido'

def playlist_download_video(url):
    try:
        p = Playlist(url)
        print(f'Downloading(video): {p.title}')
        for v in p.videos:  
            v.streams.get_highest_resolution().download(output_path=path + '/videos/' + p.title)
            print(v.title)
        return 'concluido'
    except Exception as e:
        return 'ocorreu um erro'
    
def playlist_download_audio(url):
    try:
        p = Playlist(url)
        print(f'Downloading(audio): {p.title}')
        for v in p.videos:  
            v.streams.filter(only_audio=True).first().download(output_path=path + '/audio/' + p.title, filename= v.title + '.mp3')
            print(v.title)
        return 'concluido'
    except Exception as e:
        return 'ocorreu um erro'





# while True:
#     url = input('Qual a url (ou digite "sair" para encerrar): ')
    
#     if url.lower() == 'sair':
#         print('\nSaindo...')
#         break

#     while op != '3':
#         print('Escolha uma opção \n')
#         print('1 - Video (qualidade mais alta)')
#         print('2 - Audio')
#         print('3 - playlist(video)')
#         print('4 - playlist(audio)')
#         print('5 - Sair')
#         op = input(': ')

#         if op == '1':
#             result = video_download(url)
#             print('\n' + result + '\n')
#             break
#         elif op == '2':
#             result = audio_download(url)
#             print('\n' + result + '\n')
#             break
#         elif op == '3':
#             result = playlist_download_video(url)
#             print('\n' + result + '\n')
#             break        
#         elif op == '4':
#             result = playlist_download_audio(url)
#             print('\n' + result + '\n')
#             break        
#         elif op == '5':
#             print('\nSaindo...')
#             break
#         else:
#             print('Opção inválida')
            

while True:
    print('--------- Baixador de Video ---------')
    print('1-Video')
    print('2-playlist')
    print('digite: \"sair\" para sair')
    e = input(': ')
    
    if e == 'sair':
        print('\nSaindo...')
        break
    
    while True:
    
        if e == '1':
            print('Videos Unico')
            
            url = input('Qual a url (ou digite "sair" para encerrar): ')
            if url.lower() == 'sair':
                print('\nSaindo...')
                break
        
            while op != '3':
                print('Escolha uma opção \n')
                print('1 - Video (qualidade mais alta)')
                print('2 - Audio')
                print('3 - Sair')
                op = input(': ')

                if op == '1':
                    result = video_download(url)
                    print('\n' + result + '\n')
                    break
                elif op == '2':
                    result = audio_download(url)
                    print('\n' + result + '\n')
                    break     
                elif op == '3':
                    print('\nSaindo...')
                    break
                else:
                    print('Opção inválida')
                break
        
        elif e == '2':
            print('Playlist')
            
            url = input('Qual a url (ou digite "sair" para encerrar): ')
            if url.lower() == 'sair':
                print('\nSaindo...')
                break
            
            while op != '3':
                print('Escolha uma opção \n')
                print('1 - playlist(video)')
                print('2 - playlist(audio)')
                print('3 - Sair')
                op = input(': ')

                if op == '1':
                    result = playlist_download_video(url)
                    print('\n' + result + '\n')
                    break        
                elif op == '2':
                    result = playlist_download_audio(url)
                    print('\n' + result + '\n')
                    break        
                elif op == '3':
                    print('\nSaindo...')
                    break
                else:
                    print('\nOpção inválida')
                break
            
            break
        else :
            print('\nOpção inválida')
            break