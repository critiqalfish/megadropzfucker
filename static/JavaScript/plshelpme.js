function copyToClipBoard(id) {
    var range = document.createRange();
    range.selectNode(document.getElementById(id));
    window.getSelection().removeAllRanges(); // clear current selection
    window.getSelection().addRange(range); // to select text
    document.execCommand("copy");
    alert("Copied the text: " + range);
    window.getSelection().removeAllRanges();// to deselect
}