from zerodb.models import Model, Field


class Trade(Model):
    timestamp = Field()
    last = Field()
    # volume is not indexed

    def __str__(self):
        return "[{0}] 1 BTC = {1} USD, volume = {2} BTC".format(str(self.timestamp), self.last, self.volume)

    def __repr__(self):
        return self.__str__()
