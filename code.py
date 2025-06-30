from PIL import Image
import numpy as np

#Mettre des commentaire pour expliquer ce que font chaque fonction
#ouvrir l'image
def ouvImage(img_path):
	img = Image.open(img_path)
	return img

#récuperer la largeur et la hauteur
def tailleImage(img):
	largeur,hauteur = img.size
	return largeur,hauteur

#transformer le texte en format binair et rajouter la clé
def txt2Binair(txt):
	txt_binair=''
	for c in txt:
		txt_binair += format(ord(c), '08b')
	txt_binair += '1111111111111110'
	return txt_binair
	
#veriffier la taille de l'image par rapport au texte
def TailleImageValid(txt_binair,l,h):
	if len(txt_binair) > l * h * 3:
		print("L'image est trop petite pour contenir le texte.")
		return False
	return True
	
#curseur 
def iterateur(txt_binair):
	iterateur=iter(txt_binair)
	return iterateur
	
#sauvgarder l'image 
def sauvImage(img, path_sauv):
	img.save(path_sauv)
	
#transormer les pixels en liste de valeurs 
def recupPixelEnArray(img):
	pixels = list(img.getdata())
	pixels_array = np.array(pixels)
	return pixels_array
	
#ajouter le texte dans l'image
def ajoutTxtImageRGB(img,l,h,txt_binair, path_sauv):
	iterateur=iter(txt_binair)
	for i in range(l):
		for j in range(h):
			r, v, b = img.getpixel((i, j))
			try:
				img.putpixel((i, j), (r - r % 2 + int(next(iterateur)), v - v % 2 + int(next(iterateur)), b - b % 2 + int(next(iterateur))))
			except StopIteration:
				sauvImage(img, path_sauv)
				return
	print("save")
	sauvImage(img, path_sauv)
	
#recuperer le texte normal a partire du texte binair
def binair2txt(txt_binair):
	txt = ''
	for i in range(0, len(txt_binair)-16, 8):
		txt += chr(int(txt_binair[i:i+8], 2))
	return txt
	
#recuperer le texte de l'image
def retraitTxtImageRGB(img,l,h):
	txt_binair = ''
	for i in range(l):
		for j in range(h):
			r, v, b = img.getpixel((i, j))

			txt_binair += str(r % 2)
			txt_binair += str(v % 2)
			txt_binair += str(b % 2)

			if txt_binair[-16:] == '1111111111111110':
				txt = binair2txt(txt_binair)
				print(txt)
				return txt


#remplacer ? par TailleImageValid, ouvImage, ajoutTxtImageRGB, txt2Binair, tailleImage
def cacher_texte_dans_image(img_path, txt, path_sauv):
	img=ouvImage(img_path)
	l,h=tailleImage(img)
	txt_binair=txt2Binair(txt)
	if TailleImageValid(txt_binair,l,h)==True:
		ajoutTxtImageRGB(img,l,h,txt_binair, path_sauv)

#utiliser retraitTxtImageRGB, ouvImage, tailleImage
def decoder_texte_dans_image(img_path):
	img=ouvImage(img_path)	
	l,h=tailleImage(img)
	retraitTxtImageRGB(img,l,h)

cacher_texte_dans_image('singe.png', 'bonjour', 'singe_text.png')
img = ouvImage('singe_text.png')
pixel = recupPixelEnArray(img)
print(pixel)
decoder_texte_dans_image("singe_text.png")
