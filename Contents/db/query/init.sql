
use cardsdb;

CREATE TABLE Cards01 (
   is_deleted       bit(1)       NOT NULL DEFAULT 0                                          COMMENT '{"name":"削除フラグ","note":""}'
 , card_id      varchar(32)   NOT NULL                                                    COMMENT '{"name":"単語ID","note":""}'
 , card_name    varchar(256)  NOT NULL                                                    COMMENT '{"name":"単語名","note":""}'
 , large_category_id          varchar(32)   NOT NULL                                          COMMENT '{"name":"大分類ID","note":"OS識別用(1:iOS、2:Android、etc)"}'
 , small_category_id    varchar(32)  NOT NULL                                                    COMMENT '{"name":"小分類ID","note":""}'
 , primal_note_id    varchar(32)  DEFAULT NULL                                                    COMMENT '{"name":"優先ノートID","note":"優先表示するノートのノートID"}'
 , sort_number      varchar(3)   DEFAULT NULL                                                    COMMENT '{"name":"カード番号","note":"検索時には大分類・小分類番号を頭につけてソート番号とする。"}'
 , associate_id_joined      varchar(200)   DEFAULT NULL                                                    COMMENT '{"name":"関連カードID一覧","note":"関連する単語の単語IDを文字列型にして、_で繋ぐ"}'
 , significance      varchar(1)   NOT NULL DEFAULT '3'                                                   COMMENT '{"name":"重要度","note":"星1〜星5で評価"}'
 , study_state      varchar(1)   NOT NULL DEFAULT '1'                                                  COMMENT '{"name":"学習状況","note":"0:学習済み、1:得意、2学習中、3:苦手"}'
 , registered_at    timestamp(3) NOT NULL DEFAULT '1971-01-01 00:00:00.000'                  COMMENT '{"name":"登録日時","note":""}'
 , updated_at       timestamp(3) NOT NULL DEFAULT '1971-01-01 00:00:00.000'                  COMMENT '{"name":"更新日時","note":""}'
 , user_id       varchar(32)  DEFAULT NULL                                                    COMMENT '{"name":"更新処理","note":""}'
 , PRIMARY KEY (card_id)
) COMMENT='{"name":"単語帳カードマスタ","note":"単語帳カードを管理する"}';

CREATE TABLE Notes01 (
   is_deleted       bit(1)       NOT NULL DEFAULT 0                                          COMMENT '{"name":"削除フラグ","note":""}'
 , note_id      varchar(32)   NOT NULL                                                    COMMENT '{"name":"端末ID","note":""}'
 , card_id          varchar(32)   NOT NULL                                          COMMENT '{"name":"OSタイプ","note":"OS識別用(1:iOS、2:Android、etc)"}'
 , note_content    varchar(256)  NOT NULL                                                    COMMENT '{"name":"端末名称","note":""}'
 , sort_number     varchar(3)   DEFAULT NULL                                                    COMMENT '{"name":"端末ID","note":""}'
 , registered_at    timestamp(3) NOT NULL DEFAULT '1971-01-01 00:00:00.000'                  COMMENT '{"name":"登録日時","note":""}'
 , updated_at       timestamp(3) NOT NULL DEFAULT '1971-01-01 00:00:00.000'                  COMMENT '{"name":"更新日時","note":""}'
 , user_id       varchar(32)  DEFAULT NULL                                                    COMMENT '{"name":"更新処理","note":""}'
 , PRIMARY KEY (note_id)
) COMMENT='{"name":"ノートマスタ","note":"単語帳のノートを管理する"}';

