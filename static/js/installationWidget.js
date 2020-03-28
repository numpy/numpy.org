// let linux = document.getElementById('linux');
// let macos = document.getElementById('macos');
// let windows = document.getElementById('windows');
// let conda = document.getElementById('conda');
// let pip = document.getElementById('pip');
// let source = document.getElementById('source');
// let py36 = document.getElementById('3.6');
// let py37 = document.getElementById('3.7');
// let py38 = document.getElementById('3.8');

const replyClick = () => {
    alert("Button clicked, id " + this.id);
    console.log("installationWidget runs");
}

document.getElementById('linux').onclick = replyClick();
document.getElementById('macos').onclick = replyClick();
document.getElementById('windows').onclick = replyClick();