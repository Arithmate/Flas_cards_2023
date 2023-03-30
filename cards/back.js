

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