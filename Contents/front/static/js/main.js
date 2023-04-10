
const LOCAL_HOST = "http://localhost:5005";


// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
// 大分類一覧
// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
if(document.URL.match(/large_list/)){
  $(document).ready(function() {

    var data_list = JSON.parse(data_json)

    for (index = 0; index < data_list.length; index++) {

      data = data_list[index];
      let large_category_id = data['large_category_id']
      let large_category_name = data['large_category_name']

      $('#js-Data-Wrapper-ListLargeCategory').append(
        '<form action="/small_list/get_list/' + large_category_id + '" method="get" id="tmp' + index + '">',
        '</form>'
      );
      $('#tmp' + index).append(
        '<input type="hidden" name="large_category_id_str" value=' + large_category_id +  '>',
        '<input type="submit" class="List_Btn" value=' + large_category_name +  '>',
      );
    }
  })};


// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
// 小分類一覧
// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
if(document.URL.match(/small_list/)){
  $(document).ready(function() {

    var data_list = JSON.parse(data_json)

    let large_category_name = data_list[0]['large_category_name'];
    $('.c-Link-Wrapper').append(
      '<a href="http://localhost:5005/large_list/get_list">ホーム</a>',
      ' > ' + large_category_name,
    );

    for (index = 0; index < data_list.length; index++) {

      data = data_list[index];
      let small_category_id = data['small_category_id']
      let small_category_name = data['small_category_name']

      $('#js-Data-Wrapper-ListSmallCategory').append(
        '<form action="/list_cards/get_list/' + small_category_id + '" method="get" id="tmp' + index + '">',
        '</form>'
      );
      $('#tmp' + index).append(
        '<input type="hidden" name="small_category_id_str" value=' + small_category_id +  '>',
        '<input type="submit" class="List_Btn" value=' + small_category_name +  '>',
      );
    }
})};


// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
// 単語帳一覧
// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
if(document.URL.match(/list_cards/)){
  $(document).ready(function() {

    var data_list = JSON.parse(data_json)

    let large_category_id = data_list[0]['large_category_id'];
    let large_category_name = data_list[0]['large_category_name'];
    let small_category_id = data_list[0]['small_category_id'];
    let small_category_name = data_list[0]['small_category_name'];

    var note_element = document.querySelector('form[id="js-Note-Update"]')
    note_element.setAttribute('action','/put_card/update_note/' + small_category_id);

    $('.c-Link-Wrapper').append(
      '<a href="http://localhost:5005/large_list/get_list">ホーム</a>',
      ' > <a href="http://localhost:5005/small_list/get_list/' + large_category_id + '">' + large_category_name + '</a>',
      ' > ' + small_category_name,
    );


    for (index = 0; index < data_list.length; index++) {

      data = data_list[index];
      let card_id = data['card_id']
      let card_name = data['card_name']
      let is_reaf = data['is_reaf']

      if(is_reaf == true){
        let note_content = data['note_content']

        $('#js-Data-Wrapper-ListCards').append(
          '<form action="/put_card/view/' + card_id + '" method="post" id="tmp' + index + '">',
        );
        $('#tmp' + index).append(
          '<input type="hidden" name="card_id" value="' + card_id +  '">',
          '<input type="submit" id="' + card_id + '" class="a-Reaf value="' + card_name + '" name="作成済のしおりです。">',          
        );
      }

      if(is_reaf == false){
        let note_content = data['note_content']

        $('#js-Data-Wrapper-ListCards').append(
          '<form action="/put_card/view/' + card_id + '" method="post" id="tmp' + index + '">',
        );
        $('#tmp' + index).append(
          '<input type="hidden" name="card_id" value="' + card_id +  '">',
          '<input type="submit" id="' + card_id + '" class="Card_List_Btn" value="' + card_name + '" name="' + note_content + '">',
        );
      }
    }
    display_note();
})};


// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
// ノート表示
// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
function display_note(){

  $('.Card_List_Btn').mouseover(function () {
    remove_note();

    var value = this.value;
    $('#js-Data-Wrapper-NoteTitle').append(
      '<p id="js-Note-title" class="a-title">' + value + '</p>'
    );

    var note_content = this.name;
    var card_id = this.id;
    $('#js-Data-Wrapper-Note').append(
      '<input type="hidden" id="js-Hidden-Card" name="card_id" value="' + card_id + '">',
      '<textarea id="js-Note-Content" class="a-Note-Content" name="note_content">' + note_content + '</textarea>'
    );
  });
};

function remove_note(){
  $('#js-Note-title').remove();
  $('#js-Note-Content').remove();
  $('#js-Hidden-Card').remove();
}


// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
// 単語詳細表示
// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
if(document.URL.match(/put_card/)){
  $(document).ready(function() {

    var data_record = JSON.parse(data_json)

    $('.c-Link-Wrapper').append(
      '<a href="http://localhost:5005/large_list/get_list">ホーム</a>',
      ' > <a href="http://localhost:5005/small_list/get_list/' + data_record["large_category_id"] + '">' + data_record["large_category_name"] + '</a>',
      ' > <a href="http://localhost:5005/list_cards/get_list/' + data_record["small_category_id"] + '">' + data_record["small_category_name"] + '</a>',
    );

    var CardIdElement = document.querySelector('input[id="a-Hidden-Card"]')
    CardIdElement.setAttribute('value',data_record["card_id"]);

    var SortElement = document.querySelector('input[id="a-Sort"]')
    SortElement.setAttribute('value',data_record["sort_number"]);

    var CardElement = document.querySelector('input[id="a-Card"]')
    CardElement.setAttribute('value',data_record["card_name"]);

    var LargeElement = document.querySelector('input[id="a-Large"]')
    LargeElement.setAttribute('value',data_record["large_category_name"]);

    var SmallElement = document.querySelector('input[id="a-Small"]')
    SmallElement.setAttribute('value',data_record["small_category_name"]);

    var delete_btn_element = document.querySelector('form[id="js-Delete"]')
    delete_btn_element.setAttribute('action','/put_card/delete/' + data_record["small_category_id"]);

    var DeleteIdElement = document.querySelector('input[id="a-Hidden-Card-Delete"]')
    DeleteIdElement.setAttribute('value',data_record["card_id"]);

    $('#a-Note').append(data_record["note_content"]);
})};


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