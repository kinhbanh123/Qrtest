import qrcode
img = qrcode.make("https://www.youtube.com/watch?v=N029UUlH1Dc&ab_channel=SuiseiChannel")
img.save("first.png")
