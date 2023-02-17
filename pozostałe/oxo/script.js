const board = document.querySelector('.board');
let squares = Array.from(document.querySelectorAll('.square'));
let currentPlayer = "X";

board.addEventListener('click', handleClick);

function handleClick(event) {
  const square = event.target;

  if (square.classList.contains('filled')) {
    return;
  }

  square.textContent = currentPlayer;
  square.classList.add('filled');
  checkForWin();
  switchPlayer();
}

function switchPlayer() {
  currentPlayer = currentPlayer === "X" ? "O" : "X";
}

function checkForWin() {
  const winningCombinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
  ];

  for (let i = 0; i < winningCombinations.length; i++) {
    const [a, b, c] = winningCombinations[i];
    if (squares[a].textContent === currentPlayer && squares[b].textContent === currentPlayer && squares[c].textContent === currentPlayer) {
      alert(`Gracz ${currentPlayer} wygrał!`);
      resetBoard();
      return;
    }
  }

  if (squares.every(square => square.classList.contains('filled'))) {
    alert(`Remis!`);
    resetBoard();
    return;
  }
}

function resetBoard() {
  squares.forEach(square => {
    square.textContent = '';
    square.classList.remove('filled');
  });
  currentPlayer = "X";
}

