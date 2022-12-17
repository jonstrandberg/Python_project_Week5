class Album:

    def __init__(self, title, artist, genre, record_label, stock, buy_price, sell_price, id=None):
        
        self.title = title
        self.artist = artist
        self.genre = genre
        self.record_label = record_label
        self.stock = stock
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.id = id