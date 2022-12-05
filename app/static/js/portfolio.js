function stickymenu(navbar, sticky) {
    if (window.pageYOffset >= sticky) {
        navbar.classList.add("sticky")
    } else {
        navbar.classList.remove("sticky");
    }
}

function getVal(type, name) {
    z = type
    if (z == 'text' || z == 'del') {
    x = prompt("Enter Element:")
    } else if (z == 'image' || z == 'delimg') {
    temp = prompt("Enter Image URL:")
    x = ''
        for (var i = 0; i < temp.length; i++) {
            if (temp[i] == '/') {
                x += '^'
            } else {
                x += temp[i]
            }
        }
    }

    if (z == 'text' || z == 'image') {
        y = prompt("Enter CSS:")
    } else {
        y = ''
    }
    n = name
    const request = new XMLHttpRequest();
    if (z == 'text') {
        request.open('POST', `/process_info/${JSON.stringify( [x, y, z, n] )}`);
    } else if (z == 'del') {
        request.open('POST', `/process_info/${JSON.stringify( [x, y, z, n] )}`);
    } else if (z == 'image' || z == 'delimg') {
        request.open('POST', `/process_info/${JSON.stringify( [x, y, z, n] )}`);
    }
    request.send();
}