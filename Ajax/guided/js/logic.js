$(document).ready(function () {
    //adding event listeners
    $('#createUserSubmit').bind('click', checkIfUserExists);
    $('#getUserSubmit').bind('click', showExistingUsers);
});

const users = []; //internal array of users
//Method that checks if the user exists in the internal array
checkIfUserExists = function () {

    var owner = $('#owner').val();
    var userName = $('#username').val();
    $.ajax({
        type: "POST",
        url: "https://itc-colors.appspot.com/add_user",
        data: {
            owner: owner,
            username: userName
        },
        dataType: "json",

        success: function (responsemsg) {
            if (responsemsg.msg) {
                console.log("worked!")
                console.log(responsemsg)
            }
        },
        error: function (msg) {
            console.log("error");
        },

    });

};

showExistingUsers = function () {
    $.ajax({
        type: "GET",
        url: "https://itc-colors.appspot.com/users",
        data: {
            owner: $('#owner').val()
        },
        dataType: "json",
        success: function (responsemsg) {
            console.log(responsemsg)
        },
        error: function (msg) {
            console.log("error");
        },
    });
};
