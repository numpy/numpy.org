var osContainer = document.getElementById("os"); // Gets the container Element
var osOptions = osContainer.getElementsByClassName("option"); // Get all buttons with class="option" inside the container, as an HTMLCollection

var packageContainer = document.getElementById("package"); // Repeat for other rows
var packageOptions = packageContainer.getElementsByClassName("option");

var versionContainer = document.getElementById("version");
var versionOptions = versionContainer.getElementsByClassName("option");

updateCommand = () => {
    var selectedOptions = document.getElementsByClassName("selected") // Live HTMLCollection
    var osId = selectedOptions[0].id // selectedOptions[0] is a Node from above live HTMLCollection, Node is similar to Element. selectedOptions[0].id returns the id value of the Node. Syntax is 'Element.id'
    var packageId = selectedOptions[1].id // returns string data type
    var versionId = selectedOptions[2].id

    console.log(`OS is `, osId, `and package is `, packageId, `and version is `, versionId)

   // Method 3) Using switch instead of if statement
   switch(packageId) {
       case 'source':
           switch(osId) {
                case 'linux':
                    document.getElementByTagName("pre").innerHTML = "Go to [linux-specific url] for instructions on downloading from source.";
                    break;
                case 'macos':
                    document.getElementById("command").innerHTML = "Go to [macos-specific url] for instructions on downloading from source.";
                    break;
                case 'windows':
                    document.getElementById("command").innerHTML = "Go to [windows-specific url] for instructions on downloading from source.";
                    break;
                default:
                    document.getElementById("command").innerHTML = "Invalid set-up.";
            }
        break;

        case 'pip':
            switch(osId) {
                case 'linux':
                    switch(versionId) {
                        case '3.6':
                            document.getElementById("command").innerHTML = "pip install linux 3.6";
                            break;
                        case '3.7':
                            document.getElementById("command").innerHTML = "pip install linux 3.7";
                            break;
                        case '3.8':
                            document.getElementById("command").innerHTML = "pip install linux 3.8";
                            break;
                        default:
                            document.getElementById("command").innerHTML = "Invalid set-up.";
                    }
                break;

                case 'macos':
                    switch(versionId) {
                        case '3.6':
                            document.getElementById("command").innerHTML = "pip install macos 3.6";
                            break;
                        case '3.7':
                            document.getElementById("command").innerHTML = "pip install macos 3.7";
                            break;
                        case '3.8':
                            document.getElementById("command").innerHTML = "pip install macos 3.8";
                            break;
                        default:
                            document.getElementById("command").innerHTML = "Invalid set-up.";
                    }
                break;

                case 'windows':
                switch(versionId) {
                    case '3.6':
                        document.getElementById("command").innerHTML = "pip install windows 3.6";
                        break;
                    case '3.7':
                        document.getElementById("command").innerHTML = "pip install windows 3.7";
                        break;
                    case '3.8':
                        document.getElementById("command").innerHTML = "pip install windows 3.8";
                        break;
                    default:
                        document.getElementById("command").innerHTML = "Invalid set-up.";
                    }
                break;
            }
        break;

        case 'conda':
            switch(osId) {
                case 'linux':
                    switch(versionId) {
                        case '3.6':
                            document.getElementById("command").innerHTML = "conda install linux 3.6";
                            break;
                        case '3.7':
                            document.getElementById("command").innerHTML = "conda install linux 3.7";
                            break;
                        case '3.8':
                            document.getElementById("command").innerHTML = "conda install linux 3.8";
                            break;
                        default:
                            document.getElementById("command").innerHTML = "Invalid set-up.";
                    }
                break;

                case 'macos':
                    switch(versionId) {
                        case '3.6':
                            document.getElementById("command").innerHTML = "conda install macos 3.6";
                            break;
                        case '3.7':
                            document.getElementById("command").innerHTML = "conda install macos 3.7";
                            break;
                        case '3.8':
                            document.getElementById("command").innerHTML = "conda install macos 3.8";
                            break;
                        default:
                            document.getElementById("command").innerHTML = "Invalid set-up.";
                    }
                break;

                case 'windows':
                switch(versionId) {
                    case '3.6':
                        document.getElementById("command").innerHTML = "conda install windows 3.6";
                        break;
                    case '3.7':
                        document.getElementById("command").innerHTML = "conda install windows 3.7";
                        break;
                    case '3.8':
                        document.getElementById("command").innerHTML = "conda install windows 3.8";
                        break;
                    default:
                        document.getElementById("command").innerHTML = "Invalid set-up.";
                    }
                break;
            }
   }
}

// Loop through the buttons. Add and remove the active class to the clicked button
for (var i = 0; i < osOptions.length; i++) {
    osOptions[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("selected"); // returns an HTMLCollection, an interface that represents a generic collection (array-like object similar to arguments) of elements. An HTMLCollection in the HTML DOM is live; it is automatically updated when the underlying document is changed.
    console.log(`this is current`, current)
    current[0].className = current[0].className.replace(" selected", "");
    this.className += " selected";
    console.log(`osContainer`, osContainer)
    console.log(`osOptions`, osOptions)
    updateCommand()
  });
}

for (var i = 0; i < packageOptions.length; i++) {
    packageOptions[i].addEventListener("click", function() {
    var current = packageContainer.getElementsByClassName("selected");
    console.log(`this is current`, current)
    current[0].className = current[0].className.replace(" selected", "");
    this.className += " selected";
    console.log(`packageContainer `,packageContainer)
    console.log(`packageOptions `,packageOptions)
    updateCommand()
  });
}

for (var i = 0; i < versionOptions.length; i++) {
    versionOptions[i].addEventListener("click", function() {
    var current = versionContainer.getElementsByClassName("selected");
    console.log(`this is current`, current)
    current[0].className = current[0].className.replace(" selected", "");
    this.className += " selected";
    console.log(`versionContainer `,versionContainer)
    console.log(`versionOptions `,versionOptions)
    updateCommand()
  });
}