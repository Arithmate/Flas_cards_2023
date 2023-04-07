from lib.db_util import DataBase

def reset_sort_number(
    db: DataBase,
    small_category_id,
):
    """
    0を始点に、昇順でソート番号を割り振る。
    WHERE句にソート番号を使わないため、ソート番号の重複・欠番を解消できる。
    """
    count_sql = f"""
        SELECT
            card_id
        FROM
            Cards01
        WHERE
            is_deleted = False
            AND small_category_id = '{small_category_id}'
        ORDER BY
            sort_number
            ,registered_at;
    """
    card_id_list = db.select(count_sql)

    for index, card_id_dict in enumerate(card_id_list):
        card_id_tmp = card_id_dict["card_id"]
        sort_updata_sql = f"""
            UPDATE
                Cards01
            SET
                sort_number = {index}
            WHERE
                card_id = '{card_id_tmp}'
                AND small_category_id = '{small_category_id}';
        """
        db.insert(sort_updata_sql)

    return None