
var data_list = [];
var sub_list = [];

function displayList(data_list) {
  let $target = $("#js-Data-Wrapper");
  let data;

  for (index = 0; index < data_list.length; index++) {
    data = data_list[index];
    $target.append(`
      <div>
        <p>`+ data.user_name + `</p>
        <p>`+ data.job + `</p>
      </div>
      `)
  }
}

$('#js-Btn').on('click', function () {
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
      displayList(data_list)

    }).fail(function (res) {
      alert("display NG");
    })
});



function displayListSub(data_list) {
  let $target = $("#js-Data-Wrapper-Sub");
  let data;

  for (index = 0; index < data_list.length; index++) {
    data = data_list[index];
    $target.append(`
      <div>
        <p>`+ data.user_name + `</p>
        <p>`+ data.job + `</p>
      </div>
      `)
  }
}

$('#js-Btn-Sub').on('click', function () {
  const JSON_SEPARATOR = "Separator";

  var param = {
    url: "/api/connect_sub",
    type: "post",
    dataType: "json",
  };


  $.ajax(param)
    .done(function (res) {
      console.log(res);
      var temo_json_list = res.content.split(JSON_SEPARATOR)
      for (var index = 0; index < Object.keys(temo_json_list).length; ++index) {
        sub_list.push(JSON.parse(temo_json_list[index]));
      }
      displayListSub(sub_list)

    }).fail(function (res) {
      alert("display NG");
    })
});

