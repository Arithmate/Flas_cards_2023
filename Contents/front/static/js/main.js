
const LOCAL_HOST = "http://localhost:5005";


// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
// 大分類一覧
// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
if(document.URL.match(/large_category/)){
  $(document).ready(function() {

    var data_list = JSON.parse(data_json)

    for (index = 0; index < data_list.length; index++) {

      data = data_list[index];
      let large_category_id = data['large_category_id']
      let large_category_name = data['large_category_name']

      $('#js-Data-Wrapper-ListLargeCategory').append(
        '<form action="/small_category/get_list/' + large_category_id + '" method="post" id="tmp' + index + '">',
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
if(document.URL.match(/small_category/)){
  $(document).ready(function() {

    var data_list = JSON.parse(data_json)

    for (index = 0; index < data_list.length; index++) {

      data = data_list[index];
      let small_category_id = data['small_category_id']
      let small_category_name = data['small_category_name']

      $('#js-Data-Wrapper-ListSmallCategory').append(
        '<form action="/list_cards/get_list/' + small_category_id + '" method="post" id="tmp' + index + '">',
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

    for (index = 0; index < data_list.length; index++) {

      data = data_list[index];
      let card_id = data['card_id']
      let card_name = data['card_name']
      let note_content = data['note_content']

      $('#js-Data-Wrapper-ListCards').append(
        '<form action="/detail_card/' + card_id + '" method="post" id="tmp' + index + '">',
      );
      $('#tmp' + index).append(
        '<input type="hidden" name="card_id" value=' + card_id +  '>',
        '<input type="submit" id="' + card_id + '" class="Card_List_Btn" value="' + card_name + '" name="' + note_content + '">',
      );
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
    $('#js-Data-Wrapper-Note').append(
      '<p id="js-Note-Content" class="a-Note-Content">' + note_content + '</p>'
    );
  });
};

function remove_note(){
  $('#js-Note-title').remove();
  $('#js-Note-Content').remove();
}