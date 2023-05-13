
const LOCAL_HOST = "http://localhost:5005";
const PATH = location.pathname;
const DATA_LIST = JSON.parse(data_json)
const DATA_DICT = DATA_LIST[0]

// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
// フッターとヘッダーを設定
// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
$(function(){
  $('#js-Footer').load("http://localhost:5005/static/base/footer.html");
});


// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
// 大分類一覧
// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
if(document.URL.match(/large_list/)){
  $('#js-Header').load("http://localhost:5005/static/base/header.html", function(){
    $(document).ready(function() {

      for (index = 0; index < DATA_LIST.length; index++) {

        data = DATA_LIST[index];
        let large_category_id = data['large_category_id']
        let large_category_name = data['large_category_name']

        $('#js-Data-Wrapper-ListLargeCategory').append(
          '<form action="/small_list/get_list/' + large_category_id + '" method="get" id="tmp' + index + '">',
          '</form>'
        );
        $('#tmp' + index).append(
          '<input type="submit" class="a-Category" value=' + large_category_name +  '>',
        );
      }
    })
  })};


// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
// 小分類一覧
// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
if(document.URL.match(/small_list/)){
  $('#js-Header').load("http://localhost:5005/static/base/header.html", function(){
    $(document).ready(function() {

      let large_category_name = DATA_DICT['large_category_name'];
      $('.c-Link-Wrapper').append(
        '<a href="http://localhost:5005/large_list/get_list">ホーム</a>',
        ' > ' + large_category_name,
      );

      for (index = 0; index < DATA_LIST.length; index++) {

        data = DATA_LIST[index];
        let small_category_id = data['small_category_id']
        let small_category_name = data['small_category_name']

        $('#js-Data-Wrapper-ListSmallCategory').append(
          '<form action="/list_cards/get_list/' + small_category_id + '" method="get" id="tmp' + index + '">',
          '</form>'
        );
        $('#tmp' + index).append(
          '<input type="submit" class="a-Category" value=' + small_category_name +  '>',
        );
      }
    })
})};


// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
// 単語帳一覧
// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
if(document.URL.match(/list_cards/)){
  $('#js-Header').load("http://localhost:5005/static/base/header.html", function(){
    $(document).ready(function() {

      let large_category_id = DATA_DICT['large_category_id'];
      let large_category_name = DATA_DICT['large_category_name'];
      let small_category_id = DATA_DICT['small_category_id'];
      let small_category_name = DATA_DICT['small_category_name'];

      var note_element = document.querySelector('form[id="js-Note-Update"]')
      note_element.setAttribute('action','/put_card/update_note/' + small_category_id);

      $('.c-Link-Wrapper').append(
        '<a href="http://localhost:5005/large_list/get_list">ホーム</a>',
        ' > <a href="http://localhost:5005/small_list/get_list/' + large_category_id + '">' + large_category_name + '</a>',
        ' > ' + small_category_name,
      );

      for (index = 0; index < DATA_LIST.length; index++) {

        data = DATA_LIST[index];
        let card_id = data['card_id']
        let card_name = data['card_name']
        let is_separator = data['is_separator']

        if(is_separator == true){
          let note_content = data['note_content']

          $('#js-Data-Wrapper-ListCards').append(
            '<form action="/put_card/view/' + card_id + '" method="post" id="tmp' + index + '">',
          );
          $('#tmp' + index).append(
            '<input type="hidden" name="card_id" value="' + card_id +  '">',
            '<input type="submit" id="' + card_id + '" class="a-Separator" value="' + card_name + '" name="作成済のしおりです。">',          
          );
        }

        if(is_separator == false){
          let note_content = data['note_content']

          $('#js-Data-Wrapper-ListCards').append(
            '<form action="/put_card/view/' + card_id + '" method="post" id="tmp' + index + '">',
          );
          $('#tmp' + index).append(
            '<input type="hidden" name="card_id" value="' + card_id +  '">',
            '<input type="submit" id="' + card_id + '" class="a-Card" value="' + card_name + '" name="' + note_content + '">',
          );
        }
      }
      display_note();
    })
})};



// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
// ノート表示
// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
function display_note(){

  $('.a-Card').mouseover(function () {
    remove_note();

    var value = this.value;
    $('#js-Data-Wrapper-NoteTitle').append(
      '<p id="js-Note-title">' + value + '</p>'
    );

    var note_content = this.name;
    var card_id = this.id;
    $('#js-Data-Wrapper-Note').append(
      '<input type="hidden" id="js-Hidden-Card" name="card_id" value="' + card_id + '">',
      '<textarea id="js-Note-Content" name="note_content">' + note_content + '</textarea>',
    );

    $('#js-Data-Wrapper-Note-Btn').append(
      '<input type="submit" id="js-Button-Note" value="UPDATE"/>',
    );
  });
};

function remove_note(){
  $('#js-Note-title').remove();
  $('#js-Note-Content').remove();
  $('#js-Hidden-Card').remove();
  $('#js-Button-Note').remove();
}


// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
// 単語詳細表示
// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
if(document.URL.match(/put_card/)){
  $('#js-Header').load("http://localhost:5005/static/base/header.html", function(){
    $(document).ready(function() {

      $('.c-Link-Wrapper').append(
        '<a href="http://localhost:5005/large_list/get_list">ホーム</a>',
        ' > <a href="http://localhost:5005/small_list/get_list/' + DATA_DICT["large_category_id"] + '">' + DATA_DICT["large_category_name"] + '</a>',
        ' > <a href="http://localhost:5005/list_cards/get_list/' + DATA_DICT["small_category_id"] + '">' + DATA_DICT["small_category_name"] + '</a>',
      );

      // 入力フォーム初期値
      var card_id_element = document.querySelector('input[id="a-Hidden-Card"]')
      card_id_element.setAttribute('value',DATA_DICT["card_id"]);

      var sort_element = document.querySelector('input[id="a-Sort"]')
      sort_element.setAttribute('value',DATA_DICT["sort_number"]);

      var card_element = document.querySelector('input[id="a-Card"]')
      card_element.setAttribute('value',DATA_DICT["card_name"]);

      var large_element = document.querySelector('input[id="a-Large"]')
      large_element.setAttribute('value',DATA_DICT["large_category_name"]);

      var small_element = document.querySelector('input[id="a-Small"]')
      small_element.setAttribute('value',DATA_DICT["small_category_name"]);

      $('#a-Note').append(DATA_DICT["note_content"]);

      var tag_0_element = document.querySelector('input[id="a-Tag-0"]')
      tag_0_element.setAttribute('value',DATA_DICT["tag_name_0"] ? DATA_DICT["tag_name_0"] : "");

      var tag_1_element = document.querySelector('input[id="a-Tag-1"]')
      tag_1_element.setAttribute('value',DATA_DICT["tag_name_1"] ? DATA_DICT["tag_name_1"] : "");

      var tag_2_element = document.querySelector('input[id="a-Tag-2"]')
      tag_2_element.setAttribute('value',DATA_DICT["tag_name_2"] ? DATA_DICT["tag_name_2"] : "");

      var tag_3_element = document.querySelector('input[id="a-Tag-3"]')
      tag_3_element.setAttribute('value',DATA_DICT["tag_name_3"] ? DATA_DICT["tag_name_3"] : "");

      var tag_4_element = document.querySelector('input[id="a-Tag-4"]')
      tag_4_element.setAttribute('value',DATA_DICT["tag_name_4"] ? DATA_DICT["tag_name_4"] : "");

      // キャンセルボタン、削除ボタン
      var cancel_btn_element = document.querySelector('form[id="js-Cancel"]')
      cancel_btn_element.setAttribute('action','/list_cards/get_list/' + DATA_DICT["small_category_id"]);

      var delete_btn_element = document.querySelector('form[id="js-Delete"]')
      delete_btn_element.setAttribute('action','/put_card/delete/' + DATA_DICT["small_category_id"]);

      var delete_input_element = document.querySelector('input[id="a-Hidden-Card-Delete"]')
      delete_input_element.setAttribute('value',DATA_DICT["card_id"]);
  })
})};

// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
// 単語作成
// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
// NOTE: 作成画面は共通ヘッダーを使用しない
if(document.URL.match(/post_card/)){
    $(document).ready(function() {
      var LargeElement = document.querySelector('input[id="a-Large"]')
      LargeElement.setAttribute('value',DATA_DICT["large_category_name"] ? DATA_DICT["large_category_name"] : "");

      var SmallElement = document.querySelector('input[id="a-Small"]')
      SmallElement.setAttribute('value',DATA_DICT["small_category_name"] ? DATA_DICT["small_category_name"] : "");
    })
};

// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
//　プルダウン作成
// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
if(document.URL.match(/put_card/) || document.URL.match(/post_card/)){
  $(document).ready(function() {

    var large_url = "/get_any/large"
    var large_promise = fetch(LOCAL_HOST + large_url);
    large_promise.then((response) => {
      return response.json();
    })
    .then((data) => {
      var large_list = data["record_list"]

      for (index = 0; index < large_list.length; index++) {

        data = large_list[index];
        let large_category_name = data['large_category_name']

        $('#l-Large').append(
          '<option value="' + large_category_name + '">'
        );
      };
    })
  })};


  if(document.URL.match(/put_card/) || document.URL.match(/post_card/)){
    $(document).ready(function() {
  
      var small_url = "/get_any/small"
      var small_promise = fetch(LOCAL_HOST + small_url);
      small_promise.then((response) => {
        return response.json();
      })
      .then((data) => {
        var small_list = data["record_list"]
  
        for (index = 0; index < small_list.length; index++) {
  
          data = small_list[index];
          let small_category_name = data['small_category_name']
  
          $('#l-Small').append(
            '<option value="' + small_category_name + '">'
          );
        };
      })
    })};