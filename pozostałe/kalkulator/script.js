function gen() {
    const main = document.getElementById("main");
    const display = document.createElement("input");
    display.setAttribute("type", "text");
    display.setAttribute("id", "display");
    display.setAttribute("disabled", true);
    main.appendChild(display);
  
    const keys = [
      ["C", "CE"],
      [7, 8, 9, "/"],
      [4, 5, 6, "*"],
      [1, 2, 3, "-"],
      [0, ".", "=", "+"],
    ];
  
    for (let i = 0; i < keys.length; i++) {
      const keyRow = document.createElement("div");
      keyRow.setAttribute("class", "key-row");
      for (let j = 0; j < keys[i].length; j++) {
        const key = document.createElement("button");
        key.innerText = keys[i][j];
        key.setAttribute("class", "key");
        key.setAttribute("onclick", "calculate(this)");
        keyRow.appendChild(key);
      }
      main.appendChild(keyRow);
    }
  }
  