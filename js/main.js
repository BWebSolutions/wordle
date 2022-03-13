function start() {
    for (var i = 0; i < 5; i++)
        document.getElementById("block"+i).style.color = "#000";
    loadSelect();
}

function toggleBlock(block) {
    switch (document.getElementById(block).style.backgroundColor) {
        case 'rgb(119, 119, 119)':
            // was gray, change to yellow
            document.getElementById(block).style.backgroundColor = 'rgb(211, 189, 91)';
            break;
        case 'rgb(211, 189, 91)':
            // was yellow, change to green
            document.getElementById(block).style.backgroundColor = 'rgb(106, 170, 100)';
            break;
        default:
            // change to gray
            document.getElementById(block).style.backgroundColor = 'rgb(119, 119, 119)';
            document.getElementById(block).style.color = 'white';
            break;
    }
}

function filter() {
    for (var i = 0; i < 5; i++) {
        var block = document.getElementById("block" + i);

        switch (block.style.backgroundColor) {
            case 'rgb(106, 170, 100)':
                filterGreen(block.value.toLowerCase(), i);
                dictGreen[i] = block.value;
                break;
            case 'rgb(211, 189, 91)':
                filterYellow(block.value.toLowerCase(), i);
                break;
            case 'rgb(119, 119, 119)':
                filterGray(block.value.toLowerCase());
                break;
        }
    }

    loadSelect();
    showHistory();
}

function filterGreen(c, place) {
    var x = [];
    var j = 0;

    for (var i = 0; i < w.length; i++) {
        if (w[i].indexOf(c) == place) {
            x[j] = w[i];
            j++;
        }
    }
    w = x;
}

function filterYellow(c, place) {
    var x = [];
    var j = 0;

    for (var i = 0; i < w.length; i++) {
        if (w[i].indexOf(c) > -1 && w[i].indexOf(c) != place) {
            x[j] = w[i];
            j++;
        }
    }
    w = x;
}

function filterGray(c) {
    var x = [];
    var j = 0;

    for (var i = 0; i < w.length; i++) {
        if (w[i].indexOf(c) == -1) {
            x[j] = w[i];
            j++;
        }
    }
    w = x;
}


function loadSelect() {
    var select = document.getElementById("arr");

    emptySelect(select);

    for (var i = 0; i < w.length; i++) {
        var optn = w[i].toUpperCase();
        var el = document.createElement("option");
        el.textContent = optn;
        el.value = optn;
        select.appendChild(el);
    }
}

function emptySelect(selectElement) {
    var i, L = selectElement.options.length - 1;
    for (i = L; i >= 0; i--) {
        selectElement.remove(i);
    }
}

function selectWord() {
    var select = document.getElementById("arr");
    var selectedText = select.options[select.selectedIndex].text;
    for (var i = 0; i < selectedText.length; i++) {
        block = document.getElementById("block" + i);
        block.value = selectedText[i];

        if (dictGreen[i] == block.value) {
            block.style.backgroundColor = 'rgb(106, 170, 100)';
            block.style.color = '#fff';
        }
        else {
            block.style.backgroundColor = 'rgb(119, 119, 119)';
            block.style.color = '#fff';
        }
    }
}

function showHistory() {
    if (historyRow < 5) {
        document.getElementById("guess" + historyRow).style.display = 'block';
        for (var i = 0; i <= 4; i++) {
            block = document.getElementById("block" + i);
            newBlock = document.getElementById("block" + historyRow + i);
            newBlock.value = block.value;
            newBlock.style.color = block.style.color;
            newBlock.style.backgroundColor = block.style.backgroundColor;

            block.value = '';
            block.style.color = 'black';
            block.style.backgroundColor = 'white';
        }
        historyRow++;
    }

}