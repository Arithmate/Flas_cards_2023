
var data_list = [];
var sub_list = [];


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
  var param = {
    url: "/small_category/get_list",
    type: "get",
    dataType: "json",
  };

  $.ajax(param)
    .done(function (res) {
      console.log(res);
      var data_list_from_server = res.content
      for (var index = 0; index < data_list_from_server.length; ++index) {
        data_list_for_view.push(JSON.parse(data_list_from_server[index]));
      }
      displayList(data_list_for_view)

    }).fail(function (res) {
      alert("display NG");
    })
});

$('#js-Btn-Go-ListCards').on('click', function () {
  var param = {
    url: "/small_category/get_list",
    type: "get",
    dataType: "json",
  };
});


function displayListBack(data_list) {
  let $target = $("#js-Data-Wrapper-Back");
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