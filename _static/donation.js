function open_window(cause_id) {
    var protocol = String(document.location.protocol);
    var new_url;
    if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
        new_url = "https://www.flipcause.com/widget/" + cause_id
        window.open(new_url);
    } else {
        document.getElementById("fc-fade").style.display = "block";
        document.getElementById("fc-fade").style.webkitAnimation = "backfadesin 1s";
        document.getElementById("fc-fade").style.animation = "backfadesin 1s";
        document.getElementById("fc-fade").style.mozAnimation = "backfadesin 1s";
        document.getElementById("fc-light").style.display = "block";
        document.getElementById("fc-light").style.webkitAnimation = "fadesin 1.5s";
        document.getElementById("fc-light").style.animation = "fadesin 1.5s";
        document.getElementById("fc-light").style.mozAnimation = "fadesin 1.5s";
        document.getElementById("fc-main").style.display = "block";
        document.getElementById("fc-main").style.webkitAnimation = "fadesin 1.5s";
        document.getElementById("fc-main").style.animation = "fadesin 1.5s";
        document.getElementById("fc-main").style.mozAnimation = "fadesin 1.5s";
        document.getElementById("fc-close").style.display = "block";
        document.getElementById("fc-close").style.webkitAnimation = "fadesin 1.5s";
        document.getElementById("fc-close").style.animation = "fadesin 1.5s";
        document.getElementById("fc-close").style.mozAnimation = "fadesin 1.5s";
        document.getElementById("fc-myFrame").style.display = "block";
        document.getElementById("fc-myFrame").style.webkitAnimation = "fadesin 1.5s";
        document.getElementById("fc-myFrame").style.animation = "fadesin 1.5s";
        document.getElementById("fc-myFrame").style.mozAnimation = "fadesin 1.5s";
        document.getElementById("fc-myFrame").src = "https://www.flipcause.com/widget/" + cause_id;
    }
}

function close_window() {
    document.getElementById("fc-fade").style.display = "none";
    document.getElementById("fc-light").style.display = "none";
    document.getElementById("fc-main").style.display = "none";
    document.getElementById("fc-close").style.display = "none";
    document.getElementById("fc-myFrame").style.display = "none";
}
