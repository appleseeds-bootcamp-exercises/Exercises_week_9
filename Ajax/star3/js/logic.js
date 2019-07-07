const updateAirCon = () => {
    $.ajax({
        type: "GET",
        url: "https://itc-colors.appspot.com/aircon/state",
        data: {
        },
        dataType: "json",
        success: function (responsemsg) {
            updateAirConImage(responsemsg)
        },
        error: function (msg) {
            console.log("error");
            console.log(msg);
        },
    });
}
const updateAirConImage = (response) => {
    $("#airConState").html(response.mode ? '<img class="icon" src="images/Snowflake.png">'
        : '<img class="icon" src="images/off.png">' || "")
    $("#airConMode").html(response.state)
    $("#airConTemp").html(response.temp || "")
}

$(document).ready(
    () => {
        updateAirCon()
        setInterval(updateAirCon, 10000)
    }
);
