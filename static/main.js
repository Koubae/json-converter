
var ciao = 4;

var ideaTheme = "idea";
var darculaTheme = "darcula";
var userTheme = darculaTheme;
// Body
var body = document.querySelector("body");
var background_ = "linear-gradient(0deg,  #7209fa 0%,  #240350 100%)";
var backgrounText = "rgb(255, 255, 255)";

// navBar
var navBar = document.getElementById("brandA");

// btn
var btn = document.querySelectorAll('.btn');

// a tag
var aTag = document.querySelectorAll('a');

// Input
var inPutEditor = CodeMirror.fromTextArea(document.getElementById("inputData"), {
    mode: "application/json",
    theme: ideaTheme,
    lineNumbers: true,
    autoCloseTags: true,
    tabSize: 2,
    value: 'null',
    scrollbarStyle: null
});


// Output
var outPutEditor = CodeMirror.fromTextArea(document.getElementById("outputWin"), {
    mode: "python",
    theme: ideaTheme,
    lineNumbers: false,
    autoCloseTags: true,
    tabSize: 2,
    value: "null",
    scrollbarStyle: null
});


// Theme Mode Switch
function toggleTheme(button) {
    var _switch = document.getElementById("themeToggle");
    
    if (_switch.checked){ 
        _switch.value = 'on';      
        // Code Mirror Theme
        inPutEditor.setOption('theme', darculaTheme);
        outPutEditor.setOption('theme', darculaTheme);
        
        // Webpage Style Theme;
        // Body
        body.style.background = background_;
        body.style.color = backgrounText;
        // navBar
        navBar.classList.remove("navbar-color-light", "cl-ligth");
        navBar.classList.add("navbar-color-dark", "cl-dark");
        // btn    
        for(i=0;i<btn.length; i++) {
            btn[i].classList.remove("btn-light");
            btn[i].classList.add("btn-dark");
        }
        // aTag
        for(i=0;i<aTag.length;i++) {
            aTag[i].classList.add("hiper-link-dark");
        }

    } else {
        _switch.value = 'off';
        inPutEditor.setOption('theme', ideaTheme);
        outPutEditor.setOption('theme', ideaTheme);

        // Webpage Style Theme;
        // Body
        body.style.background = null;
        body.style.color = null;
        // navBar
        navBar.classList.remove("navbar-color-dark", "cl-dark");
        navBar.classList.add("navbar-color-light", "cl-ligth");
        // btn
        for(i=0;i<btn.length; i++) {
            btn[i].classList.remove("btn-dark");
            btn[i].classList.add("btn-light");
        }
        // aTag
        for(i=0;i<aTag.length;i++) {
            aTag[i].classList.remove("hiper-link-dark");
        }


    }
    return userTheme;
}
// Call the function at least once, avoid a small bug defined below [1];
toggleTheme(); 

function switchMode(button){
    let left$Window = document.querySelector(".leftWindow");
    let right$Window = document.querySelector(".rightWindow");
    let btnSwitch = document.getElementById("modeSwitch");
    let valueSwitch = document.getElementById("mode&Switch$");
    let leftWindowTitle = document.getElementById('leftTitle');
    let rightWindowTitle = document.getElementById('rightTitle');
    
    if (btnSwitch.value == 'JSON') {        
        btnSwitch.value = 'python';
        valueSwitch.value = 'python';        
        // Right
        left$Window.removeAttribute('inputData');
        left$Window.id = 'outputWin';
        // Left
        right$Window.removeAttribute('outputWin');
        right$Window.id = 'inputData';
        // CodeMirror
        inPutEditor.setOption('mode', 'python');
        outPutEditor.setOption('mode', 'application/json');
        // WinTitle
        leftWindowTitle.innerHTML = 'Python Data';
        rightWindowTitle.innerHTML = 'JSON Object';
        console.log(btnSwitch.value);
        console.log(valueSwitch.value);
        return valueSwitch;
        
    }
    else {
        btnSwitch.value = 'JSON';
        valueSwitch.value = 'JSON';
        // Right
        right$Window.removeAttribute('inputData');
        right$Window.id = 'outputWin';
        // Left
        left$Window.removeAttribute('outputWin');
        left$Window.id = 'inputData';
        // CodeMirror
        inPutEditor.setOption('mode', 'application/json');
        outPutEditor.setOption('mode', 'python');
        // WinTitle
        leftWindowTitle.innerHTML = 'JSON Object';
        rightWindowTitle.innerHTML = 'Python Data';
        console.log(btnSwitch.value);
        console.log(valueSwitch.value);
        return valueSwitch;
    }
    
}


// POST
// fetch('/get-client', {
        
//     // Declare what type of data we're sending
//     headers: {
//         'Content-Type': 'application/json'
//     },

//     // Specify the method
//     method: 'POST',

//     // A JSON payload
//     body: JSON.stringify({"greeting": document.getElementById("mode&Switch$").value})
// })
//     .then(function (response) {
//         return response.text();
//     })
//     .then(function (text) {

//         console.log('POST response: ');

//         // Should be 'OK' if everything was successful
//         console.log(text);
//     });





// [1].
// If the pase is reloaded while the _switch checkbox is in darculaTheme, the theme will reset to White, so we need to call the function at least once so that sets the theme;



//