CREATE TABLE Tags01 (
   is_deleted       bit(1)       NOT NULL DEFAULT 0                                          COMMENT '{"name":"削除フラグ","note":""}'
 , tag_id      varchar(32)   NOT NULL                                                    COMMENT '{"name":"端末ID","note":""}'
 , card_id          varchar(32)   NOT NULL                                          COMMENT '{"name":"OSタイプ","note":"OS識別用(1:iOS、2:Android、etc)"}'
 , tag_name    varchar(256)  NOT NULL                                                    COMMENT '{"name":"端末名称","note":""}'
 , sort_number     varchar(3)   DEFAULT NULL                                                    COMMENT '{"name":"端末ID","note":""}'
 , registered_at    timestamp(3) NOT NULL DEFAULT '1971-01-01 00:00:00.000'                  COMMENT '{"name":"登録日時","note":""}'
 , updated_at       timestamp(3) NOT NULL DEFAULT '1971-01-01 00:00:00.000'                  COMMENT '{"name":"更新日時","note":""}'
 , user_id       varchar(32)  DEFAULT NULL                                                    COMMENT '{"name":"更新処理","note":""}'
 , PRIMARY KEY (tag_id)
) COMMENT='{"name":"タグマスタ","note":"単語帳のタグを管理する"}';

CREATE TABLE LargeCategory01 (
   is_deleted       bit(1)       NOT NULL DEFAULT 0                                          COMMENT '{"name":"削除フラグ","note":""}'
 , large_category_id      varchar(32)   NOT NULL                                                    COMMENT '{"name":"端末ID","note":""}'
 , large_category_name    varchar(256)  NOT NULL                                                    COMMENT '{"name":"端末名称","note":""}'
 , sort_number     varchar(3)   DEFAULT NULL                                                    COMMENT '{"name":"端末ID","note":""}'
 , registered_at    timestamp(3) NOT NULL DEFAULT '1971-01-01 00:00:00.000'                  COMMENT '{"name":"登録日時","note":""}'
 , updated_at       timestamp(3) NOT NULL DEFAULT '1971-01-01 00:00:00.000'                  COMMENT '{"name":"更新日時","note":""}'
 , user_id       varchar(32)  DEFAULT NULL                                                    COMMENT '{"name":"更新処理","note":""}'
 , PRIMARY KEY (large_category_id)
) COMMENT='{"name":"大分類マスタ","note":"大分類を管理する"}';

CREATE TABLE SmallCategory01 (
   is_deleted       bit(1)       NOT NULL DEFAULT 0                                          COMMENT '{"name":"削除フラグ","note":""}'
 , small_category_id      varchar(32)   NOT NULL                                                    COMMENT '{"name":"端末ID","note":""}'
 , small_category_name    varchar(256)  NOT NULL                                                    COMMENT '{"name":"端末名称","note":""}'
 , large_category_id      varchar(32)   NOT NULL                                                    COMMENT '{"name":"端末ID","note":""}'
 , sort_number     varchar(3)   DEFAULT NULL                                                    COMMENT '{"name":"端末ID","note":""}'
 , registered_at    timestamp(3) NOT NULL DEFAULT '1971-01-01 00:00:00.000'                  COMMENT '{"name":"登録日時","note":""}'
 , updated_at       timestamp(3) NOT NULL DEFAULT '1971-01-01 00:00:00.000'                  COMMENT '{"name":"更新日時","note":""}'
 , user_id       varchar(32)  DEFAULT NULL                                                    COMMENT '{"name":"更新処理","note":""}'
 , PRIMARY KEY (small_category_id)
) COMMENT='{"name":"タグマスタ","note":"小分類を管理する"}';

CREATE TABLE User01 (
   is_deleted       bit(1)       NOT NULL DEFAULT 0                                          COMMENT '{"name":"削除フラグ","note":""}'
 , is_authorized       bit(1)       NOT NULL DEFAULT 0                                          COMMENT '{"name":"権利者フラグ","note":""}'
 , user_id      varchar(32)   NOT NULL                                                    COMMENT '{"name":"端末ID","note":""}'
 , user_name    varchar(256)  NOT NULL                                                    COMMENT '{"name":"端末名称","note":""}'
 , sort_number     varchar(3)   DEFAULT NULL                                                    COMMENT '{"name":"端末ID","note":""}'
 , registered_at    timestamp(3) NOT NULL DEFAULT '1971-01-01 00:00:00.000'                  COMMENT '{"name":"登録日時","note":""}'
 , updated_at       timestamp(3) NOT NULL DEFAULT '1971-01-01 00:00:00.000'                  COMMENT '{"name":"更新日時","note":""}'
 , PRIMARY KEY (user_id)
) COMMENT='{"name":"タグマスタ","note":"小分類を管理する"}';

