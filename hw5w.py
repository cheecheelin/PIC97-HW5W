import sys
from PyQt4 import QtGui,QtCore

class HW5W(QtGui.QWidget,QtCore.QTimer):
	def __init__(self):
		super(HW5W, self).__init__()
		self.initUI()
		self.ball_x=5
		self.ball_y=5
		self.ball_velx=5
		self.ball_vely=5

	def initUI(self):
		self.setGeometry(300,300,600,400)
		self.setWindowTitle('HW5W')
		self.show()

	def paintEvent(self,qp):
		qp=QtGui.QPainter()
		qp.begin(self)
		self.drawRectangles(qp)
		qp.end()

	def drawRectangles(self,qp):
		qp.setBrush(QtGui.QColor(255,255,255))
		qp.drawRect(0,0,self.width(),self.height())
		qp.setBrush(QtGui.QColor(255,0,0))
		qp.drawEllipse(self.ball_x,self.ball_y,30,30)

	def animate(self):
		try:
			self.checkCollision()
			self.ball_x+=self.ball_velx
			self.ball_y+=self.ball_vely
			self.update()
		finally:
			QtCore.QTimer.singleShot(1,self.animate)

	def checkCollision(self):
		if self.ball_x==0 or self.ball_x>=self.width()-30:
			self.ball_velx=-(self.ball_velx)
		elif self.ball_y==0 or self.ball_y>=self.height()-30:
			self.ball_vely=-(self.ball_vely)
		


def main():
    
    app = QtGui.QApplication(sys.argv)
    ex=HW5W()
    ex.animate()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()