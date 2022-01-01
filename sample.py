# coding: utf-8
import numpy as np

# 参照だけならメソッド定義内でも常にグローバルスコープ
# 書き込みする場合はメソッド定義内でglobal宣言が必要
brow, bcol = 10, 6



# すべてのピース形状をPieceオブジェクトの配列に保存する
class Piece:
    def __init__(self, s, h,m,n):
        a = np.array(map(int, s)).reshape(h, -1)
        self.used = False
        self.form = []
        for i in range(m):
            for j in range(n):
                self.form.append((a, a.argmax()))
                a = np.rot90(a)
            a = np.fliplr(a)

pp = [Piece('010111010', 3,1,1),
      Piece('111101',    2,1,4),
      Piece('110011001', 3,1,4),
      Piece('110011010', 3,1,2),
      Piece('110010011', 3,2,2),
      Piece('111110',    2,2,4),
      Piece('11100011',  2,2,4),
      Piece('11110100',  2,2,4),
      Piece('111010010', 3,1,4),
      Piece('11111000',  2,2,4),
      Piece('111100100', 3,1,4),
      Piece('11111',     1,1,2)]

for i, piece in enumerate(pp):
    piece.loc_form = []
    for form in piece.form:
        a = []
        for r, row in enumerate(form[0]):
            for c, col in enumerate(row):
                if col: a.append(r * (bcol + 1) + c - form[1])
        piece.loc_form.append(a)



# boardの初期化
board = np.zeros((brow + 1) * (bcol + 1))
for i, b in enumerate(board):
    if ((i + 1) % (bcol + 1)) == 0 or i >= ((bcol + 1) * brow): board[i] = 100



# パズルの解を求める
def try_piece(board, pp, lvl):
    global counter, try_counter
    try_counter += 1
    x = board.argmin()
    for i, piece in enumerate(pp):
        if not piece.used:
            for blocks in piece.loc_form:
                if board[x + blocks[0]] or board[x + blocks[1]] or board[x + blocks[2]] or board[x + blocks[3]] or board[x + blocks[4]]: continue
                # ピースを置く
                for b in blocks: board[x + b] = i + 1
                piece.used = True
                # すべてのピースを置ききったらTrueを返す（recursiveコールの終了）
                if lvl == 11:
                    counter += 1
                    print('No', counter)
                    print(np.rot90(board.reshape((brow + 1, -1))[0:brow, 0:bcol]))
                    # ピースを戻す
                    for b in blocks: board[x + b] = 0
                    piece.used = False
                    return True
                # 次のピースを試す
                try_piece(board, pp, lvl + 1)
                # ピースを戻す
                for b in blocks: board[x + b] = 0
                piece.used = False
    return False

counter = 0
try_counter = 0
try_piece(board, pp, 0)
print ('解合計', counter)
print ('操作数', try_counter)