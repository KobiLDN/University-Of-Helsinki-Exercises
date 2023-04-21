# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents

    def __str__(self):
        return f"{self._euros}.{self._cents:02} eur"

    def __eq__(self, another):
        return self._euros == another._euros and self._cents == another._cents

    def __lt__(self, another):
        return self._euros + self._cents < another._euros + another._cents

    def __gt__(self, another):
        return self._euros + self._cents > another._euros + another._cents

    def __ne__(self, another):
        return self._euros + self._cents != another._euros + another._cents

    def __add__(self, another):
        cents = self._cents + another._cents
        euros = self._euros + another._euros
        if cents >= 100:
            cents = cents/100
            x = euros+cents
            return f"{x:.2f} eur"
        else:
            return f"{euros}.{cents:02} eur"

    def __sub__(self, another):
        euros = (self._euros * 100) + self._cents
        another = (another._euros * 100) + another._cents
        if (euros - another) < 0:
            raise ValueError("negative amount")
        else:
            euros = euros/100
            another = another/100
            x = euros -another
            return f"{x:.2f} eur"

