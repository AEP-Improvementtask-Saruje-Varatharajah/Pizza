from datetime import datetime
from model.voucher import Voucher
from data_access.voucher_data_access import VoucherDataAccess

class VoucherManager:
    def __init__(self):
        self.__voucher_da = VoucherDataAccess()

    def create_voucher(self, code: str, discount_percent: float, 
                      valid_until: datetime, activ: bool) -> Voucher:
        return self.__voucher_da.create_new_voucher(code, discount_percent, valid_until, activ)

    def read_voucher(self, voucher_id: int) -> Voucher:
        return self.__voucher_da.read_voucher_by_id(voucher_id)

    def read_voucher_by_code(self, code: str) -> Voucher:
        return self.__voucher_da.read_voucher_by_code(code)

    def read_all_vouchers(self) -> list[Voucher]:
        return self.__voucher_da.read_all_vouchers()

    def read_active_vouchers(self) -> list[Voucher]:
        return self.__voucher_da.read_active_vouchers()

    def read_valid_vouchers(self) -> list[Voucher]:
        return self.__voucher_da.read_valid_vouchers()

    def update_voucher(self, voucher: Voucher) -> None:
        self.__voucher_da.update_voucher(voucher)

    def delete_voucher(self, voucher: Voucher) -> None:
        self.__voucher_da.delete_voucher(voucher)