from __future__ import annotations
from datetime import datetime
from model.voucher import Voucher
from data_access.base_data_access import BaseDataAccess

class VoucherDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_voucher(self, code: str, discount_percent: float, 
                          valid_until: datetime, activ: bool) -> Voucher:
        if code is None:
            raise ValueError("Code is required")
        if discount_percent is None:
            raise ValueError("Discount percent is required")
        if valid_until is None:
            raise ValueError("Valid until date is required")
        if activ is None:
            raise ValueError("Active status is required")

        sql = """
        INSERT INTO Voucher (code, discount_percent, valid_until, activ) 
        VALUES (?, ?, ?, ?)
        """
        params = (code, discount_percent, valid_until, activ)
        last_row_id, row_count = self.execute(sql, params)
        return Voucher(last_row_id, code, discount_percent, valid_until, activ)

    def read_voucher_by_id(self, voucher_id: int) -> Voucher | None:
        if voucher_id is None:
            raise ValueError("Voucher ID is required")

        sql = """
        SELECT voucher_id, code, discount_percent, valid_until, activ 
        FROM Voucher WHERE voucher_id = ?
        """
        params = tuple([voucher_id])
        result = self.fetchone(sql, params)
        if result:
            voucher_id, code, discount_percent, valid_until, activ = result
            return Voucher(voucher_id, code, discount_percent, valid_until, bool(activ))
        else:
            return None

    def read_voucher_by_code(self, code: str) -> Voucher | None:
        if code is None:
            raise ValueError("Code is required")

        sql = """
        SELECT voucher_id, code, discount_percent, valid_until, activ 
        FROM Voucher WHERE code = ? LIMIT 1
        """
        params = tuple([code])
        result = self.fetchone(sql, params)
        if result:
            voucher_id, code, discount_percent, valid_until, activ = result
            return Voucher(voucher_id, code, discount_percent, valid_until, bool(activ))
        else:
            return None

    def read_all_vouchers(self) -> list[Voucher]:
        sql = """
        SELECT voucher_id, code, discount_percent, valid_until, activ 
        FROM Voucher ORDER BY code
        """
        vouchers = self.fetchall(sql)
        return [Voucher(voucher_id, code, discount_percent, valid_until, bool(activ))
            for voucher_id, code, discount_percent, valid_until, activ in vouchers]

    def read_active_vouchers(self) -> list[Voucher]:
        sql = """
        SELECT voucher_id, code, discount_percent, valid_until, activ 
        FROM Voucher WHERE activ = 1 ORDER BY code
        """
        vouchers = self.fetchall(sql)
        return [Voucher(voucher_id, code, discount_percent, valid_until, bool(activ))
            for voucher_id, code, discount_percent, valid_until, activ in vouchers]

    def read_valid_vouchers(self) -> list[Voucher]:
        sql = """
        SELECT voucher_id, code, discount_percent, valid_until, activ 
        FROM Voucher WHERE activ = 1 AND valid_until > datetime('now') ORDER BY code
        """
        vouchers = self.fetchall(sql)
        return [Voucher(voucher_id, code, discount_percent, valid_until, bool(activ))
            for voucher_id, code, discount_percent, valid_until, activ in vouchers]

    def update_voucher(self, voucher: Voucher) -> None:
        if voucher is None:
            raise ValueError("Voucher cannot be None")

        sql = """
        UPDATE Voucher SET code = ?, discount_percent = ?, valid_until = ?, activ = ? 
        WHERE voucher_id = ?
        """
        params = tuple([voucher.code, voucher.discount_percent, voucher.valid_until, 
                       voucher.activ, voucher.voucher_id])
        last_row_id, row_count = self.execute(sql, params)

    def delete_voucher(self, voucher: Voucher) -> None:
        if voucher is None:
            raise ValueError("Voucher cannot be None")

        sql = """
        DELETE FROM Voucher WHERE voucher_id = ?
        """
        params = tuple([voucher.voucher_id])
        last_row_id, row_count = self.execute(sql, params)