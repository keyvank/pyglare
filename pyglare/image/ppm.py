import io

def save(name,frame):
	with io.open(name,mode='wb') as f:
		f.write(b'P6 ')
		f.write(str(frame.width).encode('ascii'))
		f.write(b' ')
		f.write(str(frame.height).encode('ascii'))
		f.write(b' 255\n')
		for row in reversed(frame.data):
			for color in row:
				f.write(color.get_bytes())

def read(name):
	raise NotImplementedError
