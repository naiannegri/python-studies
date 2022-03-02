function rot13(str) {
    var decode = ""
    for (let i = 0; i < str.length; i++) {
      if (str.charAt(i) !== "" && str.charAt(i) !== "?" && str.charAt(i) !== ".") {
        decode += String.fromCharCode(13 + String.prototype.charCodeAt(str.charAt(i)))
      } else {
        decode += temp
      }
    }
    return decode;
    }
    
rot13("SERR PBQR PNZC");