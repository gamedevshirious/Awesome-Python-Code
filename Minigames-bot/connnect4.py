#connect4
class board :
	def __init__(self) :
		self.brrd = [ '|| 1 | 2 | 3 | 4 | 5 | 6 | 7 ||\n',
'|| :heavy_minus_sign: | :heavy_minus_sign: | :heavy_minus_sign: | :heavy_minus_sign: | :heavy_minus_sign: | :heavy_minus_sign: | :heavy_minus_sign: ||\n',
'|| :black_circle: | :black_circle: | :black_circle: | :black_circle: | :black_circle: | :black_circle: | :black_circle: ||\n',
'|| :black_circle: | :black_circle: | :black_circle: | :black_circle: | :black_circle: | :black_circle: | :black_circle: ||\n',
'|| :black_circle: | :black_circle: | :black_circle: | :black_circle: | :black_circle: | :black_circle: | :black_circle: ||\n',
'|| :black_circle: | :black_circle: | :black_circle: | :black_circle: | :black_circle: | :black_circle: | :black_circle: ||\n',
'|| :black_circle: | :black_circle: | :black_circle: | :black_circle: | :black_circle: | :black_circle: | :black_circle: ||\n',
'|| :black_circle: | :black_circle: | :black_circle: | :black_circle: | :black_circle: | :black_circle: | :black_circle: ||\n',
]
		self.brrd2 = [ '|| 1 | 2 | 3 | 4 | 5 | 6 | 7 ||\n',
'|| - | - | - | - | - | - | - ||\n',
'|| 0 | 0 | 0 | 0 | 0 | 0 | 0 ||\n',
'|| 0 | 0 | 0 | 0 | 0 | 0 | 0 ||\n',
'|| 0 | 0 | 0 | 0 | 0 | 0 | 0 ||\n',
'|| 0 | 0 | 0 | 0 | 0 | 0 | 0 ||\n',
'|| 0 | 0 | 0 | 0 | 0 | 0 | 0 ||\n',
'|| 0 | 0 | 0 | 0 | 0 | 0 | 0 ||\n',
]
b = board()
#print(''.join(b.brrd2))
#'============================\n',