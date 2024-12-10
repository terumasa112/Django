#Pillowライブラリを使う

#Image
#ImageFilter
from PIL import Image, ImageFilter

#画像ファイルを開いて作業を開始する
im = Image.open("")

#画像データを印刷する
#    画像ファイルのフォーマット、大きさ、色空間
print(im.format, im.size, im.mode)
#楕円を書く
draw = ImageDraw.Draw(im)
draw.ellipse((0, 0, im.width, im.height), outline=(0, 0, 0))
# モノクロ変換
#  .convert('L')
#サイズ変換
#  .resize((im.width//4,im.height//4))
#  元の1/4に縮小　「//4」　整数値となるように切り捨てる
gray = im.convert('L').resize((im.width//4,im.height//4))
print(gray.format, gray.size, gray.mode)

# gray.show()
# 編集した画像を指定した形式で保存する
gray.show()
gray.save('gray.png', 'png')