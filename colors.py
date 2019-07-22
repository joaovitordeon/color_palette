
# coding: utf-8


import matplotlib.pyplot as plt
import matplotlib


class Palette:

	def __init__(self, num = 10 , alpha = 0.75 , palette_name='rainbow'):
		self.num = num
		self.alpha = alpha
		self.palette_name = palette_name
		self.colors = None


		try:
			cmap = getattr(matplotlib.cm, self.palette_name) # equivalent to 'cmap = matplotlib.cm.palette'
		
		except:
			print('Rode o programa novamente com um nome de pallete válido ... \n')

		else:
			norm = matplotlib.colors.Normalize(vmin=0, vmax=self.num)

			self.colors = [cmap(norm(value), alpha = self.alpha) for value in range(0,self.num)]

	
	def get_colors(self):
		if self.colors != None:
			# print('\n --------------------------------------------------Codigos RGBA------------------------------------------------- \n')
			# for c in self.colors:
			# 	print(c)

			return self.colors
		else:
			print("Você deve setar o array de cores antes de ter acesso a ele ... \n")


	def graph(self):
		if self.colors != None:
			fig, ax = plt.subplots(figsize=(14,7));
			plt.imshow([self.colors]);

			ax.spines['right'].set_visible(False)
			ax.spines['top'].set_visible(False)
			ax.spines['left'].set_visible(False)
			ax.spines['bottom'].set_visible(False)

			plt.tight_layout()
			plt.title("Palette: {}".format(self.palette_name) , fontsize=12, weight='bold')
			plt.yticks([])
			plt.xticks(range(0,self.num), self.colors , rotation='vertical' , fontsize=12, weight='bold')
			plt.show()

		else:
			print("Você deve setar o array de cores antes de plotar ... \n")


# -------------------------------------------------------------------------------------------------------


print("\nSEE ALL PALETTES ===> https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html \n")


def program():
	#parametros ------------------------------------------
	#(ex palettes: hsv,winter,rainbow ,plasma, inferno, flag, cool, PiYG, etc...)

	try:
		palette_name=str(input('DIGITE O NOME DA PALETTE (case sensitive): \n'))
	except:
		palette_name = None

	try:
		num=int(input('DIGITE QUANTAS CORES DESEJA OBTER: \n'))
	except:
		num=None

	try:
		alpha=float(input('DIGITE O ALPHA (de 0 a 1): \n'))
	except:
		alpha=None

	#------------------------------------------------------
	if palette_name != None and num != None and alpha != None:
		# instanciar objeto
		palette = Palette(num, alpha, palette_name)

		# setar as cores
		palette.set_colors()

		# plotar grafico
		palette.graph()

		# obter os codigos das cores
		palette.get_colors()

		# deletar objeto
		del palette

	else: 
		print('Instanciando palette padrão ... \n')
		# instanciar objeto
		palette = Palette()

		# setar as cores
		palette.set_colors()

		# plotar grafico
		palette.graph()

		# obter os codigos das cores
		palette.get_colors()

		# deletar objeto
		del pallete

#program()