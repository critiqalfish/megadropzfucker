function copyToClipBoard(id) {
    var range = document.createRange();
    range.selectNode(document.getElementById(id));
    window.getSelection().removeAllRanges(); // clear current selection
    window.getSelection().addRange(range); // to select text
    document.execCommand("copy");
    alert("Copied the text: " + range);
    window.getSelection().removeAllRanges();// to deselect
}
function copy1(){
    navigator.clipboard.writeText
    ("Dextromethorphanhydrobromid#8794");
    alert("Copied the Dicord-Tag: Dextromethorphanhydrobromid#8794" );
}
function copy2(){
    navigator.clipboard.writeText
    ("1,3,7-Trimethylxanthin#4309");
    alert("Copied the Discord-Tag: Dextromethorphanhydrobromid#8794" );
}
