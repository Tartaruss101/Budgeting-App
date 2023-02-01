from datetime import datetime

class Receipt:
    def __init__(self,
                transaction_date: datetime,
                transaction_total: float,
                establishment: str,
                items: dict or str ="unitemized"):

        self.transaction_date = transaction_date
        self.transaction_total = transaction_total
        self.items = items
        self.establishment = establishment