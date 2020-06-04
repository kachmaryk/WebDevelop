$(document).ready(function () {
    let csrfToken = $("input[name=csrfmiddlewaretoken]").val();
    $("#contactDiv").on("click", "button.close", function (event) {
        event.stopPropagation();
        var dataId = $(this).data("id");
        $.ajax({
            url: '/contact_list/' + dataId + '/delete/',
            data: {
                csrfmiddlewaretoken: csrfToken,
                id: dataId
            },
            type: "post",
            dataType: "json",
            success: function () {
                $('#contactList[data-Id = "'+ dataId +'"]').remove();
            }
        })
    })
});