let idNum = 1;

const processedData = {};

window.addEventListener('hashchange', function () {
    const selectedId = window.location.hash.substring(1);
    showSelectedSection(selectedId);
});

function showSelectedSection(selectedId) {
    const containerSections = document.querySelectorAll('.row-fadeIn-wrapper');

    containerSections.forEach(function (section) {
        const sectionId = section.id;
        if (sectionId === selectedId) {
            section.style.display = 'block';
        } else {
            section.style.display = 'none';
        }
    });
}

function updatePortRes() {
    const filePath = "http://localhost:8000/http/out.json";
    fetch(filePath)
        .then(response => {
            if (!response.ok) {
                throw new Error('Error: JSON file not found');
            }
            return response.json();
        })
        .then(jsonData => {
            ParsePortRes(jsonData);
        })
        .catch(error => {
            console.error(error.message);
        });
}

function ParsePortRes(data) {
    const container = document.getElementById('ScanResults');

    for (const ip in data.port_scan) {
        if (!processedData[ip]) {
            listIP(ip);

            for (const port in data.port_scan[ip]) {
                const portInfo = data.port_scan[ip][port];

                if (!processedData[ip] || !processedData[ip].has(port)) {
                    const sectionElement = createSectionElement(idNum, port, portInfo.name, portInfo.product, portInfo.version);
                    container.appendChild(sectionElement);

                    if (!processedData[ip]) {
                        processedData[ip] = new Set();
                    }
                    processedData[ip].add(port);
                }
            }
            idNum++;
        }
    }
}


function listIP(ip) {
    var listItem = document.createElement('li');
    listItem.style.setProperty('--index', idNum+1);
    listItem.className = "ipLi";
    var link = document.createElement('a');
    link.href = `#${idNum}`;
    link.rel = 'noreferrer noopener';
    link.className = "ipA";
    var span = document.createElement('span');
    span.className = "ipSpan";
    span.innerHTML = ip;
    var svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('role', 'img');
    svg.setAttribute('viewBox', '0 0 24 24');
    var title = document.createElement('title');
    svg.appendChild(title);
    span.appendChild(svg);
    link.appendChild(span);
    listItem.appendChild(link);
    document.getElementById("ipList").appendChild(listItem);
}

function createSectionElement(id, port, name, product, version) {
    const sectionElement = document.createElement('section');
    sectionElement.classList.add('row-fadeIn-wrapper');
    sectionElement.id = id;
    const articleElement = document.createElement('article');
    articleElement.classList.add('row', 'nfl');

    const ulElement = document.createElement('ul');
    ulElement.appendChild(createLiElement('Port', port));
    ulElement.appendChild(createLiElement('Type', name));
    ulElement.appendChild(createLiElement('Product', product));
    ulElement.appendChild(createLiElement('Version', version));

    articleElement.appendChild(ulElement);

    const moreContentElement = document.createElement('ul');
    moreContentElement.classList.add('more-content');
    const liDescription = document.createElement('li');
    liDescription.textContent = `Info about ${product}`;
    moreContentElement.appendChild(liDescription);

    articleElement.appendChild(moreContentElement);

    sectionElement.appendChild(articleElement);

    return sectionElement;
}

function createLiElement(label, text) {
    const liElement = document.createElement('li');
    liElement.textContent = text;

    if (label === 'Port') {
        const aElement = document.createElement('a');
        aElement.href = `#`;
        aElement.textContent = text;
        liElement.innerHTML = '';
        liElement.appendChild(aElement);
    }

    return liElement;
}
