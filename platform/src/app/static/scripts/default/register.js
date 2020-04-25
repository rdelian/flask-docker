window.onload = function () {
    let user_id = getUrlParameter('id')
    console.log(`Param 'id'=${user_id}`);
    if (user_id) {
        document.getElementById('user_id').value = user_id
    }
    else if (!document.getElementById('user_id').value) {
        window.location.replace("/");
    }
    console.log("Form.user_id=" + document.getElementById('user_id').value);
};