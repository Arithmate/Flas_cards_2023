
var data_list = [];
var sub_list = [];
const LOCAL_HOST = "http://localhost:5005";

function displayList(data_list) {
  let $target = $("#js-Data-Wrapper");
  let data;

  for (index = 0; index < data_list.length; index++) {
    data = data_list[index];
    $target.append(`
      <div>
        <p>`+ data + `</p>
      </div>
      `)
  }
}

$('#js-Btn').on('click', function () {
  var url = LOCAL_HOST + "/small_category/view"

  fetch(url)
});

$('#js-Data-Wrapper-ListCards').ready(function () {
  var url = LOCAL_HOST + "/small_category/get_list"
  const data_list = fetch(url)
  let $target = $("#js-Data-Wrapper-ListCards");

  displayListBack(data_list, $target);
});


function displayListBack(data_list, $target) {
  
  let data;
  

  for (index = 0; index < data_list.length; index++) {
    data = data_list[index];
    $target.append(`
      <div>
        <p>`+ data + `</p>
      </div>
      `)
  }
}

$('#js-Btn-Back').on('click', function () {
  const JSON_SEPARATOR = "Separator";

  var param = {
    url: "/api/user_detail",
    type: "post",
    dataType: "json",
  };

  $.ajax(param)
    .done(function (res) {
      console.log(res);
      var temo_json_list = res.content.split(JSON_SEPARATOR)
      for (var index = 0; index < Object.keys(temo_json_list).length; ++index) {
        data_list.push(JSON.parse(temo_json_list[index]));
      }
      displayListBack(data_list)

    }).fail(function (res) {
      alert("display NG");
    })
});