
use cardsdb;

CREATE TABLE Cards01 (
   is_deleted       bit(1)       NOT NULL DEFAULT 0                                          COMMENT '{"name":"削除フラグ","note":""}'
 , card_id      binary(16)   NOT NULL                                                    COMMENT '{"name":"端末ID","note":""}'
 , large_category_id          binary(16)   NOT NULL                                          COMMENT '{"name":"OSタイプ","note":"OS識別用(1:iOS、2:Android、etc)"}'
 , small_category_id    binary(16)  NOT NULL                                                    COMMENT '{"name":"端末名称","note":""}'
 , card_sort_number      varchar(5)   NOT NULL                                                    COMMENT '{"name":"カード番号","note":"検索時には大分類・小分類番号を頭につけてソート番号とする。"}'
 , targeting_association_id      binary(16)   NOT NULL                                                    COMMENT '{"name":"関連カード用ID","note":"関連カード設定用のID"}'
 , significance      varchar(1)   NOT NULL                                                    COMMENT '{"name":"端末ID","note":""}'
 , study_state      varchar(1)   NOT NULL                                                    COMMENT '{"name":"端末ID","note":""}'
 , registered_at    timestamp(3) NOT NULL DEFAULT '1971-01-01 00:00:00.000'                  COMMENT '{"name":"登録日時","note":""}'
 , updated_at       timestamp(3) NOT NULL DEFAULT '1971-01-01 00:00:00.000'                  COMMENT '{"name":"更新日時","note":""}'
 , user_id       binary(16)  DEFAULT NULL                                                    COMMENT '{"name":"更新処理","note":""}'
 , PRIMARY KEY (card_id)
) COMMENT='{"name":"単語帳カードマスタ","note":"単語帳カードを管理する"}';

CREATE TABLE Notes01 (
   is_deleted       bit(1)       NOT NULL DEFAULT 0                                          COMMENT '{"name":"削除フラグ","note":""}'
 , note_id      binary(16)   NOT NULL                                                    COMMENT '{"name":"端末ID","note":""}'
 , card_id          binary(16)   NOT NULL                                          COMMENT '{"name":"OSタイプ","note":"OS識別用(1:iOS、2:Android、etc)"}'
 , note_content    varchar(256)  NOT NULL                                                    COMMENT '{"name":"端末名称","note":""}'
 , sort_number     varchar(1)   NOT NULL                                                    COMMENT '{"name":"端末ID","note":""}'
 , registered_at    timestamp(3) NOT NULL DEFAULT '1971-01-01 00:00:00.000'                  COMMENT '{"name":"登録日時","note":""}'
 , updated_at       timestamp(3) NOT NULL DEFAULT '1971-01-01 00:00:00.000'                  COMMENT '{"name":"更新日時","note":""}'
 , user_id       binary(16)  DEFAULT NULL                                                    COMMENT '{"name":"更新処理","note":""}'
 , PRIMARY KEY (note_id)
) COMMENT='{"name":"ノートマスタ","note":"単語帳のノートを管理する"}';

CREATE TABLE Tags01 (
   is_deleted       bit(1)       NOT NULL DEFAULT 0                                          COMMENT '{"name":"削除フラグ","note":""}'
 , tag_id      binary(16)   NOT NULL                                                    COMMENT '{"name":"端末ID","note":""}'
 , card_id          binary(16)   NOT NULL                                          COMMENT '{"name":"OSタイプ","note":"OS識別用(1:iOS、2:Android、etc)"}'
 , tag_name    varchar(256)  NOT NULL                                                    COMMENT '{"name":"端末名称","note":""}'
 , sort_number     varchar(1)   NOT NULL                                                    COMMENT '{"name":"端末ID","note":""}'
 , registered_at    timestamp(3) NOT NULL DEFAULT '1971-01-01 00:00:00.000'                  COMMENT '{"name":"登録日時","note":""}'
 , updated_at       timestamp(3) NOT NULL DEFAULT '1971-01-01 00:00:00.000'                  COMMENT '{"name":"更新日時","note":""}'
 , user_id       binary(16)  DEFAULT NULL                                                    COMMENT '{"name":"更新処理","note":""}'
 , PRIMARY KEY (tag_id)
) COMMENT='{"name":"タグマスタ","note":"単語帳のタグを管理する"}';

CREATE TABLE LargeCategory01 (
   is_deleted       bit(1)       NOT NULL DEFAULT 0                                          COMMENT '{"name":"削除フラグ","note":""}'
 , large_category_id      binary(16)   NOT NULL                                                    COMMENT '{"name":"端末ID","note":""}'
 , large_category_name    varchar(256)  NOT NULL                                                    COMMENT '{"name":"端末名称","note":""}'
 , sort_number     varchar(1)   NOT NULL                                                    COMMENT '{"name":"端末ID","note":""}'
 , registered_at    timestamp(3) NOT NULL DEFAULT '1971-01-01 00:00:00.000'                  COMMENT '{"name":"登録日時","note":""}'
 , updated_at       timestamp(3) NOT NULL DEFAULT '1971-01-01 00:00:00.000'                  COMMENT '{"name":"更新日時","note":""}'
 , user_id       binary(16)  DEFAULT NULL                                                    COMMENT '{"name":"更新処理","note":""}'
 , PRIMARY KEY (large_category_id)
) COMMENT='{"name":"大分類マスタ","note":"大分類を管理する"}';

CREATE TABLE SmallCategory01 (
   is_deleted       bit(1)       NOT NULL DEFAULT 0                                          COMMENT '{"name":"削除フラグ","note":""}'
 , small_category_id      binary(16)   NOT NULL                                                    COMMENT '{"name":"端末ID","note":""}'
 , small_category_name    varchar(256)  NOT NULL                                                    COMMENT '{"name":"端末名称","note":""}'
 , sort_number     varchar(1)   NOT NULL                                                    COMMENT '{"name":"端末ID","note":""}'
 , registered_at    timestamp(3) NOT NULL DEFAULT '1971-01-01 00:00:00.000'                  COMMENT '{"name":"登録日時","note":""}'
 , updated_at       timestamp(3) NOT NULL DEFAULT '1971-01-01 00:00:00.000'                  COMMENT '{"name":"更新日時","note":""}'
 , user_id       binary(16)  DEFAULT NULL                                                    COMMENT '{"name":"更新処理","note":""}'
 , PRIMARY KEY (small_category_id)
) COMMENT='{"name":"タグマスタ","note":"小分類を管理する"}';

CREATE TABLE User01 (
   is_deleted       bit(1)       NOT NULL DEFAULT 0                                          COMMENT '{"name":"削除フラグ","note":""}'
 , is_authorized       bit(1)       NOT NULL DEFAULT 0                                          COMMENT '{"name":"権利者フラグ","note":""}'
 , user_id      binary(16)   NOT NULL                                                    COMMENT '{"name":"端末ID","note":""}'
 , user_name    varchar(256)  NOT NULL                                                    COMMENT '{"name":"端末名称","note":""}'
 , sort_number     varchar(1)   NOT NULL                                                    COMMENT '{"name":"端末ID","note":""}'
 , registered_at    timestamp(3) NOT NULL DEFAULT '1971-01-01 00:00:00.000'                  COMMENT '{"name":"登録日時","note":""}'
 , updated_at       timestamp(3) NOT NULL DEFAULT '1971-01-01 00:00:00.000'                  COMMENT '{"name":"更新日時","note":""}'
 , PRIMARY KEY (user_id)
) COMMENT='{"name":"タグマスタ","note":"小分類を管理する"}';

