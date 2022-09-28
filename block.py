class Block:

    def __init__(self, x, y, width, height):
        '''ブロック作成'''

        # 中心座標とサイズを設定
        self.x = x
        self.y = y
        self.w = width
        self.h = height

    def getCoords(self):
        '''左上の座標と右下の座標の取得'''

        return (self.x - self.w / 2, self.y - self.h / 2, self.x + self.w / 2, self.y + self.h / 2)

