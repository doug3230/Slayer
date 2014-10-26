'''
Created on Oct 25, 2014

@author: Richard
'''
import pygame

def load_music(file_name, path_included = False):
    if not path_included:
        pygame.mixer.music.load(path_to_music(file_name))
    else:
        pygame.mixer.music.load(file_name)
    return

def play_music(loop = True):
    if loop:
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.play()
    return
    
def stop_music():
    pygame.mixer.music.stop()
    return

def load_image(file_name, path_included = False):
    if not path_included:
        image = pygame.image.load(path_to_image(file_name))
    else:
        image = pygame.image.load(file_name)
    return image.convert()

def resize_image(image, new_width, new_height):
    image = pygame.transform.scale(image, (int(new_width), int(new_height)))
    return image.convert()

def path_to_image(file_name):
    return "files/images/{0}".format(file_name)

def path_to_music(file_name):
    return "files/music/{0}".format(file_name)

def path_to_level(file_name):
    return "files/levels/{0}".format(file_name)
