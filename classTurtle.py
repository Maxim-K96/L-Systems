# -*- encoding: utf-8 -*-

import turtle

class _Init_Turtle:
	def __init__(self, 
		root, 
		startPosition = (-300, -100), 
		color = 'black', 
		speed = 0, 
		widthline = 1, 
		show = True,): 

		self.startPosition = startPosition
		self.color = color
		self.speed = speed
		self.widthline = widthline
		self.show = show

		self.root = root
		if self.show == False:
			self.root.hideturtle()
		self.root.color(self.color)
		self.root.speed(self.speed)
		self.root.width(self.widthline)

		self.root.penup()
		self.root.setpos(self.startPosition)
		self.root.pendown()

class L_Sistem(_Init_Turtle):
	def __init__(self, root):
		_Init_Turtle.__init__(self, root)

	def _main_function(self, 
										axiom:str, 
										itr:int, 
										angl:int, 
										translate:tuple, 
										condition='F', 
										two_condition=None):
		import random
		axmTemp = ''
		dl = 7
		colors = ['red', 'blue', 'purple', 'green']

		for _ in range(itr):
			for ch in axiom:
				axmTemp += translate[ch]
			axiom = axmTemp
			#print(axiom)
			axmTemp = ''

		for ch in axiom:
			if ch == '+':
				self.root.left(angl)
			elif ch == '-':
				self.root.right(angl)
			elif ch == condition or two_condition:
				color = colors[random.randrange(0, 4)]
				self.root.color(color)
				self.root.forward(dl)

	def Koch_curve(self):
		axiom = 'F'
		itr = 4
		angl = 90
		translate = {'+':'+', '-':'-', 'F':'F+F-F-F+F'}
		self._main_function(axiom, itr, angl, translate)

	def Dracon_curve(self):
		self.root.penup()
		self.root.home()
		self.root.pendown()
		axiom = 'FX'
		itr = 10
		angl = 90
		translate={'+':'+', '-':'-', 'F':'F', 'X':'X+YF+', 'Y':'-FX-Y'}
		self._main_function(axiom, itr, angl, translate)

	def Sierpinski_swept_curve(self):
		axiom = 'F'
		itr = 8
		angl = 60
		translate = {'+':'+', '-':'-', 'F':'B-F-B', 'B':'F+B+F'}
		self._main_function(axiom, itr, angl, translate, two_condition='B')

	def Sierpinski_triangle(self):
		self.root.penup()
		self.root.goto(-200, 300)
		self.root.pendown()
		axiom = 'F-G-G'
		itr = 6
		angl = 120
		translate = {'+':'+', '-':'-', 'F':'F-G+F+G-F', 'G':'GG'}
		self._main_function(axiom, itr, angl, translate, two_condition='G')


def main():
	root = turtle.Turtle()
	fractal = L_Sistem(root)
	print(type(fractal.Dracon_curve()))
	l_systems = {
		'Koch curve': 'Koch_curve()',
		'Dracon curve': 'Dracon_curve()',
		'Sierpinski swept curve': 'Sierpinski_swept_curve()',
		'Sierpinski triangle': 'Sierpinski_triangle()'
	}

	system = l_systems['Dracon curve']
	print(type(system))
	#fractal.system

if __name__ == '__main__':
	window = turtle.Screen()
	window.setup(750, 750)
	main()
	window.update()
	window.mainloop()