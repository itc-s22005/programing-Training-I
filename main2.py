from tkinter import *


from ball import Ball
from paddle import Paddle
from block import Block

class Game:
    """ ゲームのメインクラス
    このクラスで、ゲーム全体のコントロールをします。
    処理の流れとして、全体像が把握できるように作る。
    """

    def __init__(self):
        """ 基本的な初期化をします。
        Tk オブジェクトの生成や初期設定をします。
        ゲームに必要なオブジェクトの準備をします。
        """

        # tkinter を使用するときの基本部分
        self.tk = Tk()
        self.tk.title("Game")                       # Tk本体(GUIのウィンドウ)
        self.tk.resizable(False, False)             # ウィンドウのサイズ変更を許可するかどうか。横・縦
        self.tk.wm_attributes("-topmost", True)     # ウィンドウを常に前面に。

        # 図形描画に使う Canvas 
        self.canvas = Canvas(self.tk, width=500, height=400, bd=False, highlightthickness=False)
        self.canvas.pack()      # canvas をメインウィンドウ(tk)に組み込んで表示
        self.tk.update()        # tk の状態を更新

        # ゲームの準備
        self.paddle = Paddle(self.canvas, "blue")
        self.ball = Ball(self.canvas, "red", self.paddle)

        # イベントハンドラ設定(キー入力の反映)
        self.canvas.bind_all("<KeyPress-Left>", self.paddle.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.paddle.turn_right)
        self.canvas.bind_all("<KeyPress-space>", self.ball.start)

        NUM_H_BLOCK = 10  # ブロッックの数（横方向)
        NUM_V_BLOCK = 10  # ブロックの数（縦方向）
        WIDTH_BLOCK = 40  # ブロックの幅
        HEIGHT_BLOCK = 20  # ブロックの高さ
        COLOR_BLOCK = "blue"  # ブロックの色

        HEIGHT_SPACE = 300  # 縦方向の空きスペース

    def main(self):
        """ ゲームを動かすための関数
        必ず初期化後に呼び出す。
        """
        self.update()       # 更新処理の関数
        self.tk.mainloop()  # Tk 使うときに、プログラムが一瞬で終了しないようにする。

    def update(self):
        # ボールの更新処理
        self.ball.draw()
        # パドルの更新処理
        self.paddle.draw()

        # 次回 update の呼び出し予約
        self.canvas.after(1000 // 60, self.update)


game = Game()
game.main()
                                                                                         66,1          Bot

                                                                              
