const getColors = () => {
    $.ajax({
        type: "GET",
        url: "https://itc-colors.appspot.com/colors",
        data: {
        },
        dataType: "json",
        success: function (responsemsg) {
            printColors(responsemsg)
        },
        error: function (msg) {
            console.log("error");
        },
    });
}
const printColors = (response) => {
    let parsedResponse = response.map(element =>
        ` ${element["name"]}`
    );
    $("#userMessage").empty();
    parsedResponse.forEach(element => {
        $("#userMessage").append($(`<p>${element}</p>`));

    });
}
const addColor = () => {
    $.ajax({
        type: "POST",
        url: "https://itc-colors.appspot.com/add_color",
        data: {
            color: `${$("#colorInput").val()}`
        },
        dataType: "json",
        success: function (responsemsg) {
            printColors(responsemsg)
            console.log("success")
        },
        error: function (msg) {
            $("#userMessage").html($(`<p>Added to the serve, unknown error recieved</p>`));
            console.log("error");
        },
    });
}

$(document).ready(
    () => {
        $("#getColorList").click(getColors);
        $("#addColor").click(addColor);
    }
);
