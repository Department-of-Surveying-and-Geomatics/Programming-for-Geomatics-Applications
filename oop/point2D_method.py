class Point2D():
    '''
    The initialization method to instantiate a Point2D instance
    '''
    def __init__(self, x, y):
        self.x = x 
        self.y = y 

    def translate(self, x_move, y_move):
        '''
        A method that translates the Point2D object by x_move in the 
        x_axis and y_move in the y_axis 
        '''
        self.x = self.x + x_move
        self.y = self.y + y_move