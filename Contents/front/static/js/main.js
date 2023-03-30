
const LOCAL_HOST = "http://localhost:5005";


// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
// 大分類一覧
// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
$('#js-Data-Wrapper-ListLargeCategory').ready(function() {

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
  return
});


// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
// 小分類一覧
// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
$('#js-Data-Wrapper-ListSmallCategory').ready(function() {

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
  return
});


// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
// 単語帳一覧
// ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
$('#js-Data-Wrapper-ListCards').ready(function() {

  var data_list = JSON.parse(data_json)

  for (index = 0; index < data_list.length; index++) {

    data = data_list[index];
    let card_id = data['card_id']
    let card_name = data['card_name']
    let note_content = data['note_content']

    $('#js-Data-Wrapper-ListCards').append(
      '<form action="/detail_card/' + card_id + '" method="post" id="tmp' + index + '">',
      '</form>'
    );
    $('#tmp' + index).append(
      '<input type="hidden" name="card_id" value=' + card_id +  '>',
      '<input type="hidden" id="Note_Content" name="note_content" value=' + note_content +  '>',
      '<input type="submit" class="List_Btn" value=' + card_name +  '>',
    );
  }
  return
});