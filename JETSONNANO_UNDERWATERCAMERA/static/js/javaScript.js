function capture(){
    var y = document.forms["AutoFrom"]["Timer"].value;
    var z = document.forms["AutoFrom"]["Counter"].value;
    if (y == "" || y == null) {
        alert("Chưa điền thông tin TIMER");
        return false;
    }
    if (z == "" || z == null) {
        alert("Chưa điền thông tin COUNTER");
        return false;
    }
    else{
        window.location.href = "{% url 'Auto' %}";
        Call_Auto()
    }
}