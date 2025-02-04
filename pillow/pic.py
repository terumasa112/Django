#Pillowライブラリを使う

# Image  画像データを取り合う
# ImageFilter  画像に対してレタッチを行う（ぼかし、シャープネス、エッジ検出などの加工）
# ImageEnhance 画像に対してレタッチを行う（コントラスト、鮮やかさ、明るさなどの調整）
# ImageDraw 画像データを描画する
from PIL import Image, ImageFilter, ImageDraw, ImageEnhance

#画像ファイルを開いて作業を開始する
im = Image.open("twice.png")
# アルファチャンネルを削除する
im = im.convert('RGB')

#画像データを印刷する
#    画像ファイルのフォーマット、大きさ、色空間
print(im.format, im.size, im.mode)
#楕円を書く
draw = ImageDraw.Draw(im)
draw.ellipse((0, 0, im.width, im.height), outline=(0, 0, 0), width=20)
# 線を引く
# line((左上x, 左上y, 右下x, 右下y), fill=(R,G,B), width=線幅)
draw.line((0, 0, im.width, im.height), fill=(64, 64,64), width=8)
draw.polygon(((100, 100),(200, 200),(100, 200)),fill=(255, 0, 0), width=8)
# ImageFilterを使って画像をレタッチする
#     すべて大文字のフィルタはパラメータがない
#     クラスフィルターはパラメータで効果を調整できる
im_blur = im.filter(ImageFilter.GaussianBlur(radius=8))
im_blur = im_blur.filter(ImageFilter.RankFilter(size=13,rank=7))
#im_blur = im_blur.filter(ImageFilter.FIND_EDGES)

im_e = ImageEnhance.Brightness(im_blur)
#      1.0を基準とし数値が大きくなると明るく、小さくなると暗くなる
im_e = im_e.enhance(1.8)

# モノクロ変換
#  .convert('L')
#サイズ変換
#  .resize((im.width//4,im.height//4))
#  元の1/4に縮小　「//4」　整数値となるように切り捨てる
gray = im_blur.resize((im.width//4,im.height//4))
print(gray.format, gray.size, gray.mode)

# gray.show()
# 編集した画像を指定した形式で保存する
gray.show()
gray.save('gray.png', 'png')
# 拡張子をもとに形式を推測するので適切な拡張子が指定されていなければ形式は省略可能
