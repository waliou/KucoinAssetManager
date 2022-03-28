from curses.ascii import isdigit
from kucoin.client import Client
from kucoin.utils import flat_uuid

class MyClient(Client):
    def get_margin_accounts(self):
        return self._get("margin/account", True)
    def borrow(self, currency, size, max_rate="", term="", type="FOK"):
        data = {}
        data["currency"] = currency
        data["type"] = type
        data["size"] = float(size)
        if max_rate != "" and isdigit(max_rate):
            data["maxRate"] = float(max_rate)
        if term=="":
            data["term"] = term
        return self._post("margin/borrow", True, data=data)
    def repay_all(self, currency, size,sequence = "RECENTLY_EXPIRE_FIRST"):
        data = {
            "currency": currency,
            "size": size,
            "sequence": sequence
        }
        return self._post("margin/repay/all", True, data=data)
    def get_subusers(self):
        return self._get("sub/user", True)
    def get_subuser_balance(self, subuser_id):
        return self._get(f"sub-accounts/{subuser_id}", True)
    def transfer_subuser(self, currency, amount, direction, sub_user_id, main_type=None, sub_type=None):
        data = {
            'clientOid': flat_uuid(),
            'currency': currency,
            'amount': amount,
            'direction': direction,
            'subUserId': sub_user_id,
            'accountType': main_type.upper(),
            'subAccountType': sub_type.upper()}
        return self._post('accounts/sub-transfer', True, self.API_VERSION2, data=data)


        

